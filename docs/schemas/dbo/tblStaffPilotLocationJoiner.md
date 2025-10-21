# tblStaffPilotLocationJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Counter` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `UserGUIDid` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `LocationId` | `int(10,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IX_tblStaffPilotLocationJoiner`** (UNIQUE NONCLUSTERED)
  - Columns: `UserGUIDid, CompanyId, LocationId`
- **`PK_tblStaffPilotLocationJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Counter`
