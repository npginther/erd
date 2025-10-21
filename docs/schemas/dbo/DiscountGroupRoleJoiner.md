# DiscountGroupRoleJoiner

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
| `RoleId` | `int(10,0)` | **NO** | `-` | PK | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_DiscountGroupRoleJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `DiscountGroupId, OperatorId, RoleId`
