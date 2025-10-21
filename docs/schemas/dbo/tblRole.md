# tblRole

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `RoleId` | `int(10,0)` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `RoleName` | `varchar(100)` | **NO** | `-` | - | - |
| `RoleOrder` | `int(10,0)` | **NO** | `-` | - | - |
| `RoleComment` | `varchar(2500)` | **NO** | `-` | - | - |
| `ReadOnly` | `bit` | **NO** | `-` | - | - |
| `LastUpdate` | `datetime(3)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.tblRolePermissionJoiner`** 
  via `RoleId` → `RoleId`
- **`dbo.tblUserRoleJoiner`** 
  via `RoleId` → `RoleId`
- **`dbo.LabelToRoleJoiner`** 
  via `RoleId` → `RoleId`

## Indexes

- **`IX_tblRole`** (UNIQUE NONCLUSTERED)
  - Columns: `CompanyId, RoleName`
- **`PK_tblRole`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `RoleId`
