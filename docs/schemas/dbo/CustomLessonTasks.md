# CustomLessonTasks

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (15)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseTaskId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CustomLessonTaskId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Importance` | `int(10,0)` | **NO** | `-` | - | - |
| `TaskGradeScaleId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LowestPassingGradeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `DisplayLowestPassingGrade` | `bit` | **NO** | `-` | - | - |
| `CompletionStandard` | `nvarchar(MAX)` | YES | `-` | - | - |
| `AddedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `AddedBy` | `uniqueidentifier` | **NO** | `-` | - | - |

## Indexes

- **`PK_CustomLessonTasks`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_CustomLessonTasks_CustomLessonTaskId`** (UNIQUE NONCLUSTERED)
  - Columns: `CustomLessonTaskId`
- **`nci_wi_CustomLessonTasks_4C69E3272F535CB4E43D7FD3762BA9A9`** (NONCLUSTERED)
  - Columns: `OperatorId, EnrollmentId, LessonId, CourseId, Importance, AddedAt`
