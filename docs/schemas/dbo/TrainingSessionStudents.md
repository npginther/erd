# TrainingSessionStudents

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `TrainingSessionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | **NO** | `-` | - | - |

## Indexes

- **`IX_TrainingSessionStudents_OperatorIdTrainingSessionId`** (NONCLUSTERED)
  - Columns: `OperatorId, TrainingSessionId`
- **`PK_TrainingSessionStudents`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
