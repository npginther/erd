# EnrollmentCredits

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
| `StudentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `AppliesToCourseMinimums` | `bit` | **NO** | `-` | - | - |
| `PreviousSchool` | `nvarchar(200)` | YES | `-` | - | - |
| `PreviousSchoolNumber` | `nvarchar(25)` | YES | `-` | - | - |

## Indexes

- **`PK_EnrollmentCredits`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_EnrollmentCredits_EnrollmentId`** (UNIQUE NONCLUSTERED)
  - Columns: `EnrollmentId`
