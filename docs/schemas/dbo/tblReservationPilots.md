# tblReservationPilots

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | PK<br/>FK->`tblReservation` | - |
| `PilotId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `ResourceGroupId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `IsStandBy` | `bit` | **NO** | `-` | - | - |
| `Start` | `datetime(3)` | **NO** | `-` | - | - |
| `End` | `datetime(3)` | **NO** | `-` | - | - |
| `_RowId` | `bigint(19,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblReservation`** 
  via `ReservationId` → `ReservationId` `ON DELETE CASCADE`

## Indexes

- **`CX_tblReservationPilots`** (UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`IX_tblReservationPilots`** (NONCLUSTERED)
  - Columns: `ReservationId, PilotId, CompanyId, End`
- **`IX_tblReservationPilotsFields`** (NONCLUSTERED)
  - Columns: `PilotId, CompanyId, IsStandBy, Start, End`
- **`PK_tblReservationPilots`** (PRIMARY KEY UNIQUE NONCLUSTERED)
  - Columns: `ReservationId, PilotId`
