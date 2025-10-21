# Lessons

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (48)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PhaseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StageId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(150)` | **NO** | `-` | - | - |
| `Objectives` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `CompletionStandard` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Status` | `int(10,0)` | **NO** | `-` | - | - |
| `LessonGradeScaleId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `SessionGradingEnabled` | `bit` | **NO** | `-` | - | - |
| `SessionGradeScaleId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TrackedFieldsMode` | `int(10,0)` | **NO** | `-` | - | - |
| `TaskCount` | `int(10,0)` | **NO** | `-` | - | - |
| `LowestPassingLessonGradeId` | `uniqueidentifier` | YES | `-` | - | - |
| `RequiredStudy` | `nvarchar(MAX)` | YES | `-` | - | - |
| `InstructorNotes` | `nvarchar(MAX)` | YES | `-` | - | - |
| `RecommendedStudy` | `nvarchar(MAX)` | YES | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |
| `IsStageCheck` | `bit` | **NO** | `-` | - | - |
| `StageCheckRequiresPrerequisites` | `bit` | **NO** | `-` | - | - |
| `StageCheckBlocksProgression` | `bit` | **NO** | `-` | - | - |
| `StageCheckName` | `nvarchar(300)` | YES | `-` | - | - |
| `TrackExpectedCompletion` | `bit` | **NO** | `-` | - | - |
| `ExpectedCompletionInDays` | `int(10,0)` | YES | `-` | - | - |
| `ExternalId` | `nvarchar(50)` | YES | `-` | - | - |
| `ReservationTypeId` | `uniqueidentifier` | YES | `-` | - | - |
| `LessonType` | `int(10,0)` | YES | `-` | - | - |
| `IsInstructorRequired` | `bit` | **NO** | `-` | - | - |
| `FlightType` | `int(10,0)` | YES | `-` | - | - |
| `RouteType` | `int(10,0)` | YES | `-` | - | - |
| `Duration` | `int(10,0)` | YES | `-` | - | - |
| `FlightDuration` | `int(10,0)` | YES | `-` | - | - |
| `InstructorPreFlight` | `int(10,0)` | YES | `-` | - | - |
| `InstructorFlight` | `int(10,0)` | YES | `-` | - | - |
| `InstructorPostFlight` | `int(10,0)` | YES | `-` | - | - |
| `TimeOfDayRequirement` | `int(10,0)` | YES | `-` | - | - |
| `IsComplexAircraft` | `bit` | **NO** | `-` | - | - |
| `IsTAAAircraft` | `bit` | **NO** | `-` | - | - |
| `IsHighPerformanceAircraft` | `bit` | **NO** | `-` | - | - |
| `IsPressurizedAircraft` | `bit` | **NO** | `-` | - | - |
| `IsTailwheelAircraft` | `bit` | **NO** | `-` | - | - |
| `IsLSAAircraft` | `bit` | **NO** | `-` | - | - |
| `IsIFRAircraft` | `bit` | **NO** | `-` | - | - |
| `IsPart141Aircraft` | `bit` | **NO** | `-` | - | - |
| `SchedulingTemplateId` | `bigint(19,0)` | YES | `-` | - | - |

## Indexes

- **`PK_Lessons`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_Lessons_LessonId`** (UNIQUE NONCLUSTERED)
  - Columns: `LessonId`
- **`ix_Lessons_CourseId_OperatorId_Status`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId, Status`
- **`nci_msft_1_Lessons_AFD86E8DE4AE7C4D47CBD9C322998075`** (NONCLUSTERED)
  - Columns: `OperatorId, CourseId, Status INCLUDE (CompletionStandard, ExpectedCompletionInDays, ExternalId, InstructorNotes, IsLocked, IsStageCheck, LessonGradeScaleId, LessonId, LowestPassingLessonGradeId, Name, Objectives, Order, PhaseId, RecommendedStudy, RequiredStudy, SessionGradeScaleId, SessionGradingEnabled, StageCheckBlocksProgression, StageCheckName, StageCheckRequiresPrerequisites, StageId, TaskCount, TrackedFieldsMode, TrackExpectedCompletion)`
- **`nci_wi_Lessons_4180C49827CE7B12713F77D9D35BCF5E`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId, PhaseId, StageId INCLUDE (IsStageCheck, LessonGradeScaleId, LessonId, LowestPassingLessonGradeId, Name, Order, StageCheckBlocksProgression, StageCheckName, StageCheckRequiresPrerequisites, TrackedFieldsMode)`
- **`nci_wi_Lessons_6156E80F6607D6D9B51E9C5F501A421F`** (NONCLUSTERED)
  - Columns: `PhaseId, Order INCLUDE (IsLocked, LessonId, Name, Status, TaskCount)`
