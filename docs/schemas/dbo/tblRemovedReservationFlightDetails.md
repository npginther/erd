# tblRemovedReservationFlightDetails

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | PK<br/>FK->`tblRemovedReservation` | - |
| `FlightRules` | `int(10,0)` | **NO** | `-` | - | - |
| `FlightRoute` | `int(10,0)` | **NO** | `-` | - | - |
| `Destination` | `varchar(500)` | **NO** | `-` | - | - |
| `FlightTime` | `decimal(6,2)` | **NO** | `-` | - | - |
| `Comments` | `varchar(2000)` | YES | `-` | - | - |
| `InternalComments` | `varchar(500)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblRemovedReservation`** 
  via `ReservationId` → `ReservationId` `ON DELETE CASCADE`

## Indexes

- **`PK_tblRemovedReservationFlightDetails`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `ReservationId`
