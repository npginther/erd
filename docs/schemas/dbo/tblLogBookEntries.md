# tblLogBookEntries

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (26)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `LogbookEntryId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `PilotId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `DateEntryWasMade` | `datetime(3)` | **NO** | `-` | - | - |
| `DateFlightOccured` | `datetime(3)` | YES | `-` | - | - |
| `AutoEntry` | `bit` | **NO** | `-` | - | - |
| `FlightRecordId` | `uniqueidentifier` | YES | `-` | - | - |
| `IsAdjustingEntry` | `bit` | **NO** | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | YES | `-` | - | - |
| `ACMakeId` | `uniqueidentifier` | YES | `-` | - | - |
| `ACModelId` | `uniqueidentifier` | YES | `-` | - | - |
| `ACIdent` | `varchar(50)` | YES | `-` | - | - |
| `TotalHours` | `decimal(17,1)` | **NO** | `-` | - | - |
| `CCHours` | `decimal(17,1)` | **NO** | `-` | - | - |
| `NightHours` | `decimal(17,1)` | **NO** | `-` | - | - |
| `DayHours` | `decimal(17,1)` | **NO** | `-` | - | - |
| `ActualIMC` | `decimal(17,1)` | **NO** | `-` | - | - |
| `HoodedHours` | `decimal(17,1)` | **NO** | `-` | - | - |
| `DayLandings` | `int(10,0)` | **NO** | `-` | - | - |
| `NightLandings` | `int(10,0)` | **NO** | `-` | - | - |
| `DepartureAirport` | `varchar(50)` | **NO** | `-` | - | - |
| `ArrivalAirport` | `varchar(50)` | **NO** | `-` | - | - |
| `Approaches` | `int(10,0)` | **NO** | `-` | - | - |
| `OrderId` | `int(10,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_tblLogBookEntries_CompanyId_FlightRecordId`** (NONCLUSTERED)
  - Columns: `CompanyId, FlightRecordId`
- **`IDX_tblLogBookEntries_FlightRecordId`** (NONCLUSTERED)
  - Columns: `FlightRecordId`
- **`PK_tblFlightRecords`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `LogbookEntryId`
