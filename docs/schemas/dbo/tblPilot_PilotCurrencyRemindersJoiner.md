# tblPilot_PilotCurrencyRemindersJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `CompanyId` | `int(10,0)` | **NO** | `-` | PK | - |
| `ReminderId` | `int(10,0)` | **NO** | `-` | PK | - |
| `PilotId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `DateLastCompleted` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblPilot_PilotCurrencyRemindersJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `CompanyId, ReminderId, PilotId`
