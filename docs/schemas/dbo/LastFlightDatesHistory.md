# LastFlightDatesHistory

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (13)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Method` | `nvarchar(50)` | **NO** | `-` | - | - |
| `FlightRecordId` | `uniqueidentifier` | YES | `-` | - | - |
| `FlightNumber` | `bigint(19,0)` | YES | `-` | - | - |
| `MakeId` | `uniqueidentifier` | YES | `-` | - | - |
| `ModelId` | `uniqueidentifier` | YES | `-` | - | - |
| `AnyAircraftChanges` | `nvarchar(2000)` | YES | `-` | - | - |
| `MakeModelChanges` | `nvarchar(2000)` | YES | `-` | - | - |
| `CreatedBy` | `uniqueidentifier` | YES | `-` | - | - |
| `CreatedAtUtc` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_LastFlightDatesHistory_OperatorIdUserId`** (NONCLUSTERED)
  - Columns: `OperatorId, UserId`
- **`PK_LastFlightDatesHistory`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
