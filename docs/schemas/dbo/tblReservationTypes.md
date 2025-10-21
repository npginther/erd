# tblReservationTypes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (57)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `ReservationTypeId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `ReservationName` | `varchar(50)` | **NO** | `-` | - | - |
| `DisplayType` | `int(10,0)` | **NO** | `-` | - | - |
| `Display` | `varchar(50)` | **NO** | `-` | - | - |
| `Foreground` | `varchar(10)` | **NO** | `-` | - | - |
| `Background` | `varchar(10)` | **NO** | `-` | - | - |
| `IsRequired` | `bit` | **NO** | `-` | - | - |
| `OrderingId` | `int(10,0)` | **NO** | `-` | - | - |
| `Active` | `bit` | **NO** | `-` | - | - |
| `MaximumLength` | `int(10,0)` | **NO** | `-` | - | - |
| `MinimumLength` | `int(10,0)` | **NO** | `-` | - | - |
| `DefaultLength` | `int(10,0)` | **NO** | `-` | - | - |
| `IsPhoneReservation` | `bit` | **NO** | `-` | - | - |
| `DispatchedForeground` | `varchar(10)` | **NO** | `-` | - | - |
| `DispatchedBackground` | `varchar(10)` | **NO** | `-` | - | - |
| `CompletedForeground` | `varchar(10)` | **NO** | `-` | - | - |
| `CompletedBackground` | `varchar(10)` | **NO** | `-` | - | - |
| `IsV4Type` | `bit` | YES | `-` | - | - |
| `Customer1Enabled` | `bit` | YES | `-` | - | - |
| `Customer2Enabled` | `bit` | YES | `-` | - | - |
| `DisplayNameEnabled` | `bit` | YES | `-` | - | - |
| `InstructorEnabled` | `bit` | YES | `-` | - | - |
| `InstructorPrePostEnabled` | `bit` | YES | `-` | - | - |
| `AircraftEnabled` | `bit` | YES | `-` | - | - |
| `EquipmentEnabled` | `bit` | YES | `-` | - | - |
| `FlightTypeEnabled` | `bit` | YES | `-` | - | - |
| `FlightRulesEnabled` | `bit` | YES | `-` | - | - |
| `FlightHoursEnabled` | `bit` | YES | `-` | - | - |
| `FlightRouteEnabled` | `bit` | YES | `-` | - | - |
| `Customer1Requirement` | `int(10,0)` | **NO** | `-` | - | - |
| `Customer2Requirement` | `int(10,0)` | **NO** | `-` | - | - |
| `DisplayNameRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `InstructorRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `AircraftRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `EquipmentRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `FlightTypeRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `FlightRulesRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `FlightHoursRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `FlightRouteRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `IsDeleted` | `bit` | **NO** | `-` | - | - |
| `CourseRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `LessonRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseEnabled` | `bit` | YES | `-` | - | - |
| `LessonEnabled` | `bit` | YES | `-` | - | - |
| `BillingMismatchEnabled` | `bit` | YES | `-` | - | - |
| `TrainingMismatchEnabled` | `bit` | YES | `-` | - | - |
| `BillingStatusTrackingEnabled` | `bit` | **NO** | `-` | - | - |
| `TrainingStatusTrackingEnabled` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `TrackInstructionEnabled` | `bit` | YES | `-` | - | - |
| `AutofillFlightTimeEnabled` | `bit` | YES | `-` | - | - |
| `AutofillFlightInstructionTypeId` | `uniqueidentifier` | YES | `-` | - | - |
| `AutofillGroundTimeEnabled` | `bit` | YES | `-` | - | - |
| `AutofillGroundInstructionTypeId` | `uniqueidentifier` | YES | `-` | - | - |
| `IsTaxable` | `bit` | **NO** | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.ReservationTypeToPreflightAuthorizingUsersJoiner`** 
  via `ReservationTypeId` → `ReservationTypeId`

## Indexes

- **`IDX_tblReservationTypes_CompanyIdDisplayType`** (NONCLUSTERED)
  - Columns: `CompanyId, DisplayType`
- **`PK_tblReservationTypes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `ReservationTypeId`
