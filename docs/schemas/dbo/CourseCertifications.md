# CourseCertifications

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CourseCertificationId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CertificationId` | `uniqueidentifier` | YES | `-` | - | - |
| `RegulationId` | `int(10,0)` | YES | `-` | - | - |
| `Other` | `nvarchar(100)` | YES | `-` | - | - |

## Indexes

- **`PK_CourseCertifications`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_CourseCertifications_CourseCertificationId`** (UNIQUE NONCLUSTERED)
  - Columns: `CourseCertificationId`
- **`nci_wi_CourseCertifications_52FF7A99A49BFE4BC592393E9BFB4A69`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId, RegulationId INCLUDE (CertificationId, CourseCertificationId, Other)`
