# AzureSyncTablesForCurriculum

**Schema:** `AzureSync`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (3)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `TableName` | `varchar(255)` | **NO** | `-` | - | - |
| `FullCopy` | `bit` | YES | `-` | - | - |

## Indexes

- **`PK_AzureSyncTablesForCurriculum`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
