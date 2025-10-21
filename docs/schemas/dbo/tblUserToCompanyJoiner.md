# tblUserToCompanyJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (19)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `CompanyId` | `int(10,0)` | **NO** | `-` | PK | - |
| `UserId` | `int(10,0)` | **NO** | `-` | PK | - |
| `IsDefault` | `bit` | **NO** | `-` | - | - |
| `IsApproved` | `bit` | **NO** | `-` | - | - |
| `SignedUpCompany` | `bit` | **NO** | `-` | - | - |
| `IsActive` | `bit` | **NO** | `-` | - | - |
| `IsDeleted` | `bit` | **NO** | `-` | - | - |
| `DeactivationReason` | `varchar(750)` | **NO** | `-` | - | - |
| `IsCharterCustomer` | `bit` | **NO** | `-` | - | - |
| `IsFlightSchoolCustomer` | `bit` | **NO** | `-` | - | - |
| `IsCharterPassenger` | `bit` | **NO** | `-` | - | - |
| `IsCFDPassenger` | `bit` | **NO** | `-` | - | - |
| `IsEmployee` | `bit` | **NO** | `-` | - | - |
| `IsFlightSchoolStudent` | `bit` | YES | `-` | - | - |
| `AvailableInList` | `bit` | **NO** | `-` | - | - |
| `DeletedAt` | `datetime(3)` | YES | `-` | - | - |
| `DocumentUploadsDeletedAfterUserDeleted` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`CompanyId`** (NONCLUSTERED)
  - Columns: `CompanyId`
- **`IDX_tblUserToCompanyJoiner_IsApprovedIsActiveIsDeleted_UserId`** (NONCLUSTERED)
  - Columns: `IsApproved, IsActive, IsDeleted INCLUDE (UserId)`
- **`IsDefault`** (NONCLUSTERED)
  - Columns: `IsDefault`
- **`PK_tblUserToCompanyJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `CompanyId, UserId`
- **`UserId`** (NONCLUSTERED)
  - Columns: `UserId`
- **`ix_IsActive_IsDeleted`** (NONCLUSTERED)
  - Columns: `IsActive, IsDeleted`
- **`ix_tblUserToCompanyJoiner_IsApproved_IsDeleted_includes`** (NONCLUSTERED)
  - Columns: `IsApproved, IsDeleted INCLUDE (UserId)`
