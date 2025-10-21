# LabelToUserJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `LabelId` | `bigint(19,0)` | **NO** | `-` | PK<br/>FK->`Labels` | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | PK | - |
| `UserGuid` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CreatedAtUtc` | `datetime2(7)` | **NO** | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.Labels`** 
  via `LabelId` → `LabelId` `ON DELETE CASCADE`

## Indexes

- **`IX_LabelToUserJoiner_LabelId_OperatorId`** (NONCLUSTERED)
  - Columns: `LabelId, OperatorId`
- **`IX_LabelToUserJoiner_UserGuid_OperatorId`** (NONCLUSTERED)
  - Columns: `UserGuid, OperatorId`
- **`PK_LabelToUserJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `LabelId, OperatorId, UserGuid`
