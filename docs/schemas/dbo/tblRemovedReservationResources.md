# tblRemovedReservationResources

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (12)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | PK<br/>FK->`tblRemovedReservation` | - |
| `ItemId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `ResourceGroupId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `IsStandBy` | `bit` | **NO** | `-` | - | - |
| `ResourceType` | `int(10,0)` | **NO** | `-` | - | - |
| `Start` | `datetime(3)` | **NO** | `-` | - | - |
| `End` | `datetime(3)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `SchedulingSlotId` | `int(10,0)` | YES | `-` | - | - |
| `SlotManuallySelected` | `bit` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblRemovedReservation`** 
  via `ReservationId` → `ReservationId` `ON DELETE CASCADE`

## Indexes

- **`PK_tblRemovedReservationResources`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `ReservationId, ItemId`
