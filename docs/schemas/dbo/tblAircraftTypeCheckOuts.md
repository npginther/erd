# tblAircraftTypeCheckOuts

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (11)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PilotId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `AircraftMakeId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `AircraftModelId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CheckoutDate` | `datetime(3)` | **NO** | `-` | - | - |
| `UserWhoApprovedId` | `int(10,0)` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Id` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Expiration` | `datetime(3)` | YES | `-` | - | - |
| `Revoked` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblAircraftTypeCheckOuts`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PilotId, AircraftMakeId, AircraftModelId`
