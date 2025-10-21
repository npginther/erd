# tblInvoicingPayments

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PaymentId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `InvoiceId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Date` | `datetime(3)` | **NO** | `-` | - | - |
| `Amount` | `decimal(11,2)` | **NO** | `-` | - | - |
| `PaymentType` | `int(10,0)` | YES | `-` | - | - |
| `Note` | `nvarchar(500)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblInvoicingPayments`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PaymentId`
