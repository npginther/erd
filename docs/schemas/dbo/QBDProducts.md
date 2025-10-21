# QBDProducts

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
| `Id` | `nvarchar(100)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `Description` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Price` | `decimal(15,6)` | **NO** | `-` | - | - |
| `AccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `SalesTaxId` | `nvarchar(100)` | YES | `-` | - | - |
| `TaxReferenceId` | `nvarchar(100)` | YES | `-` | - | - |
| `IsActive` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_QBDProducts`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
