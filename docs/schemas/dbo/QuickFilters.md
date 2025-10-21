# QuickFilters

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Filter` | `nvarchar(MAX)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_QuickFilters`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `RowId`
- **`UK_QuickFilters_CompanyId_UserId`** (UNIQUE NONCLUSTERED)
  - Columns: `CompanyId, UserId`
