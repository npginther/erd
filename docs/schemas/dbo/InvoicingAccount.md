# InvoicingAccount

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (11)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `InvoicingAccountId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(150)` | **NO** | `-` | - | - |
| `Active` | `bit` | **NO** | `-` | - | - |
| `IsDeleted` | `bit` | **NO** | `-` | - | - |
| `AccountingAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountingAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountType` | `nvarchar(100)` | YES | `-` | - | - |
| `QBDAccountingAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `QBDAccountingAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_InvoicingAccount`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `InvoicingAccountId`
