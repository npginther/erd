# MeterRecordSegments

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
| `FlightRecordId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `MeterRecordId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `SegmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Minutes` | `int(10,0)` | YES | `-` | - | - |
| `StartTime` | `datetime(3)` | YES | `-` | - | - |
| `EndTime` | `datetime(3)` | YES | `-` | - | - |
| `SegmentOrder` | `int(10,0)` | **NO** | `-` | - | - |
| `ReservationId` | `uniqueidentifier` | YES | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | - | - |

## Indexes

- **`PK__MeterRec__94D7B0A4B23CE40E`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
