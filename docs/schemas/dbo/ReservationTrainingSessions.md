# ReservationTrainingSessions

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (16)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ReservationId` | `uniqueidentifier` | **NO** | `-` | FK->`tblReservation` | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | YES | `-` | - | - |
| `IsCompleted` | `bit` | **NO** | `-` | - | - |
| `SessionDate` | `datetime(3)` | YES | `-` | - | - |
| `SessionTime` | `decimal(9,2)` | YES | `-` | - | - |
| `SessionId` | `uniqueidentifier` | YES | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | YES | `-` | - | - |
| `SessionStatus` | `int(10,0)` | YES | `-` | - | - |
| `SessionNumber` | `bigint(19,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `IsMassSession` | `bit` | **NO** | `-` | - | - |
| `InstructorId` | `uniqueidentifier` | YES | `-` | - | - |
| `StudentId` | `uniqueidentifier` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblReservation`** 
  via `ReservationId` → `ReservationId` `ON DELETE CASCADE`

## Indexes

- **`PK_ReservationTrainingSessions`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`dbo.IDX_ReservationTrainingSessions_ReservationIdOperatorId`** (NONCLUSTERED)
  - Columns: `ReservationId, OperatorId`
