# SyncRuns

**Schema:** `AzureSync`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `DataSet` | `varchar(50)` | **NO** | `-` | - | - |
| `SyncStart` | `datetime(3)` | **NO** | `-` | - | - |
| `SyncComplete` | `datetime(3)` | YES | `-` | - | - |

## Indexes

- **`PK_SyncRuns`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
