# MaintenanceReminderResolutions

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (79)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ResolutionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `TemplateId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ReminderId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ResolvedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `ResolvedBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `DateBased` | `bit` | **NO** | `-` | - | - |
| `DateResolvedAt` | `datetime(3)` | YES | `-` | - | - |
| `TimeBased` | `bit` | **NO** | `-` | - | - |
| `TimeMeterBasedOn` | `int(10,0)` | YES | `-` | - | - |
| `TimeMeterTypeId` | `int(10,0)` | YES | `-` | - | - |
| `TimeMeterIndex` | `int(10,0)` | YES | `-` | - | - |
| `TimeResolvedAt` | `decimal(9,2)` | YES | `-` | - | - |
| `CycleBased` | `bit` | **NO** | `-` | - | - |
| `CyclesTypeId` | `int(10,0)` | YES | `-` | - | - |
| `CyclesIndex` | `int(10,0)` | YES | `-` | - | - |
| `CyclesResolvedAt` | `int(10,0)` | YES | `-` | - | - |
| `Hobbs` | `decimal(9,2)` | YES | `-` | - | - |
| `HeaterHobbs` | `decimal(9,2)` | YES | `-` | - | - |
| `Airtime` | `decimal(9,2)` | YES | `-` | - | - |
| `AircraftCycles` | `int(10,0)` | YES | `-` | - | - |
| `AirframeTTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine1Tach` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine1Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine1TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine1TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine1Prop1TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine1Prop1TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine2Tach` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine2Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine2TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine2TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine2Prop1TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine2Prop1TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine3Tach` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine3Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine3TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine3TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine3Prop1TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine3Prop1TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine4Tach` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine4Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine4TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine4TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine4Prop1TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine4Prop1TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine5Tach` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine5Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine5TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine5TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine5Prop1TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine5Prop1TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine6Tach` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine6Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine6TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine6TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine6Prop1TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine6Prop1TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine7Tach` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine7Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine7TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine7TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine7Prop1TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine7Prop1TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine8Tach` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine8Cycles` | `int(10,0)` | YES | `-` | - | - |
| `Engine8TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine8TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine8Prop1TTIS` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine8Prop1TSOH` | `decimal(9,2)` | YES | `-` | - | - |
| `CyclesResolvedAtDec` | `decimal(9,2)` | YES | `-` | - | - |
| `AircraftCyclesDec` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine1CyclesDec` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine2CyclesDec` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine3CyclesDec` | `decimal(9,2)` | YES | `-` | - | - |
| `Engine4CyclesDec` | `decimal(9,2)` | YES | `-` | - | - |
| `FlightTime` | `decimal(9,2)` | YES | `-` | - | - |

## Indexes

- **`PK_MaintenanceReminderResolutions`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_MaintenanceReminderResolutions_ResolutionId`** (UNIQUE NONCLUSTERED)
  - Columns: `ResolutionId`
