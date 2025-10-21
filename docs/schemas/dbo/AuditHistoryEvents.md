# AuditHistoryEvents

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (22)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `EventId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `EventType` | `int(10,0)` | **NO** | `-` | - | - |
| `EventDate` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `LocationId` | `int(10,0)` | YES | `-` | - | - |
| `LocationName` | `nvarchar(50)` | YES | `-` | - | - |
| `CreatedById` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CreatedByName` | `nvarchar(200)` | **NO** | `-` | - | - |
| `IPAddress` | `nvarchar(39)` | YES | `-` | - | - |
| `Message` | `nvarchar(1024)` | YES | `-` | - | - |
| `ResourceId` | `uniqueidentifier` | YES | `-` | - | - |
| `ResourceName` | `nvarchar(200)` | YES | `-` | - | - |
| `ResourceType` | `int(10,0)` | YES | `-` | - | - |
| `Data` | `nvarchar(MAX)` | YES | `-` | - | - |
| `OriginalJson` | `nvarchar(MAX)` | YES | `-` | - | - |
| `ResultingJson` | `nvarchar(MAX)` | YES | `-` | - | - |
| `PatchJson` | `nvarchar(MAX)` | YES | `-` | - | - |
| `ProductType` | `nvarchar(100)` | YES | `-` | - | - |
| `CreatedByGlobalUserId` | `bigint(19,0)` | YES | `-` | - | - |
| `ObjectId` | `nvarchar(100)` | YES | `-` | - | - |
| `ObjectName` | `nvarchar(200)` | YES | `-` | - | - |
| `ObjectType` | `nvarchar(100)` | YES | `-` | - | - |

## Indexes

- **`PK_AuditHistoryEvents`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `EventId`
- **`ix_OperatorIdResourceIdEventTypeEventDate`** (NONCLUSTERED)
  - Columns: `OperatorId, ResourceId, EventType, EventDate`
