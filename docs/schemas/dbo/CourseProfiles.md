# CourseProfiles

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (17)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseProfileId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Name` | `nvarchar(50)` | **NO** | `-` | - | - |
| `LessonPerSevenDays` | `decimal(5,2)` | **NO** | `-` | - | - |
| `NonControlledCancellationIsTraining` | `bit` | **NO** | `-` | - | - |
| `LessonCompletionStatusBehind` | `int(10,0)` | **NO** | `-` | - | - |
| `LessonCompletionStatusAtRisk` | `int(10,0)` | **NO** | `-` | - | - |
| `LessonCompletionStatusOnTrack` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseMinimumTimeField1` | `nvarchar(50)` | YES | `-` | - | - |
| `CourseMinimumTimeField2` | `nvarchar(50)` | YES | `-` | - | - |
| `CourseMinimumTimeField3` | `nvarchar(50)` | YES | `-` | - | - |
| `CourseMinimumStatusBehind` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseMinimumStatusAtRiskLow` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseMinimumStatusOnTrack` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseMinimumStatusAtRiskHigh` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_CourseProfiles`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`nci_wi_CourseProfiles_679768DD3C431977B5111343BA73A2F5`** (NONCLUSTERED)
  - Columns: `CourseProfileId, OperatorId INCLUDE (CourseMinimumTimeField1, CourseMinimumTimeField2, CourseMinimumTimeField3, Name)`
