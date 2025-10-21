# Labels

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `LabelId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `LabelCategoryId` | `bigint(19,0)` | **NO** | `-` | FK->`LabelCategories` | - |
| `LabelGuid` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Name` | `nvarchar(50)` | **NO** | `-` | - | - |
| `IsActive` | `bit` | **NO** | `-` | - | - |
| `CreatedAtUtc` | `datetime2(7)` | **NO** | `-` | - | - |
| `LastModifiedAtUtc` | `datetime2(7)` | **NO** | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.LabelCategories`** 
  via `LabelCategoryId` → `LabelCategoryId` `ON DELETE CASCADE`

### Referenced By (Child Tables):

- **`dbo.LabelToRoleJoiner`** 
  via `LabelId` → `LabelId`
- **`dbo.LabelToUserJoiner`** 
  via `LabelId` → `LabelId`

## Indexes

- **`IX_Labels_LabelGuid_OperatorId`** (NONCLUSTERED)
  - Columns: `LabelGuid, OperatorId`
- **`PK_Labels`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `LabelId`
