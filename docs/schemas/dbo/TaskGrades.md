# TaskGrades

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
| `TaskGradeScaleId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TaskGradeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Name` | `nvarchar(50)` | **NO** | `-` | - | - |
| `ShortLabel` | `nvarchar(5)` | **NO** | `-` | - | - |
| `Definition` | `nvarchar(250)` | YES | `-` | - | - |
| `DefaultLowestPassingGrade` | `bit` | **NO** | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_TaskGrades`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_TaskGrades_TaskGradeId`** (UNIQUE NONCLUSTERED)
  - Columns: `TaskGradeId`
- **`nci_wi_TaskGrades_9C4931EF954E578E4A06506121827A9D`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId, TaskGradeScaleId, DefaultLowestPassingGrade INCLUDE (Name, Order, ShortLabel, TaskGradeId)`
