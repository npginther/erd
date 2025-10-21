# Courses

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (49)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `Status` | `int(10,0)` | **NO** | `-` | - | - |
| `StagesEnabled` | `bit` | **NO** | `-` | - | - |
| `StagesPluralLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `StagesSingularLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `PhasesEnabled` | `bit` | **NO** | `-` | - | - |
| `PhasesPluralLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `PhasesSingularLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `LessonsPluralLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `LessonsSingularLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `PartsEnabled` | `bit` | **NO** | `-` | - | - |
| `PartsPluralLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `PartsSingularLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `TasksPluralLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `TasksSingularLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `EnrollmentType` | `int(10,0)` | **NO** | `-` | - | - |
| `Objectives` | `nvarchar(MAX)` | YES | `-` | - | - |
| `CreatedAtUtc` | `datetime(3)` | **NO** | `-` | - | - |
| `PINRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `Description` | `nvarchar(MAX)` | YES | `-` | - | - |
| `CompletionStandard` | `nvarchar(MAX)` | YES | `-` | - | - |
| `RequiredStudy` | `nvarchar(MAX)` | YES | `-` | - | - |
| `RecommendedStudy` | `nvarchar(MAX)` | YES | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |
| `SyllabusProviderId` | `int(10,0)` | YES | `-` | - | - |
| `TermsOfServiceAcceptedBy` | `uniqueidentifier` | YES | `-` | - | - |
| `SyllabusProviderCourseId` | `uniqueidentifier` | YES | `-` | - | - |
| `SyllabusProviderCourseTypeId` | `int(10,0)` | YES | `-` | - | - |
| `IsReadOnly` | `bit` | **NO** | `-` | - | - |
| `IsChargedCourse` | `bit` | **NO** | `-` | - | - |
| `FAAPart141CertNumber` | `nvarchar(100)` | YES | `-` | - | - |
| `EnrollmentCertificateEnabled` | `bit` | **NO** | `-` | - | - |
| `EnrollmentCertificateCourseName` | `nvarchar(MAX)` | YES | `-` | - | - |
| `SyllabusEnabled` | `bit` | **NO** | `-` | - | - |
| `SafetyProceduresEnabled` | `bit` | **NO** | `-` | - | - |
| `EnrollmentDocsPINRequired` | `bit` | **NO** | `-` | - | - |
| `GraduationCertificateEnabled` | `bit` | **NO** | `-` | - | - |
| `GraduationCertificateCourseName` | `nvarchar(MAX)` | YES | `-` | - | - |
| `GraduationDocsPINRequired` | `bit` | **NO** | `-` | - | - |
| `ExternalId` | `nvarchar(50)` | YES | `-` | - | - |
| `EnrollmentCertificateCompanyName` | `nvarchar(MAX)` | YES | `-` | - | - |
| `GraduationCertificateCompanyName` | `nvarchar(MAX)` | YES | `-` | - | - |
| `CourseTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `Version` | `int(10,0)` | YES | `-` | - | - |
| `ShowDeprecatedFieldWarning` | `bit` | YES | `-` | - | - |
| `CourseFamilyId` | `uniqueidentifier` | YES | `-` | - | - |

## Indexes

- **`PK_Courses`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_Courses_CourseId`** (UNIQUE NONCLUSTERED)
  - Columns: `CourseId`
- **`ix_Courses_CourseFamilyId`** (NONCLUSTERED)
  - Columns: `CourseFamilyId INCLUDE (CourseId)`
- **`nci_wi_Courses_7F7D3A98CDE02C53D9252215A2EBF4F2`** (NONCLUSTERED)
  - Columns: `OperatorId, Status`
