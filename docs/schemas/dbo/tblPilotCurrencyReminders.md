# tblPilotCurrencyReminders

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (11)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `int(10,0)` | **NO** | `-` | PK | - |
| `Name` | `varchar(75)` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Interval` | `int(10,0)` | **NO** | `-` | - | - |
| `ExpiresOnLastDayOfMonth` | `bit` | **NO** | `-` | - | - |
| `CurrencyTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `ApplyToStudentPilots` | `bit` | **NO** | `-` | - | - |
| `OnlyApplyToStudentPilots` | `bit` | **NO** | `-` | - | - |
| `GuidId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblPilotCurrencyReminders`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
- **`ix_tblPilotCurrencyReminders_CompanyId`** (NONCLUSTERED)
  - Columns: `CompanyId`
