# TrainingSessionTaskGrades

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (11)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | YES | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | YES | `-` | - | - |
| `TrainingSessionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TaskId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TaskGradeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TaskStatus` | `int(10,0)` | **NO** | `-` | - | - |
| `Notes` | `nvarchar(MAX)` | YES | `-` | - | - |

## Indexes

- **`IDX_TrainingSessionTaskGrades_OperatorIdEnrollmentId`** (NONCLUSTERED)
  - Columns: `OperatorId, EnrollmentId`
- **`PK_TrainingSessionTaskGrades`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_TrainingSessionTaskGrades_TrainingSessionIdTaskId`** (UNIQUE NONCLUSTERED)
  - Columns: `TrainingSessionId, TaskId`
- **`ix_TrainingSessionTaskGrades_OperatorId_LessonId_EnrollmentId`** (NONCLUSTERED)
  - Columns: `OperatorId, LessonId, EnrollmentId INCLUDE (TrainingSessionId)`
- **`nci_wi_TrainingSessionTaskGrades_E00656627CAC26D9AF91D09B735AFAC7`** (NONCLUSTERED)
  - Columns: `EnrollmentId, LessonId, OperatorId, CourseId, TrainingSessionId`
- **`nci_wi_TrainingSessionTaskGrades_F66187BBC6F1891C5CF136017EB09735`** (NONCLUSTERED)
  - Columns: `OperatorId, TrainingSessionId, EnrollmentId, CourseId INCLUDE (LessonId, StudentId, TaskGradeId, TaskId, TaskStatus)`
