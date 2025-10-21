# tblReservationResources

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (14)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | PK<br/>FK->`tblReservation` | - |
| `ItemId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `ResourceGroupId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `IsStandBy` | `bit` | **NO** | `-` | - | - |
| `ResourceType` | `int(10,0)` | **NO** | `-` | - | - |
| `Start` | `datetime(3)` | **NO** | `-` | - | - |
| `End` | `datetime(3)` | **NO** | `-` | - | - |
| `ByType` | `bit` | **NO** | `-` | - | - |
| `_RowId` | `bigint(19,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `SchedulingSlotId` | `int(10,0)` | YES | `-` | - | - |
| `SlotManuallySelected` | `bit` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblReservation`** 
  via `ReservationId` → `ReservationId` `ON DELETE CASCADE`

## Indexes

- **`CX_tblReservationResources`** (UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`IDX_tblReservationResources_CompanyIdIsStandByItemIdStartEnd_ReservationId`** (NONCLUSTERED)
  - Columns: `CompanyId, IsStandBy, ItemId, Start, End INCLUDE (ReservationId)`
- **`IDX_tblReservationResources_CompanyIdItemIdStartEnd_ReservationId`** (NONCLUSTERED)
  - Columns: `CompanyId, ItemId, Start, End INCLUDE (ReservationId)`
- **`IDX_tblReservationResources_ItemIdIsStandByStartEnd_ReservationId`** (NONCLUSTERED)
  - Columns: `ItemId, IsStandBy, Start, End INCLUDE (ReservationId)`
- **`PK_tblReservationResources`** (PRIMARY KEY UNIQUE NONCLUSTERED)
  - Columns: `ReservationId, ItemId`
- **`ix_tblReservationResources_ItemId_CompanyId_ResourceType_includes`** (NONCLUSTERED)
  - Columns: `ItemId, CompanyId, ResourceType INCLUDE (ReservationId)`
