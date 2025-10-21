# tblEnginePropellerJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `EngineId` | `uniqueidentifier` | **NO** | `-` | PK<br/>FK->`tblEngine` | - |
| `PropellerId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblEngine`** 
  via `EngineId` → `EngineId` `ON DELETE CASCADE`

## Indexes

- **`PK_tblEnginePropellerJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `EngineId, PropellerId`
