# tblPersonToContactNumberJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PersonId` | `int(10,0)` | **NO** | `-` | PK | - |
| `ContactNumberId` | `int(10,0)` | **NO** | `-` | PK<br/>FK->`tblContactNumbers` | - |
| `ContactNumberType` | `int(10,0)` | **NO** | `-` | PK | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblContactNumbers`** 
  via `ContactNumberId` → `Id` `ON DELETE CASCADE`

## Indexes

- **`PK_tblPersonToContactNumberJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PersonId, ContactNumberId, ContactNumberType`
