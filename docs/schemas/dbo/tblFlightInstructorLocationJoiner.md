# tblFlightInstructorLocationJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `FlightInstructorId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `LocationId` | `int(10,0)` | **NO** | `-` | PK | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`IDX_tblFlightInstructorLocationJoiner_LocationId`** (NONCLUSTERED)
  - Columns: `LocationId`
- **`PK_tblFlightInstructorLocationJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `FlightInstructorId, LocationId`
