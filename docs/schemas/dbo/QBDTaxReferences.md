# QBDTaxReferences

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `Id` | `nvarchar(100)` | **NO** | `-` | - | - |
| `IsTaxable` | `bit` | **NO** | `-` | - | - |
| `IsActive` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_QBDTaxReferences`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
