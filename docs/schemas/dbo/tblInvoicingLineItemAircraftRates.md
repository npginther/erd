# tblInvoicingLineItemAircraftRates

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (11)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `LineItemId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `AircraftRateTypeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `UnitCost` | `decimal(15,6)` | YES | `-` | - | - |
| `AccountingProductId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountingProductName` | `nvarchar(100)` | YES | `-` | - | - |
| `DoesNotApply` | `bit` | YES | `-` | - | - |
| `QBDAccountingProductId` | `nvarchar(200)` | YES | `-` | - | - |
| `QBDAccountingProductName` | `nvarchar(200)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblInvoicingLineItemAircraftRates`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`ix_OperatorId_DoesNotApply_Includes`** (NONCLUSTERED)
  - Columns: `OperatorId, DoesNotApply INCLUDE (AccountingProductId, AccountingProductName, AircraftRateTypeId, LineItemId)`
- **`ix_OperatorId_LineItemId_DoesNotApply_Includes`** (NONCLUSTERED)
  - Columns: `OperatorId, LineItemId, DoesNotApply INCLUDE (AccountingProductId, AccountingProductName, AircraftRateTypeId)`
