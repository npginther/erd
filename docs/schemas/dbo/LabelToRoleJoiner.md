# LabelToRoleJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `LabelId` | `bigint(19,0)` | **NO** | `-` | PK<br/>FK->`Labels` | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | PK | - |
| `RoleId` | `int(10,0)` | **NO** | `-` | PK<br/>FK->`tblRole` | - |
| `CreatedAtUtc` | `datetime2(7)` | **NO** | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.Labels`** 
  via `LabelId` → `LabelId` `ON DELETE CASCADE`
- **`dbo.tblRole`** 
  via `RoleId` → `RoleId` `ON DELETE CASCADE`

## Indexes

- **`IX_LabelToRoleJoiner_LabelId_OperatorId`** (NONCLUSTERED)
  - Columns: `LabelId, OperatorId`
- **`IX_LabelToRoleJoiner_RoleId_OperatorId`** (NONCLUSTERED)
  - Columns: `RoleId, OperatorId`
- **`PK_LabelToRoleJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `LabelId, OperatorId, RoleId`
