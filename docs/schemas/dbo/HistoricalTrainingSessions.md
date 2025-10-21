# HistoricalTrainingSessions

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (45)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | YES | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | YES | `-` | - | - |
| `TrainingSessionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `HistoricalTrainingSessionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `InstructorId` | `uniqueidentifier` | YES | `-` | - | - |
| `SessionType` | `int(10,0)` | **NO** | `-` | - | - |
| `SessionGradeId` | `uniqueidentifier` | YES | `-` | - | - |
| `Remarks` | `nvarchar(MAX)` | YES | `-` | - | - |
| `IsDraft` | `bit` | **NO** | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | YES | `-` | - | - |
| `AircraftMake` | `nvarchar(100)` | YES | `-` | - | - |
| `AircraftModel` | `nvarchar(100)` | YES | `-` | - | - |
| `AircraftTailNumber` | `nvarchar(25)` | YES | `-` | - | - |
| `AircraftClass` | `char(5)` | YES | `-` | - | - |
| `IsComplex` | `bit` | YES | `-` | - | - |
| `IsHighPerformance` | `bit` | YES | `-` | - | - |
| `IsTailWheel` | `bit` | YES | `-` | - | - |
| `CreatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `StudentSigned` | `bit` | **NO** | `-` | - | - |
| `StudentSignedAt` | `datetime(3)` | YES | `-` | - | - |
| `StudentSignatureType` | `int(10,0)` | YES | `-` | - | - |
| `InstructorSigned` | `bit` | **NO** | `-` | - | - |
| `InstructorSignedAt` | `datetime(3)` | YES | `-` | - | - |
| `InstructorSignatureType` | `int(10,0)` | YES | `-` | - | - |
| `LessonGradeId` | `uniqueidentifier` | YES | `-` | - | - |
| `SessionDate` | `datetime(3)` | YES | `-` | - | - |
| `IsFirstSession` | `bit` | **NO** | `-` | - | - |
| `AwaitingSignature` | `bit` | **NO** | `-` | - | - |
| `ReservationId` | `uniqueidentifier` | YES | `-` | - | - |
| `ReservationNumber` | `bigint(19,0)` | YES | `-` | - | - |
| `PeopleGroupId` | `uniqueidentifier` | YES | `-` | - | - |
| `PeopleGroupName` | `nvarchar(400)` | YES | `-` | - | - |
| `IsMassSession` | `bit` | **NO** | `-` | - | - |
| `ParentTrainingSessionId` | `uniqueidentifier` | YES | `-` | - | - |
| `CertifyingUserSigned` | `bit` | **NO** | `-` | - | - |
| `CertifyingUserSignedAt` | `datetime(3)` | YES | `-` | - | - |
| `CertifyingUserSignatureType` | `int(10,0)` | YES | `-` | - | - |
| `CertifyingUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `IsTAA` | `bit` | YES | `-` | - | - |
| `LessonAttemptCount` | `int(10,0)` | YES | `-` | - | - |
| `LoggedAt` | `datetime(3)` | YES | `-` | - | - |

## Indexes

- **`IX_HistoricalTrainingSessions_OperatorIdTrainingSessionId_LoggedAt`** (NONCLUSTERED)
  - Columns: `OperatorId, TrainingSessionId INCLUDE (LoggedAt)`
- **`PK_HistoricalTrainingSessions`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_HistoricalTrainingSessions_HistoricalTrainingSessionId`** (UNIQUE NONCLUSTERED)
  - Columns: `HistoricalTrainingSessionId`
