# CustomCancellationReasons

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `id` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CancellationReasonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Reason` | `nvarchar(100)` | **NO** | `-` | - | - |
| `IsDeleted` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CancellationCause` | `int(10,0)` | YES | `-` | - | - |
| `RequireExplanation` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_CustomCancellationReasons`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `id`
- **`ix_CustomCancellationReasons_CompanyId_IsDeleted`** (NONCLUSTERED)
  - Columns: `CompanyId, IsDeleted`
