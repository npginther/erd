# PhotoIds

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `PhotoIdId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PhotoIdType` | `int(10,0)` | **NO** | `-` | - | - |
| `PhotoIdNumber` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Expires` | `bit` | **NO** | `-` | - | - |
| `ExpirationDate` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_PhotoIds`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
