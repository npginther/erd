# StudentLessonCustomTaskGrades

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
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CustomLessonTaskId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TaskGradeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TaskStatus` | `int(10,0)` | **NO** | `-` | - | - |
| `InstructorId` | `uniqueidentifier` | YES | `-` | - | - |
| `SessionDate` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_StudentLessonCustomTaskGrades`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_StudentLessonCustomTaskGrades_EnrollmentIdLessonIdCustomLessonTaskId`** (UNIQUE NONCLUSTERED)
  - Columns: `EnrollmentId, LessonId, CustomLessonTaskId`
- **`nci_wi_StudentLessonCustomTaskGrades_21DBB4EE872D315B722ECD0CD91582D8`** (NONCLUSTERED)
  - Columns: `CustomLessonTaskId, OperatorId INCLUDE (TaskGradeId, TaskStatus)`
