# tblPersonEmailJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PersonId` | `int(10,0)` | **NO** | `-` | PK | - |
| `EmailId` | `int(10,0)` | **NO** | `-` | PK | - |
| `EmailTypeId` | `int(10,0)` | **NO** | `-` | PK | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`EmailId`** (NONCLUSTERED)
  - Columns: `EmailId`
- **`PK_tblPersonEmailJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PersonId, EmailId, EmailTypeId`
- **`PersonId`** (NONCLUSTERED)
  - Columns: `PersonId`
