# ProfileDocumentationExpiration

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (13)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ProfileDocumentationExpirationId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `DocumentationTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `DocumentationId` | `uniqueidentifier` | YES | `-` | - | - |
| `CompletedOn` | `datetime(3)` | YES | `-` | - | - |
| `CompletedBy` | `uniqueidentifier` | YES | `-` | - | - |
| `ExpiresOn` | `datetime(3)` | YES | `-` | - | - |
| `Revoked` | `bit` | **NO** | `-` | - | - |
| `HasFileUpload` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `UserDocumentId` | `nvarchar(200)` | YES | `-` | - | - |

## Indexes

- **`IDX_ProfileDocumentationExpiration_OperatorIdUserId`** (NONCLUSTERED)
  - Columns: `OperatorId, UserId`
- **`IDX_ProfileDocumentationExpiration_ProfileDocumentationExpirationId`** (NONCLUSTERED)
  - Columns: `ProfileDocumentationExpirationId`
- **`PK_ProfileDocumentationExpiration`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
