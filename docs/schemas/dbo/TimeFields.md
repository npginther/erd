# TimeFields

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (12)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `nvarchar(50)` | **NO** | `-` | PK | - |
| `Name` | `nvarchar(150)` | **NO** | `-` | - | - |
| `ValueType` | `nvarchar(5)` | **NO** | `-` | - | - |
| `InputField` | `bit` | **NO** | `-` | - | - |
| `EnabledByDefault` | `bit` | **NO** | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `UniversalField` | `bit` | **NO** | `-` | - | - |
| `AircraftField` | `bit` | **NO** | `-` | - | - |
| `SimulatorField` | `bit` | **NO** | `-` | - | - |
| `IsLandingField` | `bit` | **NO** | `-` | - | - |
| `MaxVersion` | `int(10,0)` | YES | `-` | - | - |
| `MinVersion` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_TimeFields`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
