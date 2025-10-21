# PeopleGroups

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `PeopleGroupId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `GroupName` | `nvarchar(200)` | **NO** | `-` | - | - |
| `Active` | `bit` | **NO** | `-` | - | - |
| `GroupOwnerUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `Deleted` | `bit` | **NO** | `-` | - | - |
| `CreatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_PeopleGroups`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
