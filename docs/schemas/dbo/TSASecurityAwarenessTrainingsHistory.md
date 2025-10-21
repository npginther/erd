# TSASecurityAwarenessTrainingsHistory

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (13)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `PerformedBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PerformedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `Mode` | `char(6)` | **NO** | `-` | - | - |
| `TSASecurityAwarenessTrainingId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | YES | `-` | - | - |
| `TrainingType` | `int(10,0)` | YES | `-` | - | - |
| `DateCompleted` | `datetime(3)` | YES | `-` | - | - |
| `AlternativeTraining` | `bit` | YES | `-` | - | - |
| `EmployeeId` | `nvarchar(50)` | YES | `-` | - | - |
| `TrainersName` | `nvarchar(150)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_TSASecurityAwarenessTrainingHistory`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
