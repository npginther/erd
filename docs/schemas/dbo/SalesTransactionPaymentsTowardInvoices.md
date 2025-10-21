# SalesTransactionPaymentsTowardInvoices

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `PaymentInvoiceId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PaidInvoiceId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Amount` | `decimal(11,2)` | **NO** | `-` | - | - |
| `Returned` | `decimal(11,2)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_SalesTransactionPaymentsTowardInvoices`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
