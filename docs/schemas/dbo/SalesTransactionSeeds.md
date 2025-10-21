# SalesTransactionSeeds

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (8)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `SalesTransactionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TransactionNumber` | `int(10,0)` | **NO** | `-` | - | - |
| `SeedDate` | `datetime(3)` | **NO** | `-` | - | - |
| `ReservationId` | `uniqueidentifier` | YES | `-` | - | - |
| `ReturnInvoiceId` | `uniqueidentifier` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_SalesTransactionSeeds`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`UK_SalesTransactionSeeds`** (UNIQUE NONCLUSTERED)
  - Columns: `OperatorId, SalesTransactionId`
