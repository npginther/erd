# EnrollmentCreditPreviousTotals

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `FieldId` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Value` | `decimal(9,2)` | YES | `-` | - | - |

## Indexes

- **`PK_EnrollmentCreditPreviousTotals`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`nci_wi_EnrollmentCreditPreviousTotals_EA93683341CC50D25975B2140147BD5E`** (NONCLUSTERED)
  - Columns: `OperatorId, EnrollmentId, Value INCLUDE (FieldId)`
