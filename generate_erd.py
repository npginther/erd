#!/usr/bin/env python3
"""
Generate ERD diagram from SQL Server INFORMATION_SCHEMA exports
"""
import csv
from collections import defaultdict
from pathlib import Path

def read_csv_file(filename):
    """Read CSV file and return rows as list of dicts"""
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def parse_constraints():
    """Parse all constraint CSV files and build relationship data"""
    
    print("Reading CSV files...")
    
    # Read all CSV files
    column_usage = read_csv_file('constraint_column_usage.csv')
    table_usage = read_csv_file('constraint_table_usage.csv')
    constraint_types = read_csv_file('table_constraints.csv')
    ref_constraints = read_csv_file('referential_constraints.csv')
    
    print(f"   - {len(column_usage)} constraint columns")
    print(f"   - {len(table_usage)} constraint tables")
    print(f"   - {len(constraint_types)} constraints")
    print(f"   - {len(ref_constraints)} foreign key relationships")
    
    # Build lookup dictionaries
    constraint_type_map = {}
    for row in constraint_types:
        key = (row['CONSTRAINT_SCHEMA'], row['CONSTRAINT_NAME'])
        constraint_type_map[key] = row['CONSTRAINT_TYPE']
    
    # Map constraint names to their columns
    constraint_columns = defaultdict(list)
    for row in column_usage:
        key = (row['CONSTRAINT_SCHEMA'], row['CONSTRAINT_NAME'])
        constraint_columns[key].append({
            'table_schema': row['TABLE_SCHEMA'],
            'table_name': row['TABLE_NAME'],
            'column_name': row['COLUMN_NAME']
        })
    
    # Map constraint names to referenced constraints
    fk_references = {}
    for row in ref_constraints:
        fk_key = (row['CONSTRAINT_SCHEMA'], row['CONSTRAINT_NAME'])
        pk_key = (row['UNIQUE_CONSTRAINT_SCHEMA'], row['UNIQUE_CONSTRAINT_NAME'])
        fk_references[fk_key] = {
            'pk_constraint': pk_key,
            'delete_rule': row['DELETE_RULE'],
            'update_rule': row['UPDATE_RULE']
        }
    
    # Build relationships
    relationships = []
    tables = defaultdict(lambda: {'primary_keys': [], 'columns': set()})
    
    for (schema, constraint_name), constraint_type in constraint_type_map.items():
        columns = constraint_columns.get((schema, constraint_name), [])
        
        if not columns:
            continue
            
        if constraint_type == 'PRIMARY KEY':
            # Track primary keys
            for col in columns:
                full_table = f"{col['table_schema']}.{col['table_name']}"
                tables[full_table]['primary_keys'].append(col['column_name'])
                tables[full_table]['columns'].add(col['column_name'])
        
        elif constraint_type == 'FOREIGN KEY':
            # Build FK relationships
            fk_info = fk_references.get((schema, constraint_name))
            if not fk_info:
                continue
            
            pk_columns = constraint_columns.get(fk_info['pk_constraint'], [])
            
            if columns and pk_columns:
                fk_col = columns[0]
                pk_col = pk_columns[0]
                
                from_table = f"{fk_col['table_schema']}.{fk_col['table_name']}"
                to_table = f"{pk_col['table_schema']}.{pk_col['table_name']}"
                
                # Track columns
                tables[from_table]['columns'].add(fk_col['column_name'])
                tables[to_table]['columns'].add(pk_col['column_name'])
                
                relationships.append({
                    'from_schema': fk_col['table_schema'],
                    'from_table': fk_col['table_name'],
                    'from_column': fk_col['column_name'],
                    'to_schema': pk_col['table_schema'],
                    'to_table': pk_col['table_name'],
                    'to_column': pk_col['column_name'],
                    'constraint_name': constraint_name,
                    'delete_rule': fk_info['delete_rule'],
                    'update_rule': fk_info['update_rule']
                })
    
    return tables, relationships

