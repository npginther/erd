# tblCompanyEmailJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `CompanyId` | `int(10,0)` | **NO** | `-` | PK | - |
| `EmailId` | `int(10,0)` | **NO** | `-` | PK | - |
| `EmailTypeId` | `int(10,0)` | **NO** | `-` | PK | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblCompanyEmailJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `CompanyId, EmailId, EmailTypeId`
