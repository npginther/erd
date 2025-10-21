# Stages

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `StageId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `Objectives` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `Visible` | `bit` | **NO** | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |
| `ExternalId` | `nvarchar(50)` | YES | `-` | - | - |

## Indexes

- **`PK_Stages`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_Stages_StageId`** (UNIQUE NONCLUSTERED)
  - Columns: `StageId`
- **`nci_wi_Stages_C68E9FC2C0420442E120FBD6DFCDF3D4`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId INCLUDE (IsLocked, Name, Order, StageId)`