def generate_mermaid_erd(tables, relationships, schema_filter=None):
    """Generate Mermaid ERD syntax"""
    
    # Filter by schema if specified
    if schema_filter:
        filtered_relationships = [r for r in relationships 
                                 if r['from_schema'] == schema_filter or r['to_schema'] == schema_filter]
        
        # Get unique tables involved
        table_names = set()
        for r in filtered_relationships:
            table_names.add(f"{r['from_schema']}.{r['from_table']}")
            table_names.add(f"{r['to_schema']}.{r['to_table']}")
        
        filtered_tables = {k: v for k, v in tables.items() if k in table_names}
    else:
        filtered_relationships = relationships
        filtered_tables = tables
    
    print(f"\nGenerating Mermaid ERD...")
    print(f"   - {len(filtered_tables)} tables")
    print(f"   - {len(filtered_relationships)} relationships")
    
    mermaid = ["erDiagram"]
    
    # Add table definitions with primary keys
    for table_full_name, table_info in sorted(filtered_tables.items()):
        schema, table = table_full_name.split('.')
        
        # Simplify table name for diagram
        table_display = f"{table}"
        
        if table_info['primary_keys']:
            pk_list = ', '.join(table_info['primary_keys'])
            mermaid.append(f"    {table_display} {{")
            for pk in table_info['primary_keys']:
                mermaid.append(f"        {pk} PK")
            mermaid.append(f"    }}")
    
    # Add relationships
    for rel in filtered_relationships:
        from_table = rel['from_table']
        to_table = rel['to_table']
        
        # Mermaid relationship syntax: From ||--o{ To : "relationship"
        # Many-to-one: child }o--|| parent
        label = f"{rel['from_column']} FK"
        
        # Determine cardinality based on delete rule
        if rel['delete_rule'] == 'CASCADE':
            # If cascade, child is dependent on parent
            mermaid.append(f"    {to_table} ||--o{{ {from_table} : \"{label}\"")
        else:
            # NO ACTION means less strict dependency
            mermaid.append(f"    {to_table} ||..o{{ {from_table} : \"{label}\"")
    
    return '\n'.join(mermaid)

def generate_mermaid_flowchart(tables, relationships, schema_filter=None):
    """Generate Mermaid flowchart with top-down orientation using subgraphs"""
    
    # Filter by schema if specified
    if schema_filter:
        filtered_relationships = [r for r in relationships 
                                 if r['from_schema'] == schema_filter or r['to_schema'] == schema_filter]
        
        # Get unique tables involved
        table_names = set()
        for r in filtered_relationships:
            table_names.add(f"{r['from_schema']}.{r['from_table']}")
            table_names.add(f"{r['to_schema']}.{r['to_table']}")
        
        filtered_tables = {k: v for k, v in tables.items() if k in table_names}
    else:
        filtered_relationships = relationships
        filtered_tables = tables
    
    print(f"\nGenerating Mermaid Flowchart (Top-Down)...")
    print(f"   - {len(filtered_tables)} tables")
    print(f"   - {len(filtered_relationships)} relationships")
    
    # Build hierarchy - identify parent tables and their children
    parent_to_children = defaultdict(list)
    all_children = set()
    parent_tables = set()
    
    for rel in filtered_relationships:
        parent_to_children[rel['to_table']].append({
            'table': rel['from_table'],
            'column': rel['from_column'],
            'cascade': rel['delete_rule'] == 'CASCADE'
        })
        parent_tables.add(rel['to_table'])
        all_children.add(rel['from_table'])
    
    # Root parents are those that are parents but never children
    root_parents = parent_tables - all_children
    
    mermaid = ["flowchart TD"]
    mermaid.append("")
    
    # Define all table nodes
    for table_full_name, table_info in sorted(filtered_tables.items()):
        schema, table = table_full_name.split('.')
        
        if table_info['primary_keys']:
            pk_list = ', '.join(table_info['primary_keys'][:2])  # Limit to 2 PKs for readability
            if len(table_info['primary_keys']) > 2:
                pk_list += '...'
            mermaid.append(f"    {table}[\"{table}<br/><small>PK: {pk_list}</small>\"]")
        else:
            mermaid.append(f"    {table}[\"{table}\"]")
    
    mermaid.append("")
    mermaid.append("    %% Styling")
    mermaid.append("    classDef parentTable fill:#4CAF50,stroke:#2E7D32,color:#fff,stroke-width:3px")
    mermaid.append("    classDef childTable fill:#2196F3,stroke:#1565C0,color:#fff")
    mermaid.append("    classDef mixedTable fill:#FF9800,stroke:#E65100,color:#fff")
    mermaid.append("")
    
    # Group relationships by parent for better vertical layout
    mermaid.append("    %% Relationships grouped by parent table")
    for parent in sorted(parent_to_children.keys()):
        children = parent_to_children[parent]
        mermaid.append(f"    %% {parent} children")
        for child_info in children:
            child = child_info['table']
            col = child_info['column']
            if child_info['cascade']:
                mermaid.append(f"    {parent} -->|{col}| {child}")
            else:
                mermaid.append(f"    {parent} -.->|{col}| {child}")
    
    # Apply styling
    mermaid.append("")
    mermaid.append("    %% Apply styles")
    for table in root_parents:
        mermaid.append(f"    class {table} parentTable")
    
    for table in all_children:
        if table in parent_tables:  # This table is both parent and child
            mermaid.append(f"    class {table} mixedTable")
        else:
            mermaid.append(f"    class {table} childTable")
    
    return '\n'.join(mermaid)

