# tblResourceLineItemJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `ResourceId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `ResourceType` | `int(10,0)` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `LineItemId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblResourceLineItemJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `ResourceId`
