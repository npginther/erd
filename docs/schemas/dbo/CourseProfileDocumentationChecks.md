# CourseProfileDocumentationChecks

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `ProfileDocumentationId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CertificateType` | `int(10,0)` | YES | `-` | - | - |
| `SoloEndorsement` | `bit` | YES | `-` | - | - |
| `FlightReview` | `bit` | YES | `-` | - | - |

## Indexes

- **`PK_CourseProfileDocumentationChecks`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
