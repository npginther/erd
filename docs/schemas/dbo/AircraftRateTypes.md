# AircraftRateTypes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `AircraftRateTypeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `IsActive` | `bit` | **NO** | `-` | - | - |
| `IsDeleted` | `bit` | **NO** | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `InvoicingAccountId` | `uniqueidentifier` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_AircraftRateTypes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
