# StudentLessonsPreviousCredits

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CreatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `CreatedBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TrainingSessionId` | `uniqueidentifier` | **NO** | `-` | - | - |

## Indexes

- **`PK_StudentLessonsPreviousCredit`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`nci_wi_StudentLessonsPreviousCredits_0965FBB2B33F474C16096223F8D7F42B`** (NONCLUSTERED)
  - Columns: `EnrollmentId, LessonId, CourseId, OperatorId, StudentId`
- **`nci_wi_StudentLessonsPreviousCredits_B1E38BF7C36A4C2CA97ADECFF1E02B22`** (NONCLUSTERED)
  - Columns: `OperatorId, TrainingSessionId`
