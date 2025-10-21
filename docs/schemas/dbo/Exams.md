# Exams

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ExamId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Description` | `nvarchar(250)` | YES | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `IncludedInTrainingRecord` | `bit` | **NO** | `-` | - | - |
| `FileUploadEnabled` | `bit` | **NO** | `-` | - | - |
| `FileUploadRequirement` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_Exams`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_Exams_ExamId`** (UNIQUE NONCLUSTERED)
  - Columns: `ExamId`
