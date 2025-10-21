# LastFlightDatesByMakeModel

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (8)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `MakeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ModelId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LastFlightDate` | `datetime(3)` | YES | `-` | - | - |
| `LastFlightDateWithInstruction` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_LastFlightDateByMakeModel`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`ix_OperatorId_UserID_MakeId_ModelID`** (NONCLUSTERED)
  - Columns: `OperatorId, UserId, MakeId, ModelId`
