# tblFlightInstructor

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (13)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `InstructorId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `PilotId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `DisplayName` | `varchar(75)` | **NO** | `-` | - | - |
| `IsActive` | `bit` | **NO** | `-` | - | - |
| `ScheduleOrder` | `int(10,0)` | **NO** | `-` | - | - |
| `IsDeleted` | `bit` | **NO** | `-` | - | - |
| `UserGUIDId` | `uniqueidentifier` | YES | `-` | - | - |
| `ImageHash` | `nvarchar(100)` | YES | `-` | - | - |
| `About` | `nvarchar(MAX)` | YES | `-` | - | - |
| `InstructorType` | `int(10,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.ScheduleMatchUserPreferencesToFlightInstructorJoiner`** 
  via `InstructorId` → `InstructorId`

## Indexes

- **`IDX_tblFlightInstructor_CompanyIdIsActiveIsDeleted`** (NONCLUSTERED)
  - Columns: `CompanyId, IsActive, IsDeleted`
- **`IDX_tblFlightInstructor_UserGuidID_InstructorIdDisplayName`** (NONCLUSTERED)
  - Columns: `UserGUIDId INCLUDE (DisplayName, InstructorId)`
- **`PK_tblFlightInstructors`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `InstructorId`
- **`ix_CompanyId_IsDeleted`** (NONCLUSTERED)
  - Columns: `CompanyId, IsDeleted`
- **`ix_tblFlightInstructor_PilotId_IsActive_IsDeleted`** (NONCLUSTERED)
  - Columns: `PilotId, IsActive, IsDeleted`