def main():
    """Main execution"""
    print("=" * 60)
    print("  ERD Generator - Foreign Key Relationship Visualizer")
    print("=" * 60)
    
    tables, relationships = parse_constraints()
    
    # Get unique schemas
    schemas = set()
    for rel in relationships:
        schemas.add(rel['from_schema'])
        schemas.add(rel['to_schema'])
    
    print(f"\nSchemas found: {', '.join(sorted(schemas))}")
    
    # Generate full ERD
    print("\n" + "=" * 60)
    print("Full ERD (All Schemas)")
    print("=" * 60)
    mermaid_full = generate_mermaid_erd(tables, relationships)
    
    with open('erd_full.mmd', 'w', encoding='utf-8') as f:
        f.write(mermaid_full)
    print(f"\n[OK] Saved to: erd_full.mmd")
    
    # Generate full flowchart (vertical)
    print("\n" + "=" * 60)
    print("Full Flowchart - Vertical Layout (All Schemas)")
    print("=" * 60)
    flowchart_full = generate_mermaid_flowchart(tables, relationships)
    
    with open('erd_full_vertical.mmd', 'w', encoding='utf-8') as f:
        f.write(flowchart_full)
    print(f"\n[OK] Saved to: erd_full_vertical.mmd")
    
    # Generate schema-specific ERDs and flowcharts
    for schema in sorted(schemas):
        if schema in ['dbo', 'mx', 'inv']:  # Focus on main schemas
            print("\n" + "=" * 60)
            print(f"{schema.upper()} Schema ERD (Horizontal)")
            print("=" * 60)
            mermaid_schema = generate_mermaid_erd(tables, relationships, schema)
            
            filename = f'erd_{schema}.mmd'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(mermaid_schema)
            print(f"\n[OK] Saved to: {filename}")
            
            # Also generate vertical version
            print(f"\n{schema.upper()} Schema Flowchart (Vertical)")
            flowchart_schema = generate_mermaid_flowchart(tables, relationships, schema)
            
            filename_vertical = f'erd_{schema}_vertical.mmd'
            with open(filename_vertical, 'w', encoding='utf-8') as f:
                f.write(flowchart_schema)
            print(f"[OK] Saved to: {filename_vertical}")
    
    print("\n" + "=" * 60)
    print("ERD Generation Complete!")
    print("=" * 60)
    print("\nHow to view:")
    print("  1. Open .mmd files in VS Code with Mermaid extension")
    print("  2. Paste into https://mermaid.live")
    print("  3. Use in Markdown with ```mermaid code blocks")
    print("  4. GitHub will render .mmd files automatically")
    print("\nFiles generated:")
    print("  - erd_*.mmd = Horizontal ERD layout (traditional)")
    print("  - erd_*_vertical.mmd = Vertical flowchart layout (top-down)")

if __name__ == '__main__':
    main()

