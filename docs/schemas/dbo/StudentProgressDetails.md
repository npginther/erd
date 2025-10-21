# StudentProgressDetails

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (37)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `Date` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseProfileId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | YES | `-` | - | - |
| `LessonName` | `nvarchar(150)` | YES | `-` | - | - |
| `LessonCompleted` | `bit` | YES | `-` | - | - |
| `TrainingSessionId` | `uniqueidentifier` | YES | `-` | - | - |
| `TrainingDayNumber` | `int(10,0)` | YES | `-` | - | - |
| `AvailableTrainingDay` | `int(10,0)` | YES | `-` | - | - |
| `LessonCompletionPercent` | `decimal(7,2)` | YES | `-` | - | - |
| `LessonCompletionPercentVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `LessonCompletionVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `LessonStatus` | `int(10,0)` | YES | `-` | - | - |
| `LessonsCompletedCount` | `int(10,0)` | YES | `-` | - | - |
| `TimeField1Id` | `nvarchar(50)` | YES | `-` | - | - |
| `TimeField1Value` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField1CompletionPercent` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField1CompletionPercentVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField1CompletionVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField1Status` | `int(10,0)` | YES | `-` | - | - |
| `TimeField2Id` | `nvarchar(50)` | YES | `-` | - | - |
| `TimeField2Value` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField2CompletionPercent` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField2CompletionPercentVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField2CompletionVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField2Status` | `int(10,0)` | YES | `-` | - | - |
| `TimeField3Id` | `nvarchar(50)` | YES | `-` | - | - |
| `TimeField3Value` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField3CompletionPercent` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField3CompletionPercentVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField3CompletionVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `TimeField3Status` | `int(10,0)` | YES | `-` | - | - |
| `OverallProgressStatus` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_StudentProgressDetails`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`nci_wi_StudentProgressDetails_E59E28FD8F16D86FEDF0629E51D00702`** (NONCLUSTERED)
  - Columns: `EnrollmentId, OperatorId INCLUDE (AvailableTrainingDay, CourseId, CourseProfileId, Date, LessonCompleted, LessonCompletionPercent, LessonCompletionPercentVariance, LessonCompletionVariance, LessonId, LessonName, LessonsCompletedCount, LessonStatus, OverallProgressStatus, StudentId, TimeField1CompletionPercent, TimeField1CompletionPercentVariance, TimeField1CompletionVariance, TimeField1Id, TimeField1Status, TimeField1Value, TimeField2CompletionPercent, TimeField2CompletionPercentVariance, TimeField2CompletionVariance, TimeField2Id, TimeField2Status, TimeField2Value, TimeField3CompletionPercent, TimeField3CompletionPercentVariance, TimeField3CompletionVariance, TimeField3Id, TimeField3Status, TimeField3Value, TrainingDayNumber, TrainingSessionId)`
