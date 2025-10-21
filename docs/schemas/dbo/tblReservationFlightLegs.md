# tblReservationFlightLegs

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (19)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Counter` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `LegId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `ParentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | YES | `-` | - | - |
| `DepartureTime` | `datetime(3)` | YES | `-` | - | - |
| `ArrivalTime` | `datetime(3)` | YES | `-` | - | - |
| `DepartureAirport` | `varchar(50)` | **NO** | `-` | - | - |
| `ArrivalAirport` | `varchar(50)` | **NO** | `-` | - | - |
| `TripAuthorizer` | `varchar(200)` | **NO** | `-` | - | - |
| `LeadPassengerUserGUIDId` | `uniqueidentifier` | YES | `-` | - | - |
| `PIC` | `uniqueidentifier` | YES | `-` | - | - |
| `SIC` | `uniqueidentifier` | YES | `-` | - | - |
| `CustomerUserGUIDId` | `uniqueidentifier` | YES | `-` | - | - |
| `Comments` | `varchar(500)` | **NO** | `-` | - | - |
| `InternalComments` | `varchar(500)` | **NO** | `-` | - | - |
| `CreatedFor` | `varchar(100)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IX_tblReservationFlightLegs_CompanyId`** (NONCLUSTERED)
  - Columns: `CompanyId`
- **`IX_tblReservationFlightLegs_ParentId`** (NONCLUSTERED)
  - Columns: `ParentId`
- **`PK_tblReservationFlightLegs`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Counter`
