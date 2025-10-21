# tblAuditEventTypes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (3)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `EventTypeId` | `int(10,0)` | **NO** | `-` | PK | - |
| `EventType` | `varchar(200)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblAuditEventTypes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `EventTypeId`
