# TSASecurityAwarenessTrainings

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `TSASecurityAwarenessTrainingId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TrainingType` | `int(10,0)` | **NO** | `-` | - | - |
| `DateCompleted` | `datetime(3)` | **NO** | `-` | - | - |
| `AlternativeTraining` | `bit` | **NO** | `-` | - | - |
| `EmployeeId` | `nvarchar(50)` | **NO** | `-` | - | - |
| `TrainersName` | `nvarchar(150)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_TSASecurityAwarenessTraining`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_TSASecurityAwarenessTraining_TSASecurityAwarenessTrainingId`** (UNIQUE NONCLUSTERED)
  - Columns: `TSASecurityAwarenessTrainingId`
