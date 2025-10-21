# tblPilotTSADocuments

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (3)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `TSADocumentId` | `int(10,0)` | **NO** | `-` | PK | - |
| `TSADocument` | `varchar(150)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblPilotTSADocuments`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `TSADocumentId`
