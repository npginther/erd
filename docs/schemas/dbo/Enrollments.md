# Enrollments

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (41)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CreatedBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CreatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `EnrollmentStatus` | `int(10,0)` | **NO** | `-` | - | - |
| `EnrollmentDate` | `datetime(3)` | YES | `-` | - | - |
| `GraduationDate` | `datetime(3)` | YES | `-` | - | - |
| `TransferredDate` | `datetime(3)` | YES | `-` | - | - |
| `TerminatedDate` | `datetime(3)` | YES | `-` | - | - |
| `ExpectedGraduationDate` | `datetime(3)` | YES | `-` | - | - |
| `LessonCompletionPercentage` | `decimal(9,2)` | YES | `-` | - | - |
| `CourseMinimumCompletionPercentage` | `decimal(9,2)` | YES | `-` | - | - |
| `NextLessonId` | `uniqueidentifier` | YES | `-` | - | - |
| `EnrollmentJobId` | `uniqueidentifier` | YES | `-` | - | - |
| `AcceptedAtUtc` | `datetime(3)` | YES | `-` | - | - |
| `AcceptedBy` | `uniqueidentifier` | YES | `-` | - | - |
| `GraduatedBy` | `uniqueidentifier` | YES | `-` | - | - |
| `GraduationSigned` | `bit` | YES | `-` | - | - |
| `TerminatedBy` | `uniqueidentifier` | YES | `-` | - | - |
| `TransferredBy` | `uniqueidentifier` | YES | `-` | - | - |
| `TransferSigned` | `bit` | YES | `-` | - | - |
| `TerminationSigned` | `bit` | YES | `-` | - | - |
| `RecommendedAtUtc` | `datetime(3)` | YES | `-` | - | - |
| `ExternalId` | `nvarchar(50)` | YES | `-` | - | - |
| `CourseProfileId` | `uniqueidentifier` | YES | `-` | - | - |
| `CourseProfileOverallProgressStatus` | `int(10,0)` | YES | `-` | - | - |
| `CourseProfileTimeField1Id` | `nvarchar(50)` | YES | `-` | - | - |
| `CourseProfileTimeField1CompletionVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `CourseProfileTimeField2Id` | `nvarchar(50)` | YES | `-` | - | - |
| `CourseProfileTimeField2CompletionVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `CourseProfileTimeField3Id` | `nvarchar(50)` | YES | `-` | - | - |
| `CourseProfileTimeField3CompletionVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `CourseProfileLessonCompletionVariance` | `decimal(7,2)` | YES | `-` | - | - |
| `UpdatedAt` | `datetime(3)` | YES | `-` | - | - |
| `ProjectedGraduationDate` | `datetime2(0)` | YES | `-` | - | - |
| `ExpectedLessonsPerWeek` | `decimal(9,2)` | YES | `-` | - | - |
| `ActualLessonsPerWeek` | `decimal(9,2)` | YES | `-` | - | - |
| `RequiredLessonsPerWeek` | `decimal(9,2)` | YES | `-` | - | - |

## Indexes

- **`IDX_Enrollments_OperatorId_CourseIdEnrollmentIdStudentIdEnrollmentDate`** (NONCLUSTERED)
  - Columns: `OperatorId INCLUDE (CourseId, EnrollmentDate, EnrollmentId, StudentId)`
- **`PK_Enrollments`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_Enrollments_EnrollmentId`** (UNIQUE NONCLUSTERED)
  - Columns: `EnrollmentId`
- **`nci_wi_Enrollments_096E7FF34214652A2DC402FD1D781BA8`** (NONCLUSTERED)
  - Columns: `StudentId, OperatorId, EnrollmentStatus, CourseId, EnrollmentId`
