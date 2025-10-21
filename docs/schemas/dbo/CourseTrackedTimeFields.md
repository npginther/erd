# CourseTrackedTimeFields

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `FieldId` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Minimum` | `decimal(9,2)` | YES | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_CourseTrackedTimeFields`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`nci_wi_CourseTrackedTimeFields_0A9703808436EA29034A0DE90E5C94B2`** (NONCLUSTERED)
  - Columns: `CourseId INCLUDE (FieldId, Minimum)`
- **`nci_wi_CourseTrackedTimeFields_CD2F83D3A36A0E0DDF17D9194C758DF5`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId, Minimum INCLUDE (FieldId, IsLocked)`
