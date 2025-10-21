# tblEngine

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (22)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `EngineId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Description` | `varchar(250)` | **NO** | `-` | - | - |
| `SerialNumber` | `varchar(100)` | **NO** | `-` | - | - |
| `IsTurbine` | `bit` | **NO** | `-` | - | - |
| `IsProp` | `bit` | **NO** | `-` | - | - |
| `LastMOHTime` | `decimal(9,2)` | YES | `-` | - | - |
| `LastMOHDate` | `datetime(3)` | YES | `-` | - | - |
| `TBOHours` | `decimal(9,2)` | YES | `-` | - | - |
| `HasTachMeter` | `bit` | **NO** | `-` | - | - |
| `TachMeter` | `decimal(9,2)` | **NO** | `-` | - | - |
| `CurrentTimeAdjustment` | `decimal(9,2)` | **NO** | `-` | - | - |
| `CurrentTimeMeterType` | `int(10,0)` | **NO** | `-` | - | - |
| `CurrentTimeMeterIndex` | `int(10,0)` | **NO** | `-` | - | - |
| `CurrentTime` | `decimal(9,2)` | YES | `-` | - | - |
| `TrackCycles` | `bit` | **NO** | `-` | - | - |
| `CurrentCycles` | `int(10,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `TSOHAdjustment` | `decimal(9,2)` | YES | `-` | - | - |
| `EngineCycles` | `decimal(9,2)` | YES | `-` | - | - |
| `TSOH` | `decimal(9,2)` | YES | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.tblEnginePropellerJoiner`** 
  via `EngineId` → `EngineId`

## Indexes

- **`PK_tblEngine`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `EngineId`
