# DocumentUploadBackups

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (13)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `DocumentUploadBackupId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `InitiatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `InitiatedBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Status` | `int(10,0)` | **NO** | `-` | - | - |
| `CompletedAt` | `datetime(3)` | YES | `-` | - | - |
| `ExpiresAt` | `datetime(3)` | YES | `-` | - | - |
| `ContentType` | `nvarchar(255)` | YES | `-` | - | - |
| `FilePath` | `nvarchar(2048)` | YES | `-` | - | - |
| `FileName` | `nvarchar(285)` | YES | `-` | - | - |
| `DocumentUploadProviderId` | `int(10,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_DocumentUploadBackups`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
