# tblInvoicingTaxes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (13)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `TaxId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Number` | `int(10,0)` | **NO** | `-` | - | - |
| `Description` | `varchar(150)` | **NO** | `-` | - | - |
| `Percent` | `decimal(6,4)` | **NO** | `-` | - | - |
| `VisibilityStatus` | `int(10,0)` | **NO** | `-` | - | - |
| `_TaxRowNumber` | `bigint(19,0)` | **NO** | `-` | - | - |
| `AccountingTaxId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountingTaxName` | `nvarchar(100)` | YES | `-` | - | - |
| `QBDAccountingTaxId` | `nvarchar(100)` | YES | `-` | - | - |
| `QBDAccountingTaxName` | `nvarchar(100)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblInvoicingTaxes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `TaxId`
