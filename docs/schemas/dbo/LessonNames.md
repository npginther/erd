# LessonNames

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Name` | `nvarchar(150)` | **NO** | `-` | - | - |
| `TimeStamp` | `datetime(3)` | YES | `-` | - | - |
| `IsStageCheck` | `bit` | **NO** | `-` | - | - |
| `StageCheckName` | `nvarchar(300)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_LessonNames`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`UK_LessonNames_OperatorId_CourseId_LessonId`** (UNIQUE NONCLUSTERED)
  - Columns: `OperatorId, CourseId, LessonId`
- **`dbo.IDX_LessonNames_LessonId_NameIsStageCheckStageCheckName`** (NONCLUSTERED)
  - Columns: `LessonId INCLUDE (IsStageCheck, Name, StageCheckName)`
