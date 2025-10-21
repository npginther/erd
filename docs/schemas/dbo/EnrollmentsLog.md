# EnrollmentsLog

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ProductType` | `int(10,0)` | **NO** | `-` | - | - |
| `CurrentTime` | `datetime(3)` | **NO** | `-` | - | - |
| `Memo` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Data` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Completed` | `bit` | **NO** | `-` | - | - |
| `Quantity` | `int(10,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_EnrollmentsLog`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
