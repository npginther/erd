# StudentLessonTaskGrades

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
| `LessonTaskId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TaskGradeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TaskStatus` | `int(10,0)` | **NO** | `-` | - | - |
| `InstructorId` | `uniqueidentifier` | YES | `-` | - | - |
| `SessionDate` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_StudentLessonTaskGrades`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_StudentLessonTaskGrades_EnrollmentIdLessonIdLessonTaskId`** (UNIQUE NONCLUSTERED)
  - Columns: `EnrollmentId, LessonId, LessonTaskId`
- **`ix_StudentLessonTaskGrades_OperatorId_CourseId_LessonId_StudentId_EnrollmentId`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId, LessonId, StudentId, EnrollmentId INCLUDE (LessonTaskId, TaskGradeId, TaskStatus)`
- **`nci_wi_StudentLessonTaskGrades_B5494E4FEF258B22B6816F86F338E0EF`** (NONCLUSTERED)
  - Columns: `OperatorId, EnrollmentId, LessonId, StudentId, CourseId INCLUDE (InstructorId, LessonTaskId, SessionDate, TaskGradeId, TaskStatus)`
