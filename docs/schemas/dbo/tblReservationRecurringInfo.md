# tblReservationRecurringInfo

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `RecurringId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Info` | `varchar(500)` | **NO** | `-` | - | - |
| `_RowId` | `bigint(19,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`CX_tblReservationRecurringInfo`** (UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`PK_tblReservationRecurringInfo`** (PRIMARY KEY UNIQUE NONCLUSTERED)
  - Columns: `RecurringId`
