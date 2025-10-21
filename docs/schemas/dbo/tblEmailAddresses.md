# tblEmailAddresses

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (8)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `int(10,0)` | **NO** | `-` | PK | - |
| `EmailAddress` | `varchar(64)` | YES | `-` | - | - |
| `IsPrimary` | `bit` | **NO** | `-` | - | - |
| `IsConfirmed` | `bit` | **NO** | `-` | - | - |
| `GUID` | `uniqueidentifier` | YES | `-` | - | - |
| `IsSMSAddress` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`IsConfirmed`** (NONCLUSTERED)
  - Columns: `IsConfirmed`
- **`IsPrimary`** (NONCLUSTERED)
  - Columns: `IsPrimary`
- **`PK_tblEmailAddresses`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
