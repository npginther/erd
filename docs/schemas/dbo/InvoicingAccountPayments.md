# InvoicingAccountPayments

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (11)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `AccountPaymentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(200)` | **NO** | `-` | - | - |
| `Price` | `decimal(9,2)` | **NO** | `-` | - | - |
| `Credit` | `decimal(9,2)` | **NO** | `-` | - | - |
| `CustomPrice` | `bit` | **NO** | `-` | - | - |
| `CreditMustEqualPrice` | `bit` | **NO** | `-` | - | - |
| `AllowPurchaseOnline` | `bit` | YES | `-` | - | - |
| `AllowPurchaseWithNegativeBalance` | `bit` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_InvoicingAccountPayments`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_InvoicingAccountPayments`** (UNIQUE NONCLUSTERED)
  - Columns: `AccountPaymentId`
