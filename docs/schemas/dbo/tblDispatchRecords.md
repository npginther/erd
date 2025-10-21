# tblDispatchRecords

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (33)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `DispatchNumber` | `bigint(19,0)` | **NO** | `-` | - | - |
| `DispatcherUserid` | `int(10,0)` | **NO** | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Instructor` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Hobbsout` | `decimal(9,2)` | **NO** | `-` | - | - |
| `TachOut` | `decimal(9,2)` | **NO** | `-` | - | - |
| `DepartDate` | `datetime(3)` | **NO** | `-` | - | - |
| `ExpectedFlightHours` | `decimal(9,2)` | **NO** | `-` | - | - |
| `IsCrossCountry` | `bit` | **NO** | `-` | - | - |
| `IsPending` | `bit` | **NO** | `-` | - | - |
| `HobbsIn` | `decimal(9,2)` | **NO** | `-` | - | - |
| `TachIn` | `decimal(9,2)` | **NO** | `-` | - | - |
| `ReturnDate` | `datetime(3)` | **NO** | `-` | - | - |
| `FlightInstruction` | `decimal(9,2)` | **NO** | `-` | - | - |
| `PreFlightInstructions` | `decimal(9,2)` | **NO** | `-` | - | - |
| `PostFlightInstructions` | `decimal(9,2)` | **NO** | `-` | - | - |
| `OffSiteFuelCreditAmt` | `decimal(9,2)` | **NO** | `-` | - | - |
| `FlightDidNotOccur` | `bit` | **NO** | `-` | - | - |
| `FlightDidNotOccurReason` | `varchar(500)` | **NO** | `-` | - | - |
| `IsCheckedIn` | `bit` | **NO** | `-` | - | - |
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Comments` | `varchar(500)` | **NO** | `-` | - | - |
| `InternalComments` | `varchar(500)` | **NO** | `-` | - | - |
| `IsVFR` | `bit` | **NO** | `-` | - | - |
| `FlightRoute` | `varchar(500)` | **NO** | `-` | - | - |
| `LocationId` | `int(10,0)` | **NO** | `-` | - | - |
| `Created` | `datetime(3)` | YES | `-` | - | - |
| `CheckInUserId` | `int(10,0)` | **NO** | `-` | - | - |
| `DispatchObjectId` | `int(10,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.tblDispatchPilots`** 
  via `DispatchId` → `Id`
- **`dbo.tblDispatchResources`** 
  via `DispatchId` → `Id`

## Indexes

- **`IX_tblDispatchRecordsClustered`** (CLUSTERED)
  - Columns: `DispatchNumber`
- **`IX_tblDispatchRecordsFields`** (NONCLUSTERED)
  - Columns: `DepartDate, ReturnDate`
- **`PK_tblDispatchRecords`** (PRIMARY KEY UNIQUE NONCLUSTERED)
  - Columns: `Id`
