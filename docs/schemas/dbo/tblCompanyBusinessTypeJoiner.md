# tblCompanyBusinessTypeJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `CompanyId` | `int(10,0)` | **NO** | `-` | PK | - |
| `BusinessTypeId` | `int(10,0)` | **NO** | `-` | PK | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblCompanyBusinessTypeJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `CompanyId, BusinessTypeId`
