# MassEmails

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (15)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_rowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `MassEmailId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Subject` | `nvarchar(150)` | **NO** | `-` | - | - |
| `Body` | `nvarchar(MAX)` | YES | `-` | - | - |
| `IncludeInactiveUsers` | `bit` | YES | `-` | - | - |
| `Status` | `int(10,0)` | **NO** | `-` | - | - |
| `Creator` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CreatedAt` | `datetime(3)` | **NO** | `-` | - | - |
| `Sender` | `uniqueidentifier` | YES | `-` | - | - |
| `SentAt` | `datetime(3)` | YES | `-` | - | - |
| `Recipients` | `int(10,0)` | YES | `-` | - | - |
| `FromName` | `nvarchar(150)` | YES | `-` | - | - |
| `ReplyTo` | `nvarchar(254)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_MassEmails`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_rowId`
- **`UK_MassEmails_MassEmailId`** (UNIQUE NONCLUSTERED)
  - Columns: `MassEmailId`
