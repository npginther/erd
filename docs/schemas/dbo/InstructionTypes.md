# InstructionTypes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `InstructionTypeId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `Active` | `bit` | **NO** | `-` | - | - |
| `InvoicingAccountId` | `uniqueidentifier` | YES | `-` | - | - |
| `Billable` | `bit` | YES | `-` | - | - |
| `TrainingType` | `int(10,0)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_InstructionTypes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `InstructionTypeId`
