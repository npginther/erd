# tblAuditEvents

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `EventId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `EventTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `EventAction` | `varchar(15)` | **NO** | `-` | - | - |
| `EventDate` | `datetime(3)` | **NO** | `-` | - | - |
| `Id` | `uniqueidentifier` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `Data` | `text(2147483647)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_tblAuditEvents_CompanyIdId`** (NONCLUSTERED)
  - Columns: `CompanyId, Id`
- **`PK_tblAuditEvents`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `EventId`
