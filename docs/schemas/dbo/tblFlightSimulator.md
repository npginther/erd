# tblFlightSimulator

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `FlightSimulatorId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `varchar(100)` | **NO** | `-` | - | - |
| `Description` | `varchar(250)` | **NO** | `-` | - | - |
| `LocationId` | `int(10,0)` | **NO** | `-` | - | - |
| `IsActive` | `bit` | **NO** | `-` | - | - |
| `ScheduleOrder` | `int(10,0)` | **NO** | `-` | - | - |
| `IsDeleted` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblFlightSimulator`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `FlightSimulatorId`
