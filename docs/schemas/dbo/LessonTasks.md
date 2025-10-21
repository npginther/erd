# LessonTasks

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (20)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PartId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `HeadingId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseTaskId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonTaskId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Importance` | `int(10,0)` | **NO** | `-` | - | - |
| `TaskGradeScaleId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LowestPassingGradeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `DisplayLowestPassingGrade` | `bit` | **NO** | `-` | - | - |
| `CompletionStandard` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |
| `ObjectivesHtml` | `nvarchar(MAX)` | YES | `-` | - | - |
| `CompletionStandardHtml` | `nvarchar(MAX)` | YES | `-` | - | - |
| `RequiredStudyHtml` | `nvarchar(MAX)` | YES | `-` | - | - |
| `RecommendedStudyHtml` | `nvarchar(MAX)` | YES | `-` | - | - |
| `NoteForInstructorHtml` | `nvarchar(MAX)` | YES | `-` | - | - |

## Indexes

- **`IDX_LessonTasks_CourseTaskId`** (NONCLUSTERED)
  - Columns: `CourseTaskId`
- **`IDX_LessonTasks_HeadingId_CourseId_OperatorId_LessonId_CourseTaskId`** (NONCLUSTERED)
  - Columns: `HeadingId, CourseId, OperatorId, LessonId, CourseTaskId INCLUDE (Importance, LessonTaskId, LowestPassingGradeId, Order, TaskGradeScaleId)`
- **`IDX_LessonTasks_LessonId`** (NONCLUSTERED)
  - Columns: `LessonId`
- **`Idx_LessonTasks_OperatorIdCourseIdLessonId`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId, LessonId`
- **`PK_LessonTasks`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_LessonTasks_LessonTaskId`** (UNIQUE NONCLUSTERED)
  - Columns: `LessonTaskId`
- **`nci_wi_LessonTasks_C6CDCE128D520B5F5AA9490133CE2923`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId, HeadingId INCLUDE (CompletionStandard, CourseTaskId, DisplayLowestPassingGrade, Importance, IsLocked, LessonId, LessonTaskId, LowestPassingGradeId, Order, TaskGradeScaleId)`
