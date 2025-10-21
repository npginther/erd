# LabelCategories

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `LabelCategoryId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `LabelCategoryGuid` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Name` | `nvarchar(50)` | **NO** | `-` | - | - |
| `BackgroundColor` | `nvarchar(7)` | **NO** | `-` | - | - |
| `ForegroundColor` | `nvarchar(7)` | **NO** | `-` | - | - |
| `Type` | `int(10,0)` | **NO** | `-` | - | - |
| `CreatedAtUtc` | `datetime2(7)` | **NO** | `-` | - | - |
| `LastModifiedAtUtc` | `datetime2(7)` | **NO** | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.Labels`** 
  via `LabelCategoryId` → `LabelCategoryId`

## Indexes

- **`IX_LabelCategories_LabelCategoryGuid_OperatorId`** (NONCLUSTERED)
  - Columns: `LabelCategoryGuid, OperatorId`
- **`PK_LabelCategories`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `LabelCategoryId`
