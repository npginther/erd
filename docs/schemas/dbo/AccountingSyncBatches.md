# AccountingSyncBatches

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (16)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `BatchId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Status` | `int(10,0)` | **NO** | `-` | - | - |
| `OpenedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `CreatedAt` | `datetime(3)` | YES | `-` | - | - |
| `CompletedAt` | `datetime(3)` | YES | `-` | - | - |
| `Description` | `nvarchar(250)` | YES | `-` | - | - |
| `Content` | `nvarchar(MAX)` | YES | `-` | - | - |
| `AccountingPackage` | `nvarchar(25)` | YES | `-` | - | - |
| `Transactions` | `int(10,0)` | **NO** | `-` | - | - |
| `CreatedBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `BatchType` | `int(10,0)` | **NO** | `-` | - | - |
| `OnlyIncludeActive` | `bit` | YES | `-` | - | - |
| `SyncInitiated` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_AccountingSyncBatches_OperatorIdBatchId`** (NONCLUSTERED)
  - Columns: `OperatorId, BatchId`
- **`PK_AccountingSyncBatches`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
