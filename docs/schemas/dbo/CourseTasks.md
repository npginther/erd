# CourseTasks

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CourseTaskId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(2000)` | **NO** | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`IDX_CourseTasks_CourseId_OperatorId`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId INCLUDE (CourseTaskId, Name)`
- **`PK_CourseTasks`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_CourseTasks_CourseId_Name`** (UNIQUE NONCLUSTERED)
  - Columns: `CourseId, Name`
- **`UK_CourseTasks_CourseTaskId`** (UNIQUE NONCLUSTERED)
  - Columns: `CourseTaskId`
- **`nci_wi_CourseTasks_59770F95B69E3137CCFDFE44E9E13B51`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId, Name INCLUDE (CourseTaskId, IsLocked)`
- **`nci_wi_CourseTasks_BA04E2824C81C30B0D9E7FBC9EA98383`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId INCLUDE (CourseTaskId, IsLocked, Name)`
