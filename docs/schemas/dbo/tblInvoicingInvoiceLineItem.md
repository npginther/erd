# tblInvoicingInvoiceLineItem

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (17)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `InvoiceId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `Sequence` | `int(10,0)` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `LineItemId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Name` | `varchar(75)` | **NO** | `-` | - | - |
| `Description` | `varchar(500)` | **NO** | `-` | - | - |
| `UnitCost` | `decimal(11,2)` | **NO** | `-` | - | - |
| `Quantity` | `decimal(8,2)` | **NO** | `-` | - | - |
| `Tax1Id` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Tax1Name` | `varchar(150)` | **NO** | `-` | - | - |
| `Tax1Percent` | `decimal(6,4)` | **NO** | `-` | - | - |
| `Tax2Id` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Tax2Name` | `varchar(150)` | **NO** | `-` | - | - |
| `Tax2Percent` | `decimal(6,4)` | **NO** | `-` | - | - |
| `Cost` | `decimal(20,4)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblInvoicingInvoiceLineItem`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `InvoiceId, Sequence`
