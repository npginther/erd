# QBDCustomers

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (15)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Id` | `nvarchar(100)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `FirstName` | `nvarchar(50)` | YES | `-` | - | - |
| `LastName` | `nvarchar(50)` | YES | `-` | - | - |
| `MiddleInitial` | `nvarchar(50)` | YES | `-` | - | - |
| `CompanyName` | `nvarchar(100)` | YES | `-` | - | - |
| `MainEmail` | `nvarchar(100)` | YES | `-` | - | - |
| `MainPhone` | `nvarchar(25)` | YES | `-` | - | - |
| `TaxReferenceId` | `nvarchar(100)` | YES | `-` | - | - |
| `SalesTaxId` | `nvarchar(100)` | YES | `-` | - | - |
| `IsActive` | `bit` | **NO** | `-` | - | - |
| `Balance` | `decimal(11,2)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_QBDCustomers`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
