# OperatorAirportIdentifiers

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (3)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `AirportId` | `nvarchar(10)` | **NO** | `-` | - | - |

## Indexes

- **`PK_OperatorAirportIdentifiers`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_OperatorAirportIdentifiers_OperatorIdAirportId`** (UNIQUE NONCLUSTERED)
  - Columns: `OperatorId, AirportId`
