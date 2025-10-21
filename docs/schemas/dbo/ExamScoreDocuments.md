# ExamScoreDocuments

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (14)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ExamScoreDocumentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `ExamId` | `uniqueidentifier` | YES | `-` | - | - |
| `ExamScoreId` | `uniqueidentifier` | YES | `-` | - | - |
| `Hash` | `nvarchar(2048)` | **NO** | `-` | - | - |
| `OriginalFileName` | `nvarchar(2048)` | **NO** | `-` | - | - |
| `Extension` | `nvarchar(10)` | **NO** | `-` | - | - |
| `ContentType` | `nvarchar(255)` | **NO** | `-` | - | - |
| `CreatedAtUtc` | `datetime(3)` | **NO** | `-` | - | - |
| `SizeInBytes` | `bigint(19,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_ExamScoreDocuments`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
