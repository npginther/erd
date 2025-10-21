# tblRemovedReservationPilots

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | PK<br/>FK->`tblRemovedReservation` | - |
| `PilotId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `ResourceGroupId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `IsStandBy` | `bit` | **NO** | `-` | - | - |
| `Start` | `datetime(3)` | **NO** | `-` | - | - |
| `End` | `datetime(3)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblRemovedReservation`** 
  via `ReservationId` → `ReservationId` `ON DELETE CASCADE`

## Indexes

- **`PK_tblRemovedReservationPilots`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `ReservationId, PilotId`
- **`ix_PilotId`** (NONCLUSTERED)
  - Columns: `PilotId`
