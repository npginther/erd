# tblAircraftDescriptions

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (13)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `PowerPlant` | `varchar(250)` | **NO** | `-` | - | - |
| `FlightInstruments` | `varchar(250)` | **NO** | `-` | - | - |
| `CockPit` | `varchar(250)` | **NO** | `-` | - | - |
| `Electrical` | `varchar(250)` | **NO** | `-` | - | - |
| `FuelSystem` | `varchar(250)` | **NO** | `-` | - | - |
| `LightingSystem` | `varchar(250)` | **NO** | `-` | - | - |
| `CabinComfort` | `varchar(250)` | **NO** | `-` | - | - |
| `GPS` | `varchar(250)` | **NO** | `-` | - | - |
| `OtherEquipment` | `varchar(250)` | **NO** | `-` | - | - |
| `Description` | `varchar(500)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_tblAircraftDescriptions`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AircraftId`
