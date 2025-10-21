# tblAircraft

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (82)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `AircraftMakeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `AircraftModelId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TailNumber` | `varchar(25)` | **NO** | `-` | - | - |
| `Class` | `int(10,0)` | **NO** | `-` | - | - |
| `LocationId` | `int(10,0)` | **NO** | `-` | - | - |
| `TieDownHangerNum` | `varchar(50)` | **NO** | `-` | - | - |
| `NumberOfSeats` | `varchar(50)` | **NO** | `-` | - | - |
| `ColorScheme` | `varchar(50)` | **NO** | `-` | - | - |
| `SerialNumber` | `varchar(50)` | **NO** | `-` | - | - |
| `FuelCapacity` | `varchar(50)` | **NO** | `-` | - | - |
| `FuelType` | `int(10,0)` | **NO** | `-` | - | - |
| `CustomFuelType` | `varchar(50)` | **NO** | `-` | - | - |
| `Year` | `varchar(10)` | **NO** | `-` | - | - |
| `ScheduleOrder` | `int(10,0)` | **NO** | `-` | - | - |
| `SpecialNotes` | `varchar(250)` | **NO** | `-` | - | - |
| `OtherNotes` | `varchar(250)` | **NO** | `-` | - | - |
| `Nationality` | `varchar(50)` | **NO** | `-` | - | - |
| `StartDateAvailable` | `datetime(3)` | **NO** | `-` | - | - |
| `EndDateAvailable` | `datetime(3)` | **NO** | `-` | - | - |
| `EngineCount` | `int(10,0)` | **NO** | `-` | - | - |
| `TotalTimeInType` | `decimal(9,4)` | **NO** | `-` | - | - |
| `Active` | `bit` | **NO** | `-` | - | - |
| `RequireCheckOuts` | `bit` | **NO** | `-` | - | - |
| `CheckOutsExpire` | `bit` | **NO** | `-` | - | - |
| `CheckOutExpirationDays` | `int(10,0)` | **NO** | `-` | - | - |
| `MaxReservationDuration` | `decimal(7,3)` | **NO** | `-` | - | - |
| `MinReservationDuration` | `decimal(7,4)` | **NO** | `-` | - | - |
| `IsDeleted` | `bit` | **NO** | `-` | - | - |
| `IsIFRCertified` | `bit` | **NO** | `-` | - | - |
| `HasHobbsMeter` | `bit` | **NO** | `-` | - | - |
| `HobbsMeter` | `decimal(9,2)` | **NO** | `-` | - | - |
| `Tach` | `decimal(16,2)` | **NO** | `-` | - | - |
| `HasTach` | `bit` | **NO** | `-` | - | - |
| `HasPropellers` | `bit` | **NO** | `-` | - | - |
| `HasTurbines` | `bit` | **NO** | `-` | - | - |
| `HeaterHobbsMeter` | `decimal(9,2)` | **NO** | `-` | - | - |
| `AirTimeMeter` | `decimal(9,2)` | **NO** | `-` | - | - |
| `TotalTimeAdjustment` | `decimal(9,2)` | **NO** | `-` | - | - |
| `TotalTimeTracking` | `int(10,0)` | **NO** | `-` | - | - |
| `TotalTimeTrackingCount` | `int(10,0)` | **NO** | `-` | - | - |
| `HasHeaterHobbsMeter` | `bit` | **NO** | `-` | - | - |
| `HasAirTimeMeter` | `bit` | **NO** | `-` | - | - |
| `TotalTimeMeterType` | `int(10,0)` | **NO** | `-` | - | - |
| `TotalTimeMeterIndex` | `int(10,0)` | **NO** | `-` | - | - |
| `RequiresMedicalCert` | `bit` | **NO** | `-` | - | - |
| `DisplayBookingAlert` | `bit` | **NO** | `-` | - | - |
| `BookingAlert` | `varchar(140)` | **NO** | `-` | - | - |
| `CategoryClass` | `nvarchar(5)` | YES | `-` | - | - |
| `IsComplex` | `bit` | YES | `-` | - | - |
| `IsHighPerformance` | `bit` | YES | `-` | - | - |
| `IsTailWheel` | `bit` | YES | `-` | - | - |
| `IsLSA` | `bit` | YES | `-` | - | - |
| `RequiredFAACertificate` | `int(10,0)` | YES | `-` | - | - |
| `RequiredTCCertificate` | `int(10,0)` | YES | `-` | - | - |
| `IsPressurized` | `bit` | YES | `-` | - | - |
| `UsefulLoad` | `nvarchar(50)` | YES | `-` | - | - |
| `EmptyWeight` | `nvarchar(50)` | YES | `-` | - | - |
| `MaxGrossWeight` | `nvarchar(50)` | YES | `-` | - | - |
| `ARM` | `nvarchar(50)` | YES | `-` | - | - |
| `Moment` | `nvarchar(50)` | YES | `-` | - | - |
| `Description` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Avionics` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Accessories` | `nvarchar(MAX)` | YES | `-` | - | - |
| `BillingMeter` | `int(10,0)` | YES | `-` | - | - |
| `TrackOilFuel` | `bit` | YES | `-` | - | - |
| `TrackCycles` | `bit` | **NO** | `-` | - | - |
| `CurrentCycles` | `int(10,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `SchedulingGroupId` | `uniqueidentifier` | YES | `-` | - | - |
| `SchedulingGroupOrder` | `int(10,0)` | YES | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `ExternalId` | `nvarchar(50)` | YES | `-` | - | - |
| `DisplayMismatches` | `bit` | **NO** | `-` | - | - |
| `IsTAA` | `bit` | **NO** | `-` | - | - |
| `CurrentTime` | `decimal(9,2)` | YES | `-` | - | - |
| `AirframeCycles` | `decimal(9,2)` | YES | `-` | - | - |
| `HasFlightTimeMeter` | `bit` | **NO** | `-` | - | - |
| `FlightTimeMeter` | `decimal(9,2)` | **NO** | `-` | - | - |
| `AirTimeMeterFormat` | `int(10,0)` | **NO** | `-` | - | - |
| `FlightTimeMeterFormat` | `int(10,0)` | **NO** | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.ScheduleMatchUserPreferencesToAircraftJoiner`** 
  via `AircraftId` → `AircraftId`

## Indexes

- **`IDX_tblAircraft_ActiveIsDeletedAircraftIdCompanyIdLocationId`** (NONCLUSTERED)
  - Columns: `Active, IsDeleted INCLUDE (AircraftId, CompanyId, LocationId)`
- **`IDX_tblAircraft_CompanyIdActiveIsDeleted_AircraftIdLocationId`** (NONCLUSTERED)
  - Columns: `CompanyId, Active, IsDeleted INCLUDE (AircraftId, LocationId)`
- **`IDX_tblAircraft_CompanyIdBillingMeter`** (NONCLUSTERED)
  - Columns: `CompanyId, BillingMeter`
- **`PK_tblAircraft`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AircraftId`
