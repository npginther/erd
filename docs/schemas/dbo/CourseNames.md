# CourseNames

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `TimeStamp` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `SyllabusProviderId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_CourseNames`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`UK_CourseNames_OperatorId_CourseId`** (UNIQUE NONCLUSTERED)
  - Columns: `OperatorId, CourseId`
