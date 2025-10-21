# MaintenanceReminders

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (47)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ReminderId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `TemplateId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OneTime` | `bit` | **NO** | `-` | - | - |
| `PermanentlyComplied` | `bit` | **NO** | `-` | - | - |
| `ReminderStatus` | `int(10,0)` | **NO** | `-` | - | - |
| `DateLastCompleted` | `datetime(3)` | YES | `-` | - | - |
| `DateDueAt` | `datetime(3)` | YES | `-` | - | - |
| `DateStatus` | `int(10,0)` | YES | `-` | - | - |
| `DateDaysUntilExpiration` | `int(10,0)` | YES | `-` | - | - |
| `DateExpirationDate` | `datetime(3)` | YES | `-` | - | - |
| `DateCurrently` | `datetime(3)` | YES | `-` | - | - |
| `DateMessage` | `nvarchar(200)` | YES | `-` | - | - |
| `TimeMeterBasedOn` | `int(10,0)` | YES | `-` | - | - |
| `TimeMeterTypeId` | `int(10,0)` | YES | `-` | - | - |
| `TimeMeterIndex` | `int(10,0)` | YES | `-` | - | - |
| `TimeLastCompleted` | `decimal(9,2)` | YES | `-` | - | - |
| `TimeDueAt` | `decimal(9,2)` | YES | `-` | - | - |
| `TimeStatus` | `int(10,0)` | YES | `-` | - | - |
| `TimeHoursToExpiration` | `decimal(9,2)` | YES | `-` | - | - |
| `TimeCurrently` | `decimal(9,2)` | YES | `-` | - | - |
| `TimeMessage` | `nvarchar(200)` | YES | `-` | - | - |
| `CyclesTypeId` | `int(10,0)` | YES | `-` | - | - |
| `CyclesIndex` | `int(10,0)` | YES | `-` | - | - |
| `CyclesLastCompleted` | `int(10,0)` | YES | `-` | - | - |
| `CyclesDueAt` | `int(10,0)` | YES | `-` | - | - |
| `CyclesStatus` | `int(10,0)` | YES | `-` | - | - |
| `CyclesToExpiration` | `int(10,0)` | YES | `-` | - | - |
| `CyclesCurrently` | `int(10,0)` | YES | `-` | - | - |
| `CyclesMessage` | `nvarchar(200)` | YES | `-` | - | - |
| `CreatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `UpdatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `Active` | `bit` | **NO** | `-` | - | - |
| `Stale` | `bit` | **NO** | `-` | - | - |
| `Misconfigured` | `bit` | **NO** | `-` | - | - |
| `CyclesLastCompletedDec` | `decimal(9,2)` | YES | `-` | - | - |
| `CyclesDueAtDec` | `decimal(9,2)` | YES | `-` | - | - |
| `CyclesToExpirationDec` | `decimal(9,2)` | YES | `-` | - | - |
| `CyclesCurrentlyDec` | `decimal(9,2)` | YES | `-` | - | - |
| `DateSuggestedDueAt` | `datetime(3)` | YES | `-` | - | - |
| `TimeSuggestedDueAt` | `decimal(9,2)` | YES | `-` | - | - |
| `CyclesSuggestedDueAt` | `decimal(9,2)` | YES | `-` | - | - |
| `DateDueOverride` | `datetime(3)` | YES | `-` | - | - |
| `TimeDueOverride` | `decimal(9,2)` | YES | `-` | - | - |
| `CyclesDueOverride` | `decimal(9,2)` | YES | `-` | - | - |

## Indexes

- **`PK_MaintenanceReminders`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_MaintenanceReminders`** (UNIQUE NONCLUSTERED)
  - Columns: `OperatorId, ReminderId`
- **`ix_OperatorId_Active_ReminderStatus_Includes`** (NONCLUSTERED)
  - Columns: `OperatorId, Active, ReminderStatus INCLUDE (AircraftId)`
- **`ix_OperatorId_Active_ReminderStatus_Includes_TemplateID_AircraftID`** (NONCLUSTERED)
  - Columns: `OperatorId, Active, ReminderStatus INCLUDE (AircraftId, TemplateId)`
- **`ix_OperatorId_AircraftId_Active_Includes`** (NONCLUSTERED)
  - Columns: `OperatorId, AircraftId, Active INCLUDE (ReminderStatus, TemplateId)`
- **`ix_OperatorId_TemplateId_Active_Misconfigured`** (NONCLUSTERED)
  - Columns: `OperatorId, TemplateId, Active, Misconfigured`
