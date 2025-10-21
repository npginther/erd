# MembershipSubscriptionsHistory

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (8)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `SubscriptionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EventUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `EventDateUtc` | `datetime(3)` | **NO** | `-` | - | - |
| `EventType` | `nvarchar(15)` | **NO** | `-` | - | - |
| `EventData` | `nvarchar(MAX)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_MembershipSubscriptionsHistory`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
