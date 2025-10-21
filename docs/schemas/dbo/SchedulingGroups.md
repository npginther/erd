# SchedulingGroups

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `SchedulingGroupId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `LocationId` | `int(10,0)` | **NO** | `-` | - | - |
| `Title` | `nvarchar(MAX)` | **NO** | `-` | - | - |
| `TailAssignmentType` | `int(10,0)` | **NO** | `-` | - | - |
| `ReserveCapacityPercent` | `int(10,0)` | YES | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_SchedulingGroups`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`UK_SchedulingGroups_OperatorId_SchedulingGroupId`** (UNIQUE NONCLUSTERED)
  - Columns: `OperatorId, SchedulingGroupId`
