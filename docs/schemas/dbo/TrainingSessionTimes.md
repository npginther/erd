# TrainingSessionTimes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | YES | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | YES | `-` | - | - |
| `TrainingSessionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `FieldId` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Value` | `decimal(9,2)` | YES | `-` | - | - |
| `IsDraft` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_TrainingSessionTimes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_TrainingSessionTimes_TrainingSessionIdFieldId`** (UNIQUE NONCLUSTERED)
  - Columns: `TrainingSessionId, FieldId`
- **`ix_TrainingSessionTimes_OperatorId_CourseId_EnrollmentId`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId, EnrollmentId INCLUDE (TrainingSessionId, FieldId, Value)`
- **`nci_wi_TrainingSessionTimes_321D4F3EC7E957EC42BF6BC0618084CA`** (NONCLUSTERED)
  - Columns: `OperatorId, EnrollmentId, IsDraft INCLUDE (FieldId, TrainingSessionId, Value)`
- **`nci_wi_TrainingSessionTimes_35C9358E0FA917781608CA1038C23443`** (NONCLUSTERED)
  - Columns: `OperatorId, TrainingSessionId INCLUDE (CourseId, EnrollmentId, FieldId, IsDraft, LessonId, StudentId, Value)`
- **`nci_wi_TrainingSessionTimes_36553F02B09EC8D5691A3BA49749EC96`** (NONCLUSTERED)
  - Columns: `CourseId, EnrollmentId, OperatorId, IsDraft, LessonId INCLUDE (FieldId, TrainingSessionId, Value)`
- **`nci_wi_TrainingSessionTimes_86A05E81946FFBB72459D76498270CD4`** (NONCLUSTERED)
  - Columns: `CourseId, EnrollmentId, OperatorId INCLUDE (FieldId, TrainingSessionId, Value)`
