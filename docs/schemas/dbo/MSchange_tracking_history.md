# MSchange_tracking_history

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `internal_table_name` | `nvarchar(128)` | **NO** | `-` | - | - |
| `table_name` | `nvarchar(128)` | **NO** | `-` | - | - |
| `start_time` | `datetime(3)` | **NO** | `-` | - | - |
| `end_time` | `datetime(3)` | **NO** | `-` | - | - |
| `rows_cleaned_up` | `bigint(19,0)` | **NO** | `-` | - | - |
| `cleanup_version` | `bigint(19,0)` | **NO** | `-` | - | - |
| `comments` | `nvarchar(MAX)` | **NO** | `-` | - | - |

## Indexes

- **`IX_MSchange_tracking_history_start_time`** (NONCLUSTERED)
  - Columns: `start_time`
