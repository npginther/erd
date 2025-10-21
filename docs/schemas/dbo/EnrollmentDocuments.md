# EnrollmentDocuments

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (15)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `EnrollmentDocumentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `DocumentTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `Hash` | `nvarchar(2048)` | **NO** | `-` | - | - |
| `OriginalFileName` | `nvarchar(2048)` | **NO** | `-` | - | - |
| `Extension` | `nvarchar(10)` | **NO** | `-` | - | - |
| `ContentType` | `nvarchar(255)` | **NO** | `-` | - | - |
| `CreatedAtUtc` | `datetime(3)` | **NO** | `-` | - | - |
| `SignedAtUtc` | `datetime(3)` | YES | `-` | - | - |
| `SignedBy` | `uniqueidentifier` | YES | `-` | - | - |
| `Historical` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_EnrollmentDocuments`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`nci_wi_EnrollmentDocuments_26C113C566371C8C6766A92223933D07`** (NONCLUSTERED)
  - Columns: `EnrollmentId, OperatorId, SignedAtUtc`
- **`nci_wi_EnrollmentDocuments_6F653A1B4C1C161A05BE0DF4FD33178E`** (NONCLUSTERED)
  - Columns: `EnrollmentDocumentId, OperatorId`
