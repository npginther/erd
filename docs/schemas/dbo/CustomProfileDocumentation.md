# CustomProfileDocumentation

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (17)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `CustomProfileDocumentationId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(150)` | **NO** | `-` | - | - |
| `CompletionStandard` | `nvarchar(MAX)` | **NO** | `-` | - | - |
| `CheckingType` | `int(10,0)` | **NO** | `-` | - | - |
| `ExpirationInterval` | `int(10,0)` | **NO** | `-` | - | - |
| `ExpirationPeriod` | `int(10,0)` | **NO** | `-` | - | - |
| `ExpiresOnLastDayOfMonth` | `bit` | **NO** | `-` | - | - |
| `UserAccessLevel` | `int(10,0)` | **NO** | `-` | - | - |
| `CanOverride` | `bit` | **NO** | `-` | - | - |
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `FileUploadEnabled` | `bit` | **NO** | `-` | - | - |
| `FileUploadRequirement` | `int(10,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `IdEnabled` | `bit` | **NO** | `-` | - | - |
| `IdRequirement` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_CustomProfileDocumentation`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_CustomProfileDocumentation_CustomProfileDocumentationId`** (UNIQUE NONCLUSTERED)
  - Columns: `CustomProfileDocumentationId`
