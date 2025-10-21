# tblGatewayPagesText

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `CompanyId` | `char(10)` | **NO** | `-` | PK | - |
| `LoginPageText` | `nvarchar(1000)` | **NO** | `-` | - | - |
| `UserSignUpPageText` | `nvarchar(1000)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `char(10)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblGatewayPagesText`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `CompanyId`
