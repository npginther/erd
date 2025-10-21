# tblContactNumbers

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `int(10,0)` | **NO** | `-` | PK | - |
| `Number` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Comment` | `nvarchar(50)` | **NO** | `-` | - | - |
| `ReceiveSMS` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.tblPersonToContactNumberJoiner`** 
  via `ContactNumberId` → `Id`

## Indexes

- **`PK_tblContactNumbers`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
