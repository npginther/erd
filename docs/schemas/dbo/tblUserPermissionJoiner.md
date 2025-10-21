# tblUserPermissionJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `UserId` | `int(10,0)` | **NO** | `-` | PK | - |
| `PermissionId` | `int(10,0)` | **NO** | `-` | PK | - |
| `PermissionTypeId` | `int(10,0)` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | PK | - |
| `Allow` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_tblUserPermissionJoiner_PermissionIdCompanyId_UserIdPermissionTypeIdAllow`** (NONCLUSTERED)
  - Columns: `PermissionId, CompanyId INCLUDE (Allow, PermissionTypeId, UserId)`
- **`PK_tblUserPermissionJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `UserId, PermissionId, PermissionTypeId, CompanyId`
