# tblInvoicingTransactions

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (33)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `TransactionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TransactionType` | `int(10,0)` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ParentId` | `uniqueidentifier` | YES | `-` | - | - |
| `Created` | `datetime(3)` | **NO** | `-` | - | - |
| `Date` | `datetime(3)` | **NO** | `-` | - | - |
| `Amount` | `decimal(11,2)` | **NO** | `-` | - | - |
| `PaymentType` | `int(10,0)` | YES | `-` | - | - |
| `PaymentNote` | `nvarchar(500)` | YES | `-` | - | - |
| `VisibilityStatus` | `int(10,0)` | YES | `-` | - | - |
| `InvoiceStatus` | `int(10,0)` | YES | `-` | - | - |
| `ClientName` | `nvarchar(75)` | YES | `-` | - | - |
| `ClientAddress` | `nvarchar(250)` | YES | `-` | - | - |
| `InvoiceNumber` | `nvarchar(25)` | YES | `-` | - | - |
| `PONumber` | `nvarchar(50)` | YES | `-` | - | - |
| `Discount` | `decimal(4,2)` | YES | `-` | - | - |
| `Terms` | `text(2147483647)` | YES | `-` | - | - |
| `Comments` | `text(2147483647)` | YES | `-` | - | - |
| `TotalPayments` | `decimal(11,2)` | YES | `-` | - | - |
| `Description` | `nvarchar(50)` | YES | `-` | - | - |
| `ProcessorTypeId` | `uniqueidentifier` | YES | `-` | - | - |
| `ChargeSerialization` | `text(2147483647)` | YES | `-` | - | - |
| `VoidSerialization` | `text(2147483647)` | YES | `-` | - | - |
| `CCReferenceId` | `nvarchar(50)` | YES | `-` | - | - |
| `CCType` | `int(10,0)` | YES | `-` | - | - |
| `CCNumber` | `nvarchar(50)` | YES | `-` | - | - |
| `CCExpDate` | `datetime(3)` | YES | `-` | - | - |
| `CanBeRecurringTrans` | `bit` | **NO** | `-` | - | - |
| `CurrentBalance` | `decimal(12,2)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_tblInvoicingTransactions_CompanyId_VisibilityStatus`** (NONCLUSTERED)
  - Columns: `CompanyId, VisibilityStatus INCLUDE (Amount, Created, ParentId, PaymentNote, PaymentType, TransactionId, TransactionType)`
- **`IX_tblInvoicingTransactions_CompanyIdUserId`** (NONCLUSTERED)
  - Columns: `CompanyId, UserId`
- **`IX_tblInvoicingTransactions_ParentId`** (NONCLUSTERED)
  - Columns: `ParentId`
- **`IX_tblInvoicingTransactions_TransTypeCompanyIdVisibilityStatusUserIdAmount`** (NONCLUSTERED)
  - Columns: `TransactionType, CompanyId, VisibilityStatus INCLUDE (Amount, UserId)`
- **`IX_tblInvoicingTransactions_TransactionType_CompanyId_ParentId_VisibilityStatus`** (NONCLUSTERED)
  - Columns: `TransactionType, CompanyId, ParentId, VisibilityStatus`
- **`IX_tblInvoicingTransactions_transTypeVisibilityStatus`** (NONCLUSTERED)
  - Columns: `TransactionType, VisibilityStatus, CompanyId, UserId, Amount`
- **`PK_tblInvoicingTransactions_1`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `RowId`
- **`ix_tblInvoicingTransactions_CompanyId_Date_includes`** (NONCLUSTERED)
  - Columns: `CompanyId, Date INCLUDE (InvoiceNumber, TransactionId, UserId)`
- **`ix_tblInvoicingTransactions_CompanyId_InvoiceNumber`** (NONCLUSTERED)
  - Columns: `CompanyId, InvoiceNumber`
- **`ix_tblInvoicingTransactions_TransactionType_CompanyId_VisibilityStatus_includes`** (NONCLUSTERED)
  - Columns: `TransactionType, CompanyId, VisibilityStatus INCLUDE (Amount, ClientName, Date, Description, InvoiceNumber, InvoiceStatus, TotalPayments, TransactionId)`
