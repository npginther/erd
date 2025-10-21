# tblAircraftTach

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `TachCount` | `int(10,0)` | **NO** | `-` | PK | - |
| `Tach` | `decimal(9,2)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_tblAircraftTach`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AircraftId, TachCount`
