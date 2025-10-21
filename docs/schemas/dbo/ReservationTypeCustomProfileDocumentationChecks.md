# ReservationTypeCustomProfileDocumentationChecks

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ReservationTypeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `ActivityRole` | `int(10,0)` | **NO** | `-` | - | - |
| `CustomProfileDocumentationId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Requirement` | `int(10,0)` | **NO** | `-` | - | - |
| `IgnoreIfInstructorExists` | `bit` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_ReservationTypeCustomProfileDocumentationChecks`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_ReservationTypeCustomProfileDocumentationChecks_ReservationTypeIdCompanyIdActivityRoleCustomProfileDocumentation`** (UNIQUE NONCLUSTERED)
  - Columns: `ReservationTypeId, CompanyId, ActivityRole, CustomProfileDocumentationId`
