# StudentLessons

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
| `StudentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonGradeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonStatus` | `int(10,0)` | **NO** | `-` | - | - |
| `InstructorId` | `uniqueidentifier` | YES | `-` | - | - |
| `SessionDate` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_StudentLessons`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_StudentLessons_LessonIdEnrollmentId`** (UNIQUE NONCLUSTERED)
  - Columns: `LessonId, EnrollmentId`
- **`ix_StudentLessons_OperatorId_CourseId_StudentId_LessonsStatus`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId, StudentId, LessonStatus`
- **`nci_wi_StudentLessons_B4CA8E7CFF95DDBBA8E9A839542B11C8`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId, EnrollmentId, LessonStatus INCLUDE (LessonId, SessionDate, StudentId)`
