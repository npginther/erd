# tblAircraft_AircraftGroupJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `AircraftGroupId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_tblAircraft_AircraftGroupJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AircraftId, AircraftGroupId`
