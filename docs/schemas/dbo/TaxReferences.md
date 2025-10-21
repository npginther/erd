# TaxReferences

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (12)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `TaxReferenceId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `Taxable` | `bit` | **NO** | `-` | - | - |
| `Active` | `bit` | **NO** | `-` | - | - |
| `Deleted` | `bit` | **NO** | `-` | - | - |
| `AccountingTaxReferenceId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountingTaxReferenceName` | `nvarchar(100)` | YES | `-` | - | - |
| `QBDAccountingTaxReferenceId` | `nvarchar(200)` | YES | `-` | - | - |
| `QBDAccountingTaxReferenceName` | `nvarchar(200)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_TaxReferences`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
