# MassEmailUserIds

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `MassEmailId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_MassEmailUserIds`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_MassEmailUserIds_MassEmailId_UserId`** (UNIQUE NONCLUSTERED)
  - Columns: `MassEmailId, UserId`
