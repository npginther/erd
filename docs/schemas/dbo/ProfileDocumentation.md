# ProfileDocumentation

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (11)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ProfileDocumentationId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `DocumentationTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `Enabled` | `bit` | **NO** | `-` | - | - |
| `UserAccessLevel` | `int(10,0)` | **NO** | `-` | - | - |
| `CanBeOverridden` | `bit` | **NO** | `-` | - | - |
| `FileUploadEnabled` | `bit` | **NO** | `-` | - | - |
| `FileUploadRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_ProfileDocumentation`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_ProfileDocumentation_CompanyIdProfileDocumentationTypeId`** (UNIQUE NONCLUSTERED)
  - Columns: `CompanyId, DocumentationTypeId`
- **`UK_ProfileDocumentation_ProfileDocumentationId`** (UNIQUE NONCLUSTERED)
  - Columns: `_RowId`
