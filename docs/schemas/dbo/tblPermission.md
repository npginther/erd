# tblPermission

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PermissionTypeId` | `int(10,0)` | **NO** | `-` | PK | - |
| `PermissionValue` | `int(10,0)` | **NO** | `-` | PK | - |
| `Description` | `varchar(500)` | **NO** | `-` | - | - |
| `Grouping` | `varchar(50)` | **NO** | `-` | - | - |
| `Category` | `varchar(50)` | **NO** | `-` | - | - |
| `Title` | `varchar(50)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblPermission`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PermissionTypeId, PermissionValue`
