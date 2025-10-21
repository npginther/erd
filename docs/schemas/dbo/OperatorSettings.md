# OperatorSettings

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (12)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `DispatchSheetCustomMessage` | `nvarchar(MAX)` | YES | `-` | - | - |
| `ShowMXStateOnSchedule` | `bit` | YES | `-` | - | - |
| `ShowMXRemindersDuringBooking` | `bit` | YES | `-` | - | - |
| `ShowSquawksDuringBooking` | `bit` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `AccountOwnerUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `PrimaryUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `BillingContactUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `BillingCCEmails` | `nvarchar(MAX)` | YES | `-` | - | - |
| `LastCompanyContactUpdate` | `datetime(3)` | YES | `-` | - | - |

## Indexes

- **`PK_CompanySettings`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`ix_OperatorId_Includes`** (NONCLUSTERED)
  - Columns: `OperatorId INCLUDE (LastCompanyContactUpdate)`
