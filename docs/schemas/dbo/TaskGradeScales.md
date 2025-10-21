# TaskGradeScales

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (8)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `TaskGradeScaleId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `IsDefault` | `bit` | **NO** | `-` | - | - |
| `DefaultShowPassingGrade` | `bit` | **NO** | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_TaskGradeScales`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_TaskGradeScales_CourseId_Name`** (UNIQUE NONCLUSTERED)
  - Columns: `CourseId, Name`
- **`UK_TaskGradeScales_TaskGradeScaleId`** (UNIQUE NONCLUSTERED)
  - Columns: `TaskGradeScaleId`
