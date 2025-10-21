# EnrollmentInstructors

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `InstructorId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `PrimaryInstructor` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_EnrollmentInstructors`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`ix_EnrollmentInstructors_OperatorId`** (NONCLUSTERED)
  - Columns: `OperatorId INCLUDE (EnrollmentId, InstructorId)`
- **`nci_wi_EnrollmentInstructors_1F3EE2B3476CD28D89E1BFA868C12DB2`** (NONCLUSTERED)
  - Columns: `EnrollmentId INCLUDE (InstructorId, PrimaryInstructor)`
- **`nci_wi_EnrollmentInstructors_BABD0DFA15F4E24DB55656509AB99C56`** (NONCLUSTERED)
  - Columns: `OperatorId, EnrollmentId, PrimaryInstructor INCLUDE (InstructorId)`
