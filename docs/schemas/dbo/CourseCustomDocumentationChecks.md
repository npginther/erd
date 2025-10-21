# CourseCustomDocumentationChecks

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CustomDocumentationId` | `uniqueidentifier` | **NO** | `-` | - | - |

## Indexes

- **`PK_CourseCustomDocumentationChecks`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
