# tblAircraftCategoryJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CategoryId` | `int(10,0)` | **NO** | `-` | PK | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_tblAircraftCategoryJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AircraftId, CategoryId`
