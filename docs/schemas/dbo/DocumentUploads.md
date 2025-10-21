# DocumentUploads

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (18)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `DocumentUploadId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `FriendlyName` | `nvarchar(255)` | **NO** | `-` | - | - |
| `Extension` | `nvarchar(10)` | **NO** | `-` | - | - |
| `SizeInBytes` | `bigint(19,0)` | **NO** | `-` | - | - |
| `DocumentTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `DocumentUploadProviderId` | `int(10,0)` | **NO** | `-` | - | - |
| `DocumentUploadFilePath` | `nvarchar(2048)` | **NO** | `-` | - | - |
| `DocumentUploadFileName` | `nvarchar(285)` | **NO** | `-` | - | - |
| `ContentType` | `nvarchar(255)` | **NO** | `-` | - | - |
| `StoredAt` | `datetime(3)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | YES | `-` | - | - |
| `NoteId` | `uniqueidentifier` | YES | `-` | - | - |
| `UserDocumentationTypeId` | `int(10,0)` | YES | `-` | - | - |
| `CustomUserDocumentId` | `uniqueidentifier` | YES | `-` | - | - |
| `AddedToTrashCanAt` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_DocumentUploads`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`ix_OperatorId_DocumentTypeId_UserId_UserDocumentationTypeId_AddedToTrashCanAt`** (NONCLUSTERED)
  - Columns: `OperatorId, DocumentTypeId, UserId, UserDocumentationTypeId, AddedToTrashCanAt`
