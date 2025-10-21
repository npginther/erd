# CourseProfileLessonMinimumTimes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (8)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseProfileId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `MinimumTime1` | `decimal(5,2)` | YES | `-` | - | - |
| `MinimumTime2` | `decimal(5,2)` | YES | `-` | - | - |
| `MinimumTime3` | `decimal(5,2)` | YES | `-` | - | - |

## Indexes

- **`PK_CourseProfileLessonMinimumTimes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`nci_wi_CourseProfileLessonMinimumTimes_80202D01F3E3A2D3D680C85166399E4C`** (NONCLUSTERED)
  - Columns: `CourseProfileId, OperatorId, LessonId INCLUDE (MinimumTime1, MinimumTime2, MinimumTime3)`
