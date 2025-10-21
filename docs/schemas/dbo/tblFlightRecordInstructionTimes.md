# tblFlightRecordInstructionTimes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `FlightRecordId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `InstructionTypeId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | PK | - |
| `Value` | `decimal(5,2)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblFlightRecordInstructionTimes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `FlightRecordId, InstructionTypeId, OperatorId`
