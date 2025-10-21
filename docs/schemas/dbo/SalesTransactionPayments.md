# SalesTransactionPayments

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (18)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `SalesTransactionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PaymentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PaymentTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `Amount` | `decimal(11,2)` | **NO** | `-` | - | - |
| `Note` | `nvarchar(500)` | YES | `-` | - | - |
| `SalesTransactionDate` | `datetime(3)` | YES | `-` | - | - |
| `CreditCardType` | `int(10,0)` | YES | `-` | - | - |
| `TransactionType` | `int(10,0)` | YES | `-` | - | - |
| `CardDetails` | `nvarchar(100)` | YES | `-` | - | - |
| `ExternalTransactionType` | `nvarchar(50)` | YES | `-` | - | - |
| `ExternalTransactionResult` | `nvarchar(2000)` | YES | `-` | - | - |
| `OriginalPaymentId` | `uniqueidentifier` | YES | `-` | - | - |
| `PaymentDate` | `datetime(3)` | YES | `-` | - | - |
| `ProPayTransactionId` | `nvarchar(15)` | YES | `-` | - | - |
| `ProPayTransactionFee` | `decimal(11,2)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_SalesTransactionPayments_OperatorIdPaymentTypeIdSalesTransactionDate_SalesTransactionId`** (NONCLUSTERED)
  - Columns: `OperatorId, PaymentTypeId, SalesTransactionDate INCLUDE (SalesTransactionId)`
- **`IDX_SalesTransactionPayments_SalesTransactionIdPaymentTypeId`** (NONCLUSTERED)
  - Columns: `SalesTransactionId, PaymentTypeId`
- **`PK_SalesTransactionPayments`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`UK_SalesTransactionPayments`** (UNIQUE NONCLUSTERED)
  - Columns: `OperatorId, SalesTransactionId, PaymentId`
- **`ix_OperatorId_PaymentTypeId_PaymentDate_Includes`** (NONCLUSTERED)
  - Columns: `OperatorId, PaymentTypeId, PaymentDate INCLUDE (Amount)`
