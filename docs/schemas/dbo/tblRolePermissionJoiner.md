# tblRolePermissionJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `RoleId` | `int(10,0)` | **NO** | `-` | PK<br/>FK->`tblRole` | - |
| `PermissionId` | `int(10,0)` | **NO** | `-` | PK | - |
| `PermissionTypeId` | `int(10,0)` | **NO** | `-` | PK | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblRole`** 
  via `RoleId` → `RoleId` `ON DELETE CASCADE`

## Indexes

- **`PK_tblRolePermissionJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `RoleId, PermissionId, PermissionTypeId`
