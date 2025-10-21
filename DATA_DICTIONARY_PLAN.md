# Data Dictionary Project Roadmap

## Vision
Transform raw database schema exports into a comprehensive, searchable data dictionary that documents:
- All tables and columns with descriptions
- Relationships and dependencies
- Data types and constraints
- Business rules and indexes
- Usage statistics and metadata

---

## Phase 1: Data Collection ✅ (Partially Complete)

### Already Have:
- ✅ `constraint_column_usage.csv`
- ✅ `constraint_table_usage.csv`
- ✅ `table_constraints.csv`
- ✅ `referential_constraints.csv`
- ✅ ERD generation script

### Need to Export (see `export_queries.sql`):
1. **COLUMNS.csv** ⭐ PRIORITY - Core of data dictionary
2. **TABLES.csv** - Table metadata
3. **KEY_COLUMN_USAGE.csv** - Key details
4. **CHECK_CONSTRAINTS.csv** - Business rules
5. **VIEWS.csv** - View definitions
6. **ROUTINES.csv** - Stored procedures/functions
7. **PARAMETERS.csv** - Procedure parameters
8. **INDEXES.csv** - Performance indexes
9. **TABLE_SIZES.csv** - Storage metrics
10. **EXTENDED_PROPERTIES.csv** - Existing documentation (MS_Description)

---

## Phase 2: Data Dictionary Generator

### Features to Build:

#### 2.1 Table Documentation
```
For each table, generate:
- Table name and schema
- Description (from extended properties or manual input)
- Row count and size
- All columns with:
  * Data type and length
  * Nullable/Required
  * Default values
  * Primary/Foreign key status
  * Description
```

#### 2.2 Column Details
```
- Full data type specification
- Constraints (PK, FK, UK, CHECK)
- Which tables reference this column (FK dependencies)
- Indexes that include this column
- Statistics (if available)
```

#### 2.3 Relationship Visualization
```
- ERD diagrams (already have!)
- Lineage: "What depends on this table?"
- Impact analysis: "If I change this, what breaks?"
```

#### 2.4 Search & Discovery
```
- Search by table name
- Search by column name
- Find all tables with a specific column (e.g., "UserId")
- Find tables by schema
```

---

## Phase 3: Output Formats

### 3.1 Static HTML Site
- Single-page app with search
- Table of contents with jump links
- Responsive design
- Exportable to PDF

### 3.2 Markdown Documentation
- One file per table
- Index page with TOC
- GitHub-friendly
- Version controllable

### 3.3 Excel Workbook
- Sheet per table
- Master index sheet
- Pivot-ready format
- Shareable with non-technical users

### 3.4 Interactive Database
- SQLite database of metadata
- Query your schema!
- Build custom reports

---

## Phase 4: Enhanced Features

### 4.1 Documentation Import
```python
# Allow CSV/Excel upload with descriptions
- TableName, Description
- TableName, ColumnName, Description
- Import MS_Description from EXTENDED_PROPERTIES
```

### 4.2 Data Lineage
```
- Trace data flow through views
- Show stored procedure dependencies
- Impact analysis for schema changes
```

### 4.3 Data Quality Metrics
```
- NULL percentage by column
- Unique value counts
- Data type mismatches (e.g., varchar for IDs)
- Orphaned foreign keys
```

### 4.4 Change Tracking
```
- Git-based version control
- Schema change history
- Documentation change log
- Diff between versions
```

---

## Technology Stack Options

### Python Script (Recommended to start)
```python
# Pros:
- Builds on existing generate_erd.py
- Easy to extend
- Great libraries (pandas, jinja2, markdown)
- Can generate multiple formats

# Libraries:
- pandas: CSV processing
- jinja2: HTML templating
- markdown: MD generation
- openpyxl: Excel export
- sqlite3: Database creation
```

### Web Application (Phase 4+)
```
- React/Vue frontend for search/browse
- FastAPI/Flask backend
- PostgreSQL for metadata storage
- Elasticsearch for full-text search
```

---

## Quick Start - Next Steps

### 1. Export COLUMNS.csv (Critical!)
```sql
-- Run this first:
SELECT * FROM INFORMATION_SCHEMA.COLUMNS
ORDER BY TABLE_SCHEMA, TABLE_NAME, ORDINAL_POSITION;
```

### 2. Create Initial Data Dictionary Script
```python
generate_data_dictionary.py
- Read COLUMNS.csv
- Read existing constraint CSVs
- Generate Markdown file per table
- Create index.md with TOC
```

### 3. Template Structure
```
docs/
  ├── index.md                    # Main index
  ├── schemas/
  │   ├── dbo/
  │   │   ├── tblUsers.md        # One file per table
  │   │   ├── tblReservation.md
  │   │   └── ...
  │   ├── inv/
  │   └── mx/
  └── erd/
      ├── erd_full.mmd
      └── erd_dbo.mmd
```

---

## Example Output - Table Documentation

### tblReservation.md
```markdown
# tblReservation

**Schema:** dbo  
**Type:** BASE TABLE  
**Row Count:** ~125,000  
**Size:** 45 MB

## Description
Stores flight reservation records including scheduling, aircraft, 
and instructor assignments.

## Columns

| Column | Type | Nullable | Default | Key | Description |
|--------|------|----------|---------|-----|-------------|
| ReservationId | int | NOT NULL | - | PK | Unique identifier |
| StartDateTime | datetime | NOT NULL | - | - | Reservation start |
| EndDateTime | datetime | NOT NULL | - | - | Reservation end |
| AircraftId | int | NULL | - | FK→tblAircraft | Assigned aircraft |
| Status | varchar(50) | NOT NULL | 'Pending' | - | Current status |

## Relationships

### Parent Tables (References)
- **tblAircraft** via AircraftId
- **tblReservationTypes** via ReservationTypeId

### Child Tables (Referenced By)
- **tblReservationPilots** - Multiple pilots per reservation
- **tblReservationFlightDetails** - Flight details
- **tblReservationResources** - Additional resources
- **FlightAlerts** - Alert notifications

## Indexes
- `PK_tblReservation` (Clustered) on ReservationId
- `IX_tblReservation_StartDateTime` on StartDateTime
- `IX_tblReservation_AircraftId` on AircraftId

## Constraints
- FK_tblReservation_tblAircraft (NO ACTION)
- CK_ReservationDateTime (CHECK: EndDateTime > StartDateTime)
```

---

## Want to Start?

Run the queries in `export_queries.sql` and export results as CSVs. Then I can build the data dictionary generator!

**Priority exports to start:**
1. COLUMNS.csv - Essential
2. INDEXES.csv - Helpful for understanding performance
3. EXTENDED_PROPERTIES.csv - Capture any existing documentation
4. TABLE_SIZES.csv - Good for context

Let me know when you have these files and I'll build the generator! 🚀

