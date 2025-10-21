# tblInvoicingInvoice

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (18)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `InvoiceId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `VisibilityStatus` | `int(10,0)` | **NO** | `-` | - | - |
| `InvoiceStatus` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ClientName` | `nvarchar(75)` | **NO** | `-` | - | - |
| `ClientAddress` | `nvarchar(250)` | **NO** | `-` | - | - |
| `InvoiceNumber` | `nvarchar(25)` | **NO** | `-` | - | - |
| `Date` | `datetime(3)` | **NO** | `-` | - | - |
| `PONumber` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Discount` | `decimal(4,2)` | **NO** | `-` | - | - |
| `Terms` | `text(2147483647)` | **NO** | `-` | - | - |
| `Comments` | `text(2147483647)` | **NO** | `-` | - | - |
| `TotalPayments` | `decimal(11,2)` | **NO** | `-` | - | - |
| `Total` | `decimal(11,2)` | **NO** | `-` | - | - |
| `Description` | `varchar(50)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IX_tblInvoicingInvoice_InvoiceNumber`** (UNIQUE NONCLUSTERED)
  - Columns: `CompanyId, InvoiceNumber`
- **`PK_tblInvoicingInvoice`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `InvoiceId`
