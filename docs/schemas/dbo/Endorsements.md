# Endorsements

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (13)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `EndorsementId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EndorsementTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `MakeId` | `uniqueidentifier` | YES | `-` | - | - |
| `ModelId` | `uniqueidentifier` | YES | `-` | - | - |
| `DateGiven` | `datetime(3)` | YES | `-` | - | - |
| `Expiration` | `datetime(3)` | YES | `-` | - | - |
| `Restrictions` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Certified` | `bit` | **NO** | `-` | - | - |
| `EndorsedByUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_Endorsements`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_Endorsements_EndorsementId`** (UNIQUE NONCLUSTERED)
  - Columns: `EndorsementId`
- **`ix_Endorsements_OperatorId_UserId_EndorsementTypeId`** (NONCLUSTERED)
  - Columns: `OperatorId, UserId, EndorsementTypeId`
