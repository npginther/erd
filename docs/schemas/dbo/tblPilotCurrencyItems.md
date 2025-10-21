# tblPilotCurrencyItems

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `int(10,0)` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `ReminderId` | `int(10,0)` | **NO** | `-` | - | - |
| `DateLastCompleted` | `datetime(3)` | YES | `-` | - | - |
| `PilotId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblPilotCurrencyItems`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
