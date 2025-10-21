# MembershipSubscriptions

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (19)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `SubscriptionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `MembershipId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Status` | `int(10,0)` | **NO** | `-` | - | - |
| `CreatedLocal` | `datetime(3)` | **NO** | `-` | - | - |
| `CreatedUtc` | `datetime(3)` | **NO** | `-` | - | - |
| `ExpiresLocal` | `datetime(3)` | **NO** | `-` | - | - |
| `ExpiresUtc` | `datetime(3)` | **NO** | `-` | - | - |
| `Amount` | `decimal(11,2)` | **NO** | `-` | - | - |
| `Recurring` | `bit` | **NO** | `-` | - | - |
| `ActivationDate` | `datetime(3)` | **NO** | `-` | - | - |
| `CancelledAtUtc` | `datetime(3)` | YES | `-` | - | - |
| `CancelledBy` | `uniqueidentifier` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `LocationId` | `int(10,0)` | YES | `-` | - | - |
| `PayableByAccount` | `bit` | YES | `-` | - | - |
| `CreditCardChargingAt` | `datetime(3)` | YES | `-` | - | - |

## Indexes

- **`PK_MembershipSubscriptions`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
