# tblUserRoleJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `UserId` | `int(10,0)` | **NO** | `-` | PK | - |
| `RoleId` | `int(10,0)` | **NO** | `-` | PK<br/>FK->`tblRole` | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblRole`** 
  via `RoleId` → `RoleId` `ON DELETE CASCADE`

## Indexes

- **`IDX_tblUserRoleJoiner_RoleId_UserId`** (NONCLUSTERED)
  - Columns: `RoleId INCLUDE (UserId)`
- **`PK_tblUserRoleJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `UserId, RoleId`
