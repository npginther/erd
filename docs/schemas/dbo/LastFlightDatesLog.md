# LastFlightDatesLog

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (12)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `MakeId` | `uniqueidentifier` | YES | `-` | - | - |
| `ModelId` | `uniqueidentifier` | YES | `-` | - | - |
| `FlightDate` | `datetime(3)` | **NO** | `-` | - | - |
| `HasInstruction` | `bit` | **NO** | `-` | - | - |
| `CreatedBy` | `uniqueidentifier` | YES | `-` | - | - |
| `FlightRecordId` | `uniqueidentifier` | YES | `-` | - | - |
| `ManualUpdate` | `bit` | **NO** | `-` | - | - |
| `CreatedAtUtc` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_LastFlightDateLog`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`ix_OperatorId_UserId_FlightRecordId`** (NONCLUSTERED)
  - Columns: `OperatorId, UserId, FlightRecordId`
- **`ix_OperatorId_UserId_MakeId_ModelId_HasInstruction_Includes`** (NONCLUSTERED)
  - Columns: `OperatorId, UserId, MakeId, ModelId, HasInstruction INCLUDE (FlightDate, FlightRecordId)`
