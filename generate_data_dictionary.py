#!/usr/bin/env python3
"""
Generate comprehensive data dictionary from database schema exports
Handles operator-specific replica databases
"""
import csv
import os
from collections import defaultdict
from pathlib import Path
import json

class DataDictionaryGenerator:
    def __init__(self, csv_dir='CSVs'):
        self.csv_dir = csv_dir
        self.tables = {}
        self.columns = defaultdict(list)
        self.indexes = defaultdict(list)
        self.foreign_keys = defaultdict(list)
        self.check_constraints = {}
        self.extended_props = {}
        self.table_info = {}
        
    def read_csv(self, filename):
        """Read CSV file and return list of dicts"""
        filepath = os.path.join(self.csv_dir, filename)
        if not os.path.exists(filepath):
            print(f"Warning: {filename} not found")
            return []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def load_all_data(self):
        """Load all CSV exports"""
        print("Loading schema data...")
        
        # Load tables
        tables_data = self.read_csv('TABLES.csv')
        for row in tables_data:
            key = (row['TABLE_SCHEMA'], row['TABLE_NAME'])
            self.tables[key] = {
                'catalog': row.get('TABLE_CATALOG', ''),
                'schema': row['TABLE_SCHEMA'],
                'name': row['TABLE_NAME'],
                'type': row.get('TABLE_TYPE', 'BASE TABLE')
            }
        print(f"  Loaded {len(self.tables)} tables")
        
        # Load columns
        columns_data = self.read_csv('COLUMNS.csv')
        for row in columns_data:
            key = (row['TABLE_SCHEMA'], row['TABLE_NAME'])
            self.columns[key].append({
                'name': row['COLUMN_NAME'],
                'position': int(row['ORDINAL_POSITION']),
                'default': row.get('COLUMN_DEFAULT', ''),
                'nullable': row['IS_NULLABLE'] == 'YES',
                'data_type': row['DATA_TYPE'],
                'char_max_length': row.get('CHARACTER_MAXIMUM_LENGTH', ''),
                'numeric_precision': row.get('NUMERIC_PRECISION', ''),
                'numeric_scale': row.get('NUMERIC_SCALE', ''),
                'datetime_precision': row.get('DATETIME_PRECISION', '')
            })
        print(f"  Loaded {sum(len(cols) for cols in self.columns.values())} columns")
        
        # Load indexes
        indexes_data = self.read_csv('indexes.csv')
        for row in indexes_data:
            key = (row['SchemaName'], row['TableName'])
            self.indexes[key].append({
                'name': row['IndexName'],
                'type': row['IndexType'],
                'unique': row['IsUnique'].lower() == 'true',
                'primary_key': row['IsPrimaryKey'].lower() == 'true',
                'column': row['ColumnName'],
                'ordinal': int(row['KeyOrdinal']),
                'included': row['IsIncludedColumn'].lower() == 'true'
            })
        print(f"  Loaded {len(indexes_data)} index columns")
        
        # Load foreign keys
        ref_constraints = self.read_csv('referential_constraints.csv')
        constraint_columns = self.read_csv('constraint_column_usage.csv')
        
        # Build FK map
        fk_map = {}
        for row in ref_constraints:
            fk_name = row['CONSTRAINT_NAME']
            fk_map[fk_name] = {
                'pk_constraint': row['UNIQUE_CONSTRAINT_NAME'],
                'delete_rule': row.get('DELETE_RULE', ''),
                'update_rule': row.get('UPDATE_RULE', '')
            }
        
        # Map columns to constraints
        col_constraint_map = defaultdict(list)
        for row in constraint_columns:
            constraint_name = row['CONSTRAINT_NAME']
            col_constraint_map[constraint_name].append({
                'table_schema': row['TABLE_SCHEMA'],
                'table_name': row['TABLE_NAME'],
                'column_name': row['COLUMN_NAME']
            })
        
        # Build FK relationships
        for fk_name, fk_info in fk_map.items():
            fk_cols = col_constraint_map.get(fk_name, [])
            pk_cols = col_constraint_map.get(fk_info['pk_constraint'], [])
            
            if fk_cols and pk_cols:
                fk_table = (fk_cols[0]['table_schema'], fk_cols[0]['table_name'])
                self.foreign_keys[fk_table].append({
                    'name': fk_name,
                    'from_column': fk_cols[0]['column_name'],
                    'to_schema': pk_cols[0]['table_schema'],
                    'to_table': pk_cols[0]['table_name'],
                    'to_column': pk_cols[0]['column_name'],
                    'delete_rule': fk_info['delete_rule'],
                    'update_rule': fk_info['update_rule']
                })
        print(f"  Loaded {sum(len(fks) for fks in self.foreign_keys.values())} foreign keys")
        
        # Load check constraints
        check_data = self.read_csv('CHECK_CONSTRAINTS.csv')
        for row in check_data:
            self.check_constraints[row['CONSTRAINT_NAME']] = row.get('CHECK_CLAUSE', '')
        print(f"  Loaded {len(self.check_constraints)} check constraints")
        
        # Load extended properties
        ext_props = self.read_csv('extended_properties.csv')
        for row in ext_props:
            if row.get('PropertyName') == 'MS_Description' and row.get('PropertyValue'):
                key = (
                    row.get('SchemaName', ''),
                    row.get('ObjectName', ''),
                    row.get('ColumnName', '')
                )
                self.extended_props[key] = row['PropertyValue'].strip('"')
        print(f"  Loaded {len(self.extended_props)} descriptions")
        
        print("\nData loading complete!\n")
    
    def get_column_type_display(self, col):
        """Format column data type for display"""
        dtype = col['data_type']
        
        if col['char_max_length']:
            if col['char_max_length'] == '-1':
                return f"{dtype}(MAX)"
            return f"{dtype}({col['char_max_length']})"
        elif col['numeric_precision']:
            if col['numeric_scale']:
                return f"{dtype}({col['numeric_precision']},{col['numeric_scale']})"
            return f"{dtype}({col['numeric_precision']})"
        elif col['datetime_precision']:
            return f"{dtype}({col['datetime_precision']})"
        
        return dtype
    
    def get_table_primary_keys(self, schema, table):
        """Get primary key columns for a table"""
        key = (schema, table)
        if key not in self.indexes:
            return []
        
        pk_cols = []
        for idx in self.indexes[key]:
            if idx['primary_key'] and not idx['included']:
                pk_cols.append((idx['ordinal'], idx['column']))
        
        return [col for _, col in sorted(pk_cols)]
    
    def get_table_references(self, schema, table):
        """Find all tables that reference this table"""
        references = []
        target_table = f"{schema}.{table}"
        
        for table_key, fks in self.foreign_keys.items():
            for fk in fks:
                if f"{fk['to_schema']}.{fk['to_table']}" == target_table:
                    references.append({
                        'from_schema': table_key[0],
                        'from_table': table_key[1],
                        'from_column': fk['from_column'],
                        'to_column': fk['to_column']
                    })
        
        return references
    
    def generate_table_markdown(self, schema, table):
        """Generate Markdown documentation for a single table"""
        key = (schema, table)
        table_info = self.tables.get(key, {})
        columns = sorted(self.columns.get(key, []), key=lambda x: x['position'])
        fks = self.foreign_keys.get(key, [])
        refs = self.get_table_references(schema, table)
        pk_cols = self.get_table_primary_keys(schema, table)
        
        # Get table description
        table_desc = self.extended_props.get((schema, table, ''), '')
        
        md = []
        md.append(f"# {table}\n")
        md.append(f"**Schema:** `{schema}`  ")
        md.append(f"**Type:** {table_info.get('type', 'BASE TABLE')}  ")
        md.append(f"**Database:** {table_info.get('catalog', '')} (Operator Replica)\n")
        
        if table_desc:
            md.append(f"## Description\n\n{table_desc}\n")
        else:
            md.append(f"## Description\n\n*No description available*\n")
        
        # Columns section
        md.append(f"## Columns ({len(columns)})\n")
        md.append("| Column | Type | Nullable | Default | Keys | Description |")
        md.append("|--------|------|----------|---------|------|-------------|")
        
        for col in columns:
            col_name = col['name']
            col_type = self.get_column_type_display(col)
            nullable = "YES" if col['nullable'] else "**NO**"
            default = col['default'][:30] if col['default'] else "-"
            
            # Determine keys
            keys = []
            if col_name in pk_cols:
                keys.append("PK")
            for fk in fks:
                if fk['from_column'] == col_name:
                    keys.append(f"FK->`{fk['to_table']}`")
            key_str = "<br/>".join(keys) if keys else "-"
            
            # Get column description
            col_desc = self.extended_props.get((schema, table, col_name), '-')
            
            md.append(f"| `{col_name}` | `{col_type}` | {nullable} | `{default}` | {key_str} | {col_desc} |")
        
        md.append("")
        
        # Foreign Keys section
        if fks:
            md.append("## Foreign Key Relationships\n")
            md.append("### This Table References (Parent Tables):\n")
            for fk in fks:
                delete_rule = f" `ON DELETE {fk['delete_rule']}`" if fk['delete_rule'] else ""
                md.append(f"- **`{fk['to_schema']}.{fk['to_table']}`** ")
                md.append(f"  via `{fk['from_column']}` → `{fk['to_column']}`{delete_rule}")
            md.append("")
        
        # Referenced by section
        if refs:
            md.append("### Referenced By (Child Tables):\n")
            for ref in refs:
                md.append(f"- **`{ref['from_schema']}.{ref['from_table']}`** ")
                md.append(f"  via `{ref['from_column']}` → `{ref['to_column']}`")
            md.append("")
        
        # Indexes section
        if key in self.indexes:
            # Group indexes by name
            idx_groups = defaultdict(list)
            for idx in self.indexes[key]:
                idx_groups[idx['name']].append(idx)
            
            md.append("## Indexes\n")
            for idx_name, idx_cols in sorted(idx_groups.items()):
                idx_type = idx_cols[0]['type']
                is_unique = idx_cols[0]['unique']
                is_pk = idx_cols[0]['primary_key']
                
                # Build column list
                key_cols = sorted([c for c in idx_cols if not c['included']], key=lambda x: x['ordinal'])
                included_cols = sorted([c for c in idx_cols if c['included']], key=lambda x: x['ordinal'])
                
                col_list = ", ".join([c['column'] for c in key_cols])
                if included_cols:
                    col_list += f" INCLUDE ({', '.join([c['column'] for c in included_cols])})"
                
                # Build description
                desc_parts = []
                if is_pk:
                    desc_parts.append("PRIMARY KEY")
                if is_unique:
                    desc_parts.append("UNIQUE")
                desc_parts.append(idx_type)
                desc = " ".join(desc_parts)
                
                md.append(f"- **`{idx_name}`** ({desc})")
                md.append(f"  - Columns: `{col_list}`")
            md.append("")
        
        return "\n".join(md)
    
    def generate_index_page(self):
        """Generate index page with table of contents"""
        md = []
        md.append("# Database Data Dictionary\n")
        md.append("**Database Type:** Operator-Specific Replica Database  ")
        md.append("**Source:** Core Database (Filtered/Replicated Tables)\n")
        md.append("**Note:** This documentation reflects an operator-specific replica. ")
        md.append("Not all core database tables are replicated to operator databases.\n")
        
        # Statistics
        total_tables = len(self.tables)
        total_columns = sum(len(cols) for cols in self.columns.values())
        total_fks = sum(len(fks) for fks in self.foreign_keys.values())
        
        md.append("## Statistics\n")
        md.append(f"- **Tables:** {total_tables}")
        md.append(f"- **Columns:** {total_columns}")
        md.append(f"- **Foreign Keys:** {total_fks}")
        md.append(f"- **Schemas:** {len(set(t[0] for t in self.tables.keys()))}\n")
        
        # Group tables by schema
        schema_tables = defaultdict(list)
        for (schema, table) in sorted(self.tables.keys()):
            schema_tables[schema].append(table)
        
        md.append("## Tables by Schema\n")
        for schema in sorted(schema_tables.keys()):
            md.append(f"### {schema} Schema\n")
            for table in sorted(schema_tables[schema]):
                col_count = len(self.columns.get((schema, table), []))
                pk_cols = self.get_table_primary_keys(schema, table)
                pk_str = f" - PK: `{', '.join(pk_cols)}`" if pk_cols else ""
                md.append(f"- [`{table}`](schemas/{schema}/{table}.md) ({col_count} columns{pk_str})")
            md.append("")
        
        md.append("## Entity Relationship Diagrams\n")
        md.append("- [Full ERD - Horizontal Layout](../erd_full.mmd)")
        md.append("- [Full ERD - Vertical Layout](../erd_full_vertical.mmd)")
        md.append("- [DBO Schema ERD](../erd_dbo.mmd)")
        md.append("- [DBO Schema ERD - Vertical](../erd_dbo_vertical.mmd)\n")
        
        md.append("## Quick Reference\n")
        md.append("- [Search All Tables](#tables-by-schema)")
        md.append("- View ERD diagrams in VS Code with Mermaid extension")
        md.append("- Or paste .mmd contents into https://mermaid.live\n")
        
        return "\n".join(md)
    
    def generate_all(self, output_dir='docs'):
        """Generate complete data dictionary"""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        print(f"Generating data dictionary in '{output_dir}/'...\n")
        
        # Generate index
        print("Creating index page...")
        index_md = self.generate_index_page()
        with open(output_path / 'index.md', 'w', encoding='utf-8') as f:
            f.write(index_md)
        print(f"  [OK] index.md")
        
        # Generate table documentation
        schemas_path = output_path / 'schemas'
        schemas_path.mkdir(exist_ok=True)
        
        table_count = 0
        for (schema, table) in sorted(self.tables.keys()):
            schema_path = schemas_path / schema
            schema_path.mkdir(exist_ok=True)
            
            table_md = self.generate_table_markdown(schema, table)
            with open(schema_path / f'{table}.md', 'w', encoding='utf-8') as f:
                f.write(table_md)
            
            table_count += 1
            if table_count % 50 == 0:
                print(f"  Generated {table_count} tables...")
        
        print(f"  [OK] Generated {table_count} table documentation files\n")
        print("=" * 60)
        print("Data Dictionary Generation Complete!")
        print("=" * 60)
        print(f"\nView the documentation:")
        print(f"  Open: {output_dir}/index.md")
        print(f"  Or browse: {output_dir}/schemas/<schema>/<table>.md")
        print(f"\nTotal files generated: {table_count + 1}")

def main():
    print("=" * 60)
    print("  Data Dictionary Generator")
    print("  For Operator-Specific Replica Databases")
    print("=" * 60)
    print()
    
    generator = DataDictionaryGenerator(csv_dir='CSVs')
    generator.load_all_data()
    generator.generate_all(output_dir='docs')

if __name__ == '__main__':
    main()

