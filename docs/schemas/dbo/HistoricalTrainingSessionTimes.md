# HistoricalTrainingSessionTimes

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
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | YES | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | YES | `-` | - | - |
| `TrainingSessionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `HistoricalTrainingSessionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `FieldId` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Value` | `decimal(9,2)` | YES | `-` | - | - |
| `IsDraft` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_HistoricalTrainingSessionTimes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_HistoricalTrainingSessionTimes_HistoricalTrainingSessionIdFieldId`** (UNIQUE NONCLUSTERED)
  - Columns: `HistoricalTrainingSessionId, FieldId`
- **`nci_wi_HistoricalTrainingSessionTimes_B1E38BF7C36A4C2CA97ADECFF1E02B22`** (NONCLUSTERED)
  - Columns: `OperatorId, TrainingSessionId`
