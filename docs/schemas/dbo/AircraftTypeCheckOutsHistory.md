# AircraftTypeCheckOutsHistory

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (14)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `PerformedBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PerformedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `Mode` | `char(6)` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `AircraftTypeCheckoutId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PilotId` | `uniqueidentifier` | YES | `-` | - | - |
| `AircraftMakeId` | `uniqueidentifier` | YES | `-` | - | - |
| `AircraftModelId` | `uniqueidentifier` | YES | `-` | - | - |
| `CheckoutDate` | `datetime(3)` | YES | `-` | - | - |
| `Expiration` | `datetime(3)` | YES | `-` | - | - |
| `Revoked` | `bit` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_AircraftTypeCheckOutsHistory`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
