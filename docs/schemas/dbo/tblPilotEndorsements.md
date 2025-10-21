# tblPilotEndorsements

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `EndorsementId` | `int(10,0)` | **NO** | `-` | PK | - |
| `EndorsementType` | `varchar(50)` | **NO** | `-` | - | - |
| `EndorsementFAR` | `varchar(50)` | **NO** | `-` | - | - |
| `Endorsement` | `varchar(75)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblPilotEndorsements`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `EndorsementId`
