# tblPostItemRoleIds

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `int(10,0)` | **NO** | `-` | PK | - |
| `PostItemId` | `int(10,0)` | **NO** | `-` | FK->`tblPostItems` | - |
| `RoleId` | `varchar(50)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblPostItems`** 
  via `PostItemId` → `ID` `ON DELETE CASCADE`

## Indexes

- **`IDX_tblPostItemRoleIds_PostItemId`** (NONCLUSTERED)
  - Columns: `PostItemId`
- **`PK_tblPostItemRoleIds`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
