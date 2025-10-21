# AccountingSyncBatchTransactions

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (11)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `BatchId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TransactionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Status` | `int(10,0)` | **NO** | `-` | - | - |
| `Errors` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Details` | `nvarchar(MAX)` | YES | `-` | - | - |
| `StatusChangedAt` | `datetime(3)` | YES | `-` | - | - |
| `SyncAttempts` | `int(10,0)` | YES | `-` | - | - |
| `CleanupFailures` | `nvarchar(MAX)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_AccountingSyncBatchTransactions_OperatorIdBatchIdTransactionId`** (NONCLUSTERED)
  - Columns: `OperatorId, BatchId, TransactionId`
- **`PK_AccountingSyncBatchTransactions`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
