# CourseTimeFields

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
| `Enabled` | `bit` | **NO** | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_CourseTimeFields`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`ix_CourseTimeFields_CourseId_OperatorId`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId INCLUDE (FieldId, Enabled)`
- **`nci_wi_CourseTimeFields_2C18CC036ABA746ED7CE949BB5646133`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId, Enabled INCLUDE (FieldId, IsLocked)`
- **`nci_wi_CourseTimeFields_D6EE5371131DB673C3CECD832608C14E`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId, FieldId, Enabled INCLUDE (IsLocked)`
