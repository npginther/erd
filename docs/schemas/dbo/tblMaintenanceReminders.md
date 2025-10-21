# tblMaintenanceReminders

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (17)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `ReminderId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Description` | `varchar(100)` | **NO** | `-` | - | - |
| `Notes` | `text(2147483647)` | **NO** | `-` | - | - |
| `IsOneTimeReminder` | `bit` | **NO** | `-` | - | - |
| `IsPermanentlyComplied` | `bit` | **NO** | `-` | - | - |
| `IsDateBasedReminder` | `bit` | **NO** | `-` | - | - |
| `IsTimeBasedReminder` | `bit` | **NO** | `-` | - | - |
| `IsCycleBasedReminder` | `bit` | **NO** | `-` | - | - |
| `ReminderInfo` | `varchar(750)` | **NO** | `-` | - | - |
| `DateWarningPeriod` | `int(10,0)` | YES | `-` | - | - |
| `TimeWarningPeriod` | `decimal(5,2)` | YES | `-` | - | - |
| `CanBeOverridden` | `bit` | **NO** | `-` | - | - |
| `CycleWarningPeriod` | `int(10,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblMaintenanceReminders`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `ReminderId`
- **`ix_tblMaintenanceReminders_CompanyId_AircraftId`** (NONCLUSTERED)
  - Columns: `CompanyId, AircraftId`
- **`ix_tblMaintenanceReminders_CompanyId_AircraftId_IsTimeBasedReminder`** (NONCLUSTERED)
  - Columns: `CompanyId, AircraftId, IsTimeBasedReminder`
