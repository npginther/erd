# ReservationInvoices

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `InvoiceId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `InvoiceStatus` | `int(10,0)` | YES | `-` | - | - |
| `InvoiceNumber` | `int(10,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_ReservationInvoices`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`dbo.IDX_ReservationInvoices_ReservationId`** (NONCLUSTERED)
  - Columns: `ReservationId INCLUDE (_RowNumber, InvoiceId, OperatorId)`
