# ConsolidatedReservations

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (15)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `IsStandBy` | `bit` | **NO** | `-` | - | - |
| `ResourceId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `ResourceType` | `int(10,0)` | **NO** | `-` | - | - |
| `Start` | `datetime(3)` | **NO** | `-` | - | - |
| `End` | `datetime(3)` | **NO** | `-` | - | - |
| `ReservationTypeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PilotUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `Pilot2UserId` | `uniqueidentifier` | YES | `-` | - | - |
| `CreatedFor` | `varchar(100)` | **NO** | `-` | - | - |
| `IsDispatched` | `bit` | **NO** | `-` | - | - |
| `IsCompleted` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_ConsolidatedReservations`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `ReservationId, ResourceId`
