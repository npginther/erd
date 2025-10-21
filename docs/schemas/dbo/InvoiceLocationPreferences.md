# InvoiceLocationPreferences

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `LocationId` | `int(10,0)` | **NO** | `-` | - | - |
| `Phone` | `nvarchar(50)` | YES | `-` | - | - |
| `Address` | `nvarchar(500)` | YES | `-` | - | - |
| `Email` | `nvarchar(150)` | YES | `-` | - | - |
| `AdditionalInformation` | `nvarchar(MAX)` | YES | `-` | - | - |
| `DefaultInvoiceMessage` | `nvarchar(MAX)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_InvoiceLocationPreferences`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
