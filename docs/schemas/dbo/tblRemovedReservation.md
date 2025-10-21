# tblRemovedReservation

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (30)

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
| `DeletionReason` | `varchar(500)` | **NO** | `-` | - | - |
| `DeletedBy` | `int(10,0)` | **NO** | `-` | - | - |
| `ByAircraftType` | `bit` | **NO** | `-` | - | - |
| `HasBeenAssignedAircraft` | `bit` | **NO** | `-` | - | - |
| `DispatchId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LocationId` | `int(10,0)` | **NO** | `-` | - | - |
| `DeletedAt` | `datetime(3)` | **NO** | `-` | - | The Date and Time the reservation was deleted. |
| `ReservationObjectId` | `int(10,0)` | **NO** | `-` | - | - |
| `SendPilotEmails` | `bit` | **NO** | `-` | - | - |
| `SendCustomerEmails` | `bit` | **NO** | `-` | - | - |
| `IsPhoneReservation` | `bit` | **NO** | `-` | - | - |
| `CancellationReasonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CancellationCause` | `int(10,0)` | YES | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.tblRemovedReservationResources`** 
  via `ReservationId` → `ReservationId`
- **`dbo.tblRemovedReservationPilots`** 
  via `ReservationId` → `ReservationId`
- **`dbo.tblRemovedReservationFlightDetails`** 
  via `ReservationId` → `ReservationId`

## Indexes

- **`PK_tblRemovedReservation`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `ReservationId`
- **`ix_tblRemovedReservation_CompanyId_Start_End_includes`** (NONCLUSTERED)
  - Columns: `CompanyId, Start, End INCLUDE (ReservationId)`
- **`ix_tblRemovedReservation_IsStandby_CompanyId_Start_End`** (NONCLUSTERED)
  - Columns: `IsStandby, CompanyId, Start, End`
- **`ix_tblRemovedReservation_LocationId_Start_includes`** (NONCLUSTERED)
  - Columns: `LocationId, Start INCLUDE (CancellationReasonId, DeletedAt, DeletedBy, DeletionReason, End, ReservationId, ReservationObjectId)`
