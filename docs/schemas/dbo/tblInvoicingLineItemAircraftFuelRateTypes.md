# tblInvoicingLineItemAircraftFuelRateTypes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `LineItemId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `AircraftRateTypeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblInvoicingLineItemAircraftFuelRateTypes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
