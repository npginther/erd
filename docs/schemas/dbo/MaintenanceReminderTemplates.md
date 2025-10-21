# MaintenanceReminderTemplates

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (24)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `TemplateId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(150)` | **NO** | `-` | - | - |
| `Active` | `bit` | **NO** | `-` | - | - |
| `OneTime` | `bit` | **NO** | `-` | - | - |
| `Overrideable` | `bit` | **NO** | `-` | - | - |
| `MaintenanceOnly` | `bit` | **NO** | `-` | - | - |
| `Notes` | `nvarchar(MAX)` | **NO** | `-` | - | - |
| `DateBased` | `bit` | **NO** | `-` | - | - |
| `DateDueEvery` | `int(10,0)` | YES | `-` | - | - |
| `DateRecurrencePeriod` | `int(10,0)` | YES | `-` | - | - |
| `DateDueAtEndOfMonth` | `bit` | YES | `-` | - | - |
| `DateWarningPeriod` | `int(10,0)` | YES | `-` | - | - |
| `TimeBased` | `bit` | **NO** | `-` | - | - |
| `TimeDueEvery` | `decimal(9,2)` | YES | `-` | - | - |
| `TimeWarningPeriod` | `decimal(9,2)` | YES | `-` | - | - |
| `CyclesBased` | `bit` | **NO** | `-` | - | - |
| `CyclesDuesEvery` | `int(10,0)` | YES | `-` | - | - |
| `CyclesWarningPeriod` | `int(10,0)` | YES | `-` | - | - |
| `CreatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `UpdatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `CyclesDueEveryDec` | `decimal(9,2)` | YES | `-` | - | - |
| `CyclesWarningPeriodDec` | `decimal(9,2)` | YES | `-` | - | - |

## Indexes

- **`PK_MaintenanceReminderTemplates`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_MaintenanceReminderTemplates`** (UNIQUE NONCLUSTERED)
  - Columns: `TemplateId, OperatorId`
