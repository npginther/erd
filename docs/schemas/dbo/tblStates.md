# tblStates

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (3)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Abbreviation` | `varchar(10)` | **NO** | `-` | PK | - |
| `Description` | `varchar(75)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblStates`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Abbreviation`
