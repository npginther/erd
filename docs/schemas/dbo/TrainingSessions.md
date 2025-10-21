# TrainingSessions

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (44)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | YES | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | YES | `-` | - | - |
| `TrainingSessionId` | `uniqueidentifier` | **NO** | `-` | - | - |
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

- **`IDX_TrainingSessions_IsDraft_OperatorId_CourseId_EnrollmentId_LessonId_StudentId_TrainingSessionId`** (NONCLUSTERED)
  - Columns: `IsDraft, OperatorId, CourseId, EnrollmentId, LessonId, StudentId, TrainingSessionId INCLUDE (AircraftClass, IsComplex, IsHighPerformance, IsTailWheel, SessionDate)`
- **`IX_TrainingSessions_OperatorIdParentTrainingSessionId`** (NONCLUSTERED)
  - Columns: `OperatorId, ParentTrainingSessionId`
- **`PK_TrainingSessions`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_TrainingSessions_TrainingSessionId`** (UNIQUE NONCLUSTERED)
  - Columns: `TrainingSessionId`
- **`ix_TrainingSessions_OperatorId_IsDraft`** (NONCLUSTERED)
  - Columns: `OperatorId, IsDraft INCLUDE (TrainingSessionId, AircraftClass, IsComplex, IsHighPerformance, IsTailWheel, IsTAA)`
- **`ix_TrainingSessions_OperatorId_ReservationId`** (NONCLUSTERED)
  - Columns: `OperatorId, ReservationId`
- **`nci_msft_1_TrainingSessions_80E4436F35BAE52F6D5CCA7EDFD75B78`** (NONCLUSTERED)
  - Columns: `EnrollmentId, OperatorId, StudentId, IsDraft INCLUDE (LessonGradeId, LessonId)`
- **`nci_wi_TrainingSessions_180A8812528E00E9F75D09BF7650500F`** (NONCLUSTERED)
  - Columns: `AwaitingSignature, EnrollmentId, LessonId`
- **`nci_wi_TrainingSessions_2E26AF973D4B09C14F6EA1E13AFCA86C`** (NONCLUSTERED)
  - Columns: `IsDraft, OperatorId INCLUDE (AircraftClass, IsComplex, IsHighPerformance, IsTAA, IsTailWheel, TrainingSessionId)`
- **`nci_wi_TrainingSessions_41B1F19ACAD7D3000E1476C2B7093147`** (NONCLUSTERED)
  - Columns: `EnrollmentId, OperatorId, IsDraft INCLUDE (AircraftId, CertifyingUserSigned, CertifyingUserSignedAt, InstructorId, InstructorSigned, InstructorSignedAt, LessonGradeId, LessonId, Remarks, SessionDate, SessionGradeId, StudentSigned, StudentSignedAt, TrainingSessionId)`
- **`nci_wi_TrainingSessions_420053F31F6E0D51E84CC133A0BFFBB8`** (NONCLUSTERED)
  - Columns: `IsDraft, OperatorId, ReservationId INCLUDE (AircraftClass, IsComplex, IsHighPerformance, IsTAA, IsTailWheel, TrainingSessionId)`
- **`nci_wi_TrainingSessions_6A7F9B792B0BE0E91266FE5E33307F21`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId, EnrollmentId, LessonId, StudentId, SessionDate, TrainingSessionId INCLUDE (AwaitingSignature, IsDraft, LessonAttemptCount, LessonGradeId, ReservationId)`
- **`nci_wi_TrainingSessions_93CFDB91A60D739764E8598AA3568630`** (NONCLUSTERED)
  - Columns: `IsDraft, OperatorId, EnrollmentId, LessonId, TrainingSessionId INCLUDE (AircraftClass, AircraftId, AircraftMake, AircraftModel, AircraftTailNumber, AwaitingSignature, CertifyingUserId, CertifyingUserSignatureType, CertifyingUserSigned, CertifyingUserSignedAt, CourseId, CreatedAt, InstructorId, InstructorSignatureType, InstructorSigned, InstructorSignedAt, IsComplex, IsFirstSession, IsHighPerformance, IsMassSession, IsTAA, IsTailWheel, LessonGradeId, ParentTrainingSessionId, PeopleGroupId, PeopleGroupName, Remarks, ReservationId, ReservationNumber, SessionDate, SessionGradeId, SessionType, StudentId, StudentSignatureType, StudentSigned, StudentSignedAt)`
- **`nci_wi_TrainingSessions_A5CE7DDB2D64C8CF9A9DA43314AEB6DF`** (NONCLUSTERED)
  - Columns: `OperatorId, IsDraft INCLUDE (AircraftClass, IsComplex, IsHighPerformance, IsTailWheel, LessonId, TrainingSessionId)`
- **`nci_wi_TrainingSessions_B454BCEF2B9B18CE802C869FBFC9A0AE`** (NONCLUSTERED)
  - Columns: `IsDraft, OperatorId, InstructorId INCLUDE (AircraftClass, CourseId, CreatedAt, EnrollmentId, IsComplex, IsHighPerformance, IsTAA, IsTailWheel, ReservationId, ReservationNumber, StudentId, TrainingSessionId)`
