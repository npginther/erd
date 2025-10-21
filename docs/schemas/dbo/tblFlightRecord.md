# tblFlightRecord

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (92)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `FlightRecordId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `FlightNumber` | `bigint(19,0)` | **NO** | `-` | - | - |
| `Start` | `datetime(3)` | **NO** | `-` | - | - |
| `End` | `datetime(3)` | **NO** | `-` | - | - |
| `CreatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `CreatedBy` | `int(10,0)` | **NO** | `-` | - | - |
| `CheckedInBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CheckedOutBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `DeletedBy` | `int(10,0)` | **NO** | `-` | - | - |
| `Location` | `int(10,0)` | **NO** | `-` | - | - |
| `ObjectType` | `int(10,0)` | **NO** | `-` | - | - |
| `Status` | `int(10,0)` | **NO** | `-` | - | - |
| `Comments` | `varchar(2000)` | YES | `-` | - | - |
| `InternalComments` | `varchar(500)` | **NO** | `-` | - | - |
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CreatedFor` | `varchar(100)` | YES | `-` | - | - |
| `RecordedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `FlightTypeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ContainsMismatch` | `bit` | YES | `-` | - | - |
| `FuelAdded` | `decimal(9,3)` | YES | `-` | - | - |
| `Engine1OilAdded` | `decimal(9,3)` | YES | `-` | - | - |
| `Engine2OilAdded` | `decimal(9,3)` | YES | `-` | - | - |
| `Engine3OilAdded` | `decimal(9,3)` | YES | `-` | - | - |
| `Engine4OilAdded` | `decimal(9,3)` | YES | `-` | - | - |
| `Engine5OilAdded` | `decimal(9,3)` | YES | `-` | - | - |
| `Engine6OilAdded` | `decimal(9,3)` | YES | `-` | - | - |
| `Engine7OilAdded` | `decimal(9,3)` | YES | `-` | - | - |
| `Engine8OilAdded` | `decimal(9,3)` | YES | `-` | - | - |
| `Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine1Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine2Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine3Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine4Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine5Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine6Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine7Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine8Cycles` | `int(10,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Pilot1UserId` | `uniqueidentifier` | YES | `-` | - | - |
| `Pilot2UserId` | `uniqueidentifier` | YES | `-` | - | - |
| `PeopleGroupForPilot1` | `nvarchar(200)` | YES | `-` | - | - |
| `PeopleGroupOwnerIdForPilot1` | `uniqueidentifier` | YES | `-` | - | - |
| `PeopleGroupOwnerForPilot1` | `nvarchar(150)` | YES | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | YES | `-` | - | - |
| `ReservationNumber` | `bigint(19,0)` | YES | `-` | - | - |
| `TotalTimeMeter` | `nvarchar(25)` | YES | `-` | - | - |
| `BillingMeter` | `nvarchar(25)` | YES | `-` | - | - |
| `HobbsOut` | `decimal(9,2)` | YES | `-` | - | - |
| `HobbsIn` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach1Out` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach1In` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach2Out` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach2In` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach3Out` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach3In` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach4Out` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach4In` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach5Out` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach5In` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach6Out` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach6In` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach7Out` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach7In` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach8Out` | `decimal(9,2)` | YES | `-` | - | - |
| `Tach8In` | `decimal(9,2)` | YES | `-` | - | - |
| `AirTimeOut` | `decimal(9,2)` | YES | `-` | - | - |
| `AirTimeIn` | `decimal(9,2)` | YES | `-` | - | - |
| `HeaterHobbsOut` | `decimal(9,2)` | YES | `-` | - | - |
| `HeaterHobbsIn` | `decimal(9,2)` | YES | `-` | - | - |
| `InstructorUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `InstructorType` | `int(10,0)` | YES | `-` | - | - |
| `TotalFlightTime` | `decimal(9,2)` | YES | `-` | - | - |
| `HobbsTotal` | `decimal(10,2)` | YES | `-` | - | - |
| `Tach1Total` | `decimal(10,2)` | YES | `-` | - | - |
| `Tach2Total` | `decimal(10,2)` | YES | `-` | - | - |
| `Tach3Total` | `decimal(10,2)` | YES | `-` | - | - |
| `Tach4Total` | `decimal(10,2)` | YES | `-` | - | - |
| `Tach5Total` | `decimal(10,2)` | YES | `-` | - | - |
| `Tach6Total` | `decimal(10,2)` | YES | `-` | - | - |
| `Tach7Total` | `decimal(10,2)` | YES | `-` | - | - |
| `Tach8Total` | `decimal(10,2)` | YES | `-` | - | - |
| `AirTimeTotal` | `decimal(10,2)` | YES | `-` | - | - |
| `HeaterHobbsTotal` | `decimal(10,2)` | YES | `-` | - | - |
| `CyclesDec` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine1CyclesDec` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine2CyclesDec` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine3CyclesDec` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine4CyclesDec` | `decimal(9,2)` | YES | `-` | - | - |
| `FlightTimeOut` | `decimal(9,2)` | YES | `-` | - | - |
| `FlightTimeIn` | `decimal(9,2)` | YES | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.tblFlightRecordResources`** 
  via `FlightRecordId` → `FlightRecordId`
- **`dbo.tblMeterRecords`** 
  via `FlightRecordId` → `FlightRecordId`
- **`dbo.tblStandardFlightRecord`** 
  via `FlightRecordId` → `FlightRecordId`

## Indexes

- **`IDX_tblFlightRecord_CompanyIdStatusEnd_FlightRecordIdCreatedAt`** (NONCLUSTERED)
  - Columns: `CompanyId, Status, End INCLUDE (CreatedAt, FlightRecordId)`
- **`IDX_tblFlightRecord_Status_FlightRecordId`** (NONCLUSTERED)
  - Columns: `Status INCLUDE (FlightRecordId)`
- **`IX_tblFlightRecord`** (CLUSTERED)
  - Columns: `FlightNumber`
- **`PK_tblFlightRecord`** (PRIMARY KEY UNIQUE NONCLUSTERED)
  - Columns: `FlightRecordId`
- **`ix_CompanyID_ReservationID`** (NONCLUSTERED)
  - Columns: `CompanyId, ReservationId`
- **`ix_ReservationId`** (NONCLUSTERED)
  - Columns: `ReservationId`
- **`ix_tblFlightRecord_CompanyId_Location_Status_ObjectType_RecordedAt_includes`** (NONCLUSTERED)
  - Columns: `CompanyId, Location, Status, ObjectType, RecordedAt INCLUDE (FlightRecordId)`
