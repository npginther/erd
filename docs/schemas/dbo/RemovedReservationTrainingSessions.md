# RemovedReservationTrainingSessions

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (12)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | YES | `-` | - | - |
| `IsCompleted` | `bit` | **NO** | `-` | - | - |
| `SessionDate` | `datetime(3)` | YES | `-` | - | - |
| `SessionTime` | `decimal(9,2)` | YES | `-` | - | - |
| `SessionId` | `uniqueidentifier` | YES | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | YES | `-` | - | - |
| `SessionStatus` | `int(10,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_RemovedReservationTrainingSessions`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
