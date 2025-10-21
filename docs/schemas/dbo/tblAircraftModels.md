# tblAircraftModels

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AircraftModelId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `AircraftModel` | `varchar(150)` | **NO** | `-` | - | - |
| `IsDeleted` | `bit` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_tblAircraftModels_CompanyId_AircraftModelIdAircraftModel`** (NONCLUSTERED)
  - Columns: `CompanyId INCLUDE (AircraftModel, AircraftModelId)`
- **`PK_tblAircraftModels`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AircraftModelId`
