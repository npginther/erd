# ReservationTypeProfileDocumentationChecks

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (16)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ReservationTypeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `ActivityRole` | `int(10,0)` | **NO** | `-` | - | - |
| `DocumentationTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `Requirement` | `int(10,0)` | **NO** | `-` | - | - |
| `CertificateType` | `int(10,0)` | YES | `-` | - | - |
| `ExpirationInterval` | `int(10,0)` | YES | `-` | - | - |
| `ExpirationPeriod` | `int(10,0)` | YES | `-` | - | - |
| `SoloEndorsement` | `bit` | YES | `-` | - | - |
| `FlightReview` | `bit` | YES | `-` | - | - |
| `FlightInstructorRating` | `bit` | YES | `-` | - | - |
| `RequirementValue` | `decimal(9,2)` | YES | `-` | - | - |
| `IgnoreIfInstructorExists` | `bit` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_ReservationTypeProfileDocumentationChecks`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_ReservationTypeProfileDocumentationChecks_ReservationTypeIdCompanyIdActivityRoleDocumentationTypeId`** (UNIQUE NONCLUSTERED)
  - Columns: `ReservationTypeId, CompanyId, ActivityRole, DocumentationTypeId`
