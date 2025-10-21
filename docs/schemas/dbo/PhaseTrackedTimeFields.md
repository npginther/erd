# PhaseTrackedTimeFields

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (8)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StageId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PhaseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `FieldId` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Minimum` | `decimal(9,2)` | YES | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_PhaseTrackedTimeFields`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`nci_wi_PhaseTrackedTimeFields_8D499FE92D0DD8A350AE4B1C9C5264F9`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId, FieldId, PhaseId INCLUDE (IsLocked, Minimum)`
