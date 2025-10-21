# AzureSyncTablesForCore

**Schema:** `AzureSync`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (3)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `TableName` | `varchar(255)` | **NO** | `-` | - | - |
| `FullCopy` | `bit` | YES | `-` | - | - |
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |

## Indexes

- **`PK_AzureSyncTablesForCore`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
