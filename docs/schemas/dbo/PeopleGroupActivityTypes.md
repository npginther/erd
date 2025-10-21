# PeopleGroupActivityTypes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `PeopleGroupId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ActivityTypeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CreatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_PeopleGroupActivityTypes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
