# CustomSquawkResolutions

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (8)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `id` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CustomSquawkResolutionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Resolution` | `nvarchar(100)` | YES | `-` | - | - |
| `IsDeleted` | `bit` | **NO** | `-` | - | - |
| `ResolvesGroundableSquawk` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_CustomSquawkResolutions`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `id`
- **`dbo.IDX_CustomSquawkResolutions_CustomSquawkResolutionId_ResolvesGroundableSquawk`** (NONCLUSTERED)
  - Columns: `CustomSquawkResolutionId INCLUDE (ResolvesGroundableSquawk)`
