# Database ERD - Foreign Key Relationships

This directory contains Entity Relationship Diagrams (ERDs) generated from your SQL Server database schema.

## Generated Files

- **`erd_full.mmd`** - Complete ERD with all schemas and relationships
- **`erd_dbo.mmd`** - ERD focused on the `dbo` schema
- **`generate_erd.py`** - Python script to regenerate ERDs from CSV files

## Statistics

- **Tables**: 55 tables with foreign key relationships
- **Relationships**: 39 foreign key relationships documented
- **Schemas**: dbo (main application schema)

## How to View the ERD

### Option 1: Mermaid Live Editor (Easiest)
1. Go to https://mermaid.live
2. Open one of the `.mmd` files
3. Copy the contents
4. Paste into the editor - diagram renders automatically
5. Use zoom/pan controls to explore

### Option 2: VS Code (Best for Development)
1. Install the "Markdown Preview Mermaid Support" extension
2. Create a new Markdown file (e.g., `view_erd.md`)
3. Add this content:
   ````markdown
   # Database ERD
   
   ```mermaid
   [paste contents of erd_dbo.mmd here]
   ```
   ````
4. Click "Open Preview" (Ctrl+Shift+V)

### Option 3: GitHub
- Just push the `.mmd` files to GitHub
- GitHub automatically renders Mermaid diagrams

## Understanding the Diagram

### Relationship Symbols

- `||--o{` = **One-to-many with CASCADE delete** (solid line)
  - Parent deleted → children automatically deleted
  - Example: `tblRole ||--o{ tblUserRoleJoiner`
  
- `||..o{` = **One-to-many with NO ACTION** (dotted line)
  - Parent deleted → must delete children first
  - Example: `tblReservation ||..o{ FlightAlerts`

### Key Relationships Found

Some notable relationships in your schema:

- **Reservations** → Multiple child tables (FlightDetails, Pilots, Resources, Notifications)
- **Users & Roles** → Role-based access control with joiners
- **Labels** → Flexible labeling system for roles and users
- **Addresses** → Shared address tables for companies and people
- **Flight Records** → Connected to resources, meters, and standard flight details

## Regenerating ERDs

If you update your database schema, export new CSV files and run:

```bash
python generate_erd.py
```

### Required CSV Files

The script expects these files (exported from SQL Server):

1. **`constraint_column_usage.csv`** - INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
2. **`constraint_table_usage.csv`** - INFORMATION_SCHEMA.CONSTRAINT_TABLE_USAGE  
3. **`table_constraints.csv`** - INFORMATION_SCHEMA.TABLE_CONSTRAINTS
4. **`referential_constraints.csv`** - INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS

### SQL Export Query

```sql
-- Run these queries in SQL Server and export to CSV:

-- 1. constraint_column_usage.csv
SELECT * FROM INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
ORDER BY TABLE_SCHEMA, TABLE_NAME;

-- 2. constraint_table_usage.csv
SELECT * FROM INFORMATION_SCHEMA.CONSTRAINT_TABLE_USAGE
ORDER BY TABLE_SCHEMA, TABLE_NAME;

-- 3. table_constraints.csv
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
ORDER BY CONSTRAINT_SCHEMA, CONSTRAINT_NAME;

-- 4. referential_constraints.csv
SELECT * FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS
ORDER BY CONSTRAINT_SCHEMA, CONSTRAINT_NAME;
```

## Schema Overview

### `dbo` Schema (Main Application)
The primary application schema containing:
- User management (tblUsers, tblRole, tblPerson)
- Reservations and scheduling
- Flight records and operations
- Addresses and locations
- Labels and tagging system

## Notes

- Only foreign key relationships are shown (not all columns)
- Primary keys are indicated with "PK" in table definitions
- Cross-schema relationships (e.g., dbo → inv, dbo → mx) are included
- Cascade delete relationships shown with solid lines
- NO ACTION relationships shown with dotted lines

## Next Steps

To get a complete ERD with all columns:
1. Export INFORMATION_SCHEMA.COLUMNS table
2. Modify the script to include all columns in table definitions
3. Consider using a dedicated ERD tool like:
   - DbSchema
   - DBeaver
   - SQL Server Management Studio (Database Diagrams)
   - draw.io with database plugins

