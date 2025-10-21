# Headings

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `HeadingId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PartId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`IDX_Headings_LessonId`** (NONCLUSTERED)
  - Columns: `LessonId`
- **`PK_Headings`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_Headings_HeadingId`** (UNIQUE NONCLUSTERED)
  - Columns: `HeadingId`
- **`nci_wi_Headings_B9A95A336CDE3A7CB133E66714625055`** (NONCLUSTERED)
  - Columns: `PartId, CourseId, OperatorId, LessonId INCLUDE (HeadingId, IsLocked, Name, Order)`
- **`nci_wi_Headings_D925C8F98F1EFE6EB89336765BA35BD2`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId INCLUDE (HeadingId, LessonId, Name, Order)`
