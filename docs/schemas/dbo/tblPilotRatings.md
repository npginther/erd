# tblPilotRatings

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `RatingId` | `int(10,0)` | **NO** | `-` | PK | - |
| `CertificateClass` | `varchar(50)` | **NO** | `-` | - | - |
| `RatingClass` | `varchar(50)` | **NO** | `-` | - | - |
| `Rating` | `varchar(50)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblPilotRatings`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `RatingId`
