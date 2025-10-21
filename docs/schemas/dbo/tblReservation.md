# tblReservation

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (42)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `GroupingId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `ReservationTypeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `IsStandby` | `bit` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `ReservationNumber` | `bigint(19,0)` | **NO** | `-` | - | - |
| `PreFlightMinutes` | `int(10,0)` | **NO** | `-` | - | - |
| `PostFlightMinutes` | `int(10,0)` | **NO** | `-` | - | - |
| `Start` | `datetime(3)` | **NO** | `-` | - | - |
| `End` | `datetime(3)` | **NO** | `-` | - | - |
| `Created` | `datetime(3)` | **NO** | `-` | - | - |
| `CreatedByUserId` | `int(10,0)` | **NO** | `-` | - | - |
| `Locked` | `bit` | **NO** | `-` | - | - |
| `CreatedFor` | `varchar(100)` | **NO** | `-` | - | - |
| `EmailNotification` | `bit` | **NO** | `-` | - | - |
| `ByAircraftType` | `bit` | **NO** | `-` | - | - |
| `HasBeenAssignedAircraft` | `bit` | **NO** | `-` | - | - |
| `DispatchId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LocationId` | `int(10,0)` | **NO** | `-` | - | - |
| `ReservationObjectId` | `int(10,0)` | **NO** | `-` | - | - |
| `SendPilotEmails` | `bit` | **NO** | `-` | - | - |
| `SendCustomerEmails` | `bit` | **NO** | `-` | - | - |
| `AdditionalNotificationAddresses` | `text(2147483647)` | **NO** | `-` | - | - |
| `AdditionalUserIdsForNotification` | `text(2147483647)` | **NO** | `-` | - | - |
| `StartUTC` | `datetime(3)` | YES | `-` | - | - |
| `EndUTC` | `datetime(3)` | YES | `-` | - | - |
| `App` | `int(10,0)` | YES | `-` | - | - |
| `InvoiceId` | `uniqueidentifier` | YES | `-` | - | - |
| `InvoiceStatus` | `int(10,0)` | YES | `-` | - | - |
| `InvoiceNumber` | `int(10,0)` | YES | `-` | - | - |
| `CourseId` | `uniqueidentifier` | YES | `-` | - | - |
| `LessonId` | `uniqueidentifier` | YES | `-` | - | - |
| `BillingStatus` | `int(10,0)` | YES | `-` | - | - |
| `BillingMismatches` | `nvarchar(500)` | YES | `-` | - | - |
| `TrainingStatus` | `int(10,0)` | YES | `-` | - | - |
| `TrainingMismatches` | `nvarchar(500)` | YES | `-` | - | - |
| `BillingMismatchStatusChecked` | `bit` | YES | `-` | - | - |
| `TrainingMismatchStatusChecked` | `bit` | YES | `-` | - | - |
| `BillingMismatchStatus` | `int(10,0)` | YES | `-` | - | - |
| `TrainingMismatchStatus` | `int(10,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.FlightAlerts`** 
  via `ReservationId` → `ReservationId`
- **`dbo.tblReservationPilots`** 
  via `ReservationId` → `ReservationId`
- **`dbo.tblReservationFlightDetails`** 
  via `ReservationId` → `ReservationId`
- **`dbo.tblReservationResources`** 
  via `ReservationId` → `ReservationId`
- **`dbo.tblReservationNotifications`** 
  via `ReservationId` → `ReservationId`
- **`dbo.ReservationTrainingSessions`** 
  via `ReservationId` → `ReservationId`

## Indexes

- **`IDX_tblReservation_GroupingId_CompanyId_ReservationId_Start_End`** (NONCLUSTERED)
  - Columns: `GroupingId, CompanyId INCLUDE (End, ReservationId, Start)`
- **`IDX_tblReservation_ReservationTypeIdIsStandByCompanyIdStartEnd_ReservationIdDispatchId`** (NONCLUSTERED)
  - Columns: `ReservationTypeId, IsStandby, CompanyId, Start, End INCLUDE (DispatchId, ReservationId)`
- **`IX_tblReservationClustered`** (CLUSTERED)
  - Columns: `ReservationNumber`
- **`IX_tblReservation_CompanyDates`** (NONCLUSTERED)
  - Columns: `CompanyId, Start, End, IsStandby`
- **`IX_tblReservation_IdTypeId`** (NONCLUSTERED)
  - Columns: `ReservationId, ReservationTypeId`
- **`PK_tblReservation`** (PRIMARY KEY UNIQUE NONCLUSTERED)
  - Columns: `ReservationId`
- **`ix_CompanyId_Created`** (NONCLUSTERED)
  - Columns: `CompanyId, Created`
- **`ix_CompanyId_Includes`** (NONCLUSTERED)
  - Columns: `CompanyId INCLUDE (EndUTC, ReservationId, ReservationTypeId, StartUTC)`
- **`ix_DispatchId`** (NONCLUSTERED)
  - Columns: `DispatchId`
- **`ix_DispatchId_Includes`** (NONCLUSTERED)
  - Columns: `DispatchId INCLUDE (ReservationId)`
- **`ix_tblReservation_IsStandby_CompanyId_Start_End_includes`** (NONCLUSTERED)
  - Columns: `IsStandby, CompanyId, Start, End INCLUDE (Created, DispatchId, LocationId, ReservationId, ReservationObjectId, ReservationTypeId)`
