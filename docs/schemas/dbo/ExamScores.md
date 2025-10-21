# ExamScores

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (11)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ExamScoreId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ExamId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ScoredAt` | `datetime(3)` | **NO** | `-` | - | - |
| `Score` | `nvarchar(10)` | **NO** | `-` | - | - |
| `Status` | `int(10,0)` | **NO** | `-` | - | - |
| `InstructorId` | `uniqueidentifier` | **NO** | `-` | - | - |

## Indexes

- **`PK_ExamScores`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_ExamScores_ExamScoreId`** (UNIQUE NONCLUSTERED)
  - Columns: `ExamScoreId`
