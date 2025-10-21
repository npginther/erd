# tblAircraftMakes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AircraftMakeId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `AircraftMake` | `varchar(150)` | **NO** | `-` | - | - |
| `IsDeleted` | `bit` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_tblAircraftMakes_CompanyId`** (NONCLUSTERED)
  - Columns: `CompanyId`
- **`PK_tblAircraftMakes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AircraftMakeId`
