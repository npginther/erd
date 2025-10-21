# CustomerAccounts

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (16)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `AccountTransactionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `AccountTransactionType` | `int(10,0)` | **NO** | `-` | - | - |
| `TransactionDateUTC` | `datetime(3)` | **NO** | `-` | - | - |
| `TransactionAmount` | `decimal(11,2)` | **NO** | `-` | - | - |
| `ResultingBalance` | `decimal(11,2)` | **NO** | `-` | - | - |
| `InvoiceNumber` | `int(10,0)` | YES | `-` | - | - |
| `InvoiceId` | `uniqueidentifier` | YES | `-` | - | - |
| `Notes` | `nvarchar(500)` | YES | `-` | - | - |
| `CreatedBy` | `uniqueidentifier` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `InvoiceDate` | `datetime(3)` | YES | `-` | - | - |
| `InvoiceDeleted` | `bit` | YES | `-` | - | - |
| `InvoiceOrderedResultingBalance` | `decimal(11,2)` | YES | `-` | - | - |

## Indexes

- **`IDX_CustomerAccounts_OperatorIdUserId`** (NONCLUSTERED)
  - Columns: `OperatorId, UserId`
- **`PK_CustomerAccounts`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`UK_CustomerAccounts`** (UNIQUE NONCLUSTERED)
  - Columns: `AccountTransactionId`
