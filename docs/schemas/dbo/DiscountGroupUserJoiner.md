# DiscountGroupUserJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `DiscountGroupId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | PK | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_DiscountGroupUserJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `DiscountGroupId, OperatorId, UserId`
