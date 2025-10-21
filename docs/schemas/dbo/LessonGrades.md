# LessonGrades

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
| `LessonGradeScaleId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonGradeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Name` | `nvarchar(50)` | **NO** | `-` | - | - |
| `ShortLabel` | `nvarchar(5)` | YES | `-` | - | - |
| `Definition` | `nvarchar(250)` | YES | `-` | - | - |
| `DefaultLowestPassingGrade` | `bit` | **NO** | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_LessonGrades`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_LessonGrades_LessonGradeId`** (UNIQUE NONCLUSTERED)
  - Columns: `LessonGradeId`
- **`nci_wi_LessonGrades_130DCE20FE639D9CEE706D26BFF1C68F`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId, LessonGradeScaleId, DefaultLowestPassingGrade`
- **`nci_wi_LessonGrades_A34ED4A0CA08290CD1FF7B03411DC997`** (NONCLUSTERED)
  - Columns: `DefaultLowestPassingGrade, CourseId INCLUDE (Order)`
