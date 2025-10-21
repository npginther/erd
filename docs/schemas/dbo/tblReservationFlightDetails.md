# tblReservationFlightDetails

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | PK<br/>FK->`tblReservation` | - |
| `FlightRules` | `int(10,0)` | **NO** | `-` | - | - |
| `FlightRoute` | `int(10,0)` | **NO** | `-` | - | - |
| `Destination` | `varchar(500)` | **NO** | `-` | - | - |
| `FlightTime` | `decimal(6,2)` | **NO** | `-` | - | - |
| `Comments` | `varchar(2000)` | YES | `-` | - | - |
| `InternalComments` | `varchar(500)` | **NO** | `-` | - | - |
| `_RowId` | `bigint(19,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblReservation`** 
  via `ReservationId` → `ReservationId` `ON DELETE CASCADE`

## Indexes

- **`CX_tblReservationFlightDetails`** (UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`IDX_tblReservationFlightDetails_OperatorId_ReservationId`** (NONCLUSTERED)
  - Columns: `OperatorId INCLUDE (ReservationId)`
- **`PK_tblReservationFlightDetails`** (PRIMARY KEY UNIQUE NONCLUSTERED)
  - Columns: `ReservationId`
