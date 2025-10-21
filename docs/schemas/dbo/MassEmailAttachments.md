# MassEmailAttachments

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_rowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `MassEmailAttachmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `MassEmailId` | `uniqueidentifier` | YES | `-` | - | - |
| `BlobExists` | `bit` | **NO** | `-` | - | - |
| `MimeType` | `nvarchar(255)` | **NO** | `-` | - | - |
| `FileName` | `varchar(255)` | **NO** | `-` | - | - |
| `FileSize` | `bigint(19,0)` | **NO** | `-` | - | - |
| `CreatedAtUtc` | `datetime(3)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_MassEmailAttachments`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_rowId`
