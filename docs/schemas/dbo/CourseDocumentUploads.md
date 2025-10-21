# CourseDocumentUploads

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (14)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CourseDocumentUploadId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseDocumentTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `Hash` | `nvarchar(2048)` | **NO** | `-` | - | - |
| `OriginalFileName` | `nvarchar(2048)` | **NO** | `-` | - | - |
| `Extension` | `nvarchar(10)` | **NO** | `-` | - | - |
| `SizeInBytes` | `bigint(19,0)` | **NO** | `-` | - | - |
| `ContentType` | `nvarchar(255)` | **NO** | `-` | - | - |
| `StoredAt` | `datetime(3)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | YES | `-` | - | - |
| `Deleted` | `bit` | **NO** | `-` | - | - |
| `DeletedAt` | `datetime(3)` | YES | `-` | - | - |

## Indexes

- **`PK_CourseDocumentUploads`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
