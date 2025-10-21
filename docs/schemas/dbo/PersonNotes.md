# PersonNotes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `UserGuidId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Note` | `nvarchar(1000)` | **NO** | `-` | - | - |
| `CreatedByUserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CreatedAtUTC` | `datetime(3)` | YES | `-` | - | - |
| `PersonNoteId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `Deleted` | `bit` | **NO** | `-` | - | - |
| `InternalNote` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_PersonNotes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PersonNoteId`
