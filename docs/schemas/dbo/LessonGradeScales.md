# LessonGradeScales

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `LessonGradeScaleId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `IsDefault` | `bit` | **NO** | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_LessonGradeScales`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_LessonGradeScales_CourseId_Name`** (UNIQUE NONCLUSTERED)
  - Columns: `CourseId, Name`
- **`UK_LessonGradeScales_LessonGradeScaleId`** (UNIQUE NONCLUSTERED)
  - Columns: `LessonGradeScaleId`
