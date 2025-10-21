# CustomTimeFields

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `CustomTimeFieldId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `FieldId` | `nvarchar(50)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(50)` | **NO** | `-` | - | - |
| `AircraftField` | `bit` | **NO** | `-` | - | - |
| `SimulatorField` | `bit` | **NO** | `-` | - | - |
| `IncludeInStandardTotal` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_CustomTimeFields_CustomTimeFieldId`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `CustomTimeFieldId`
- **`UK_CustomTimeFields_FieldId`** (UNIQUE NONCLUSTERED)
  - Columns: `FieldId`
- **`UK_CustomTimeFields_OperatorId_Name`** (UNIQUE NONCLUSTERED)
  - Columns: `OperatorId, Name`
