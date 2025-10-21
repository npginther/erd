# DiscountGroup

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (19)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `DiscountGroupId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Type` | `int(10,0)` | **NO** | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(200)` | **NO** | `-` | - | - |
| `Active` | `bit` | **NO** | `-` | - | - |
| `AircraftRentalDiscount` | `decimal(5,2)` | YES | `-` | - | - |
| `InstructionDiscount` | `decimal(5,2)` | YES | `-` | - | - |
| `ProductsDiscount` | `decimal(5,2)` | YES | `-` | - | - |
| `AircraftRentalRateTypeId` | `uniqueidentifier` | YES | `-` | - | - |
| `MinimumBalanceRequired` | `bit` | YES | `-` | - | - |
| `MinimumBalance` | `decimal(11,2)` | YES | `-` | - | - |
| `RenewalSpan` | `int(10,0)` | YES | `-` | - | - |
| `RenewalPeriod` | `int(10,0)` | YES | `-` | - | - |
| `ActivateUserOnActivate` | `bit` | YES | `-` | - | - |
| `AssignToRoleOnActivate` | `int(10,0)` | YES | `-` | - | - |
| `SendNotificationOnActivate` | `bit` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_DiscountGroups`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
