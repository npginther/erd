# LessonTrackedTimeFields

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StageId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PhaseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `FieldId` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Minimum` | `decimal(9,2)` | YES | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_LessonTrackedTimeFields`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`ix_LessonTrackedTimeFields_LessonId_OperatorId_FieldId`** (NONCLUSTERED)
  - Columns: `LessonId, OperatorId, FieldId`
- **`nci_wi_LessonTrackedTimeFields_79B1BEEF11F63E3A2E5CA4F374AF21D4`** (NONCLUSTERED)
  - Columns: `LessonId, OperatorId, FieldId INCLUDE (IsLocked, Minimum)`
- **`nci_wi_LessonTrackedTimeFields_8CDAAADE5013E8E9AEDEDB7323AB1AB9`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId INCLUDE (FieldId, LessonId, Minimum)`
