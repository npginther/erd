# EndorsementsHistory

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (17)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `PerformedBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PerformedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `Mode` | `char(6)` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `EndorsementId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | YES | `-` | - | - |
| `EndorsementTypeId` | `int(10,0)` | YES | `-` | - | - |
| `MakeId` | `uniqueidentifier` | YES | `-` | - | - |
| `ModelId` | `uniqueidentifier` | YES | `-` | - | - |
| `DateGiven` | `datetime(3)` | YES | `-` | - | - |
| `Expiration` | `datetime(3)` | YES | `-` | - | - |
| `Restrictions` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Certified` | `bit` | YES | `-` | - | - |
| `EndorsedByUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_EndorsementsHistory`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
