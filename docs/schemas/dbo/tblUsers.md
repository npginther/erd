# tblUsers

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (31)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `UserId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserName` | `varchar(50)` | **NO** | `-` | PK | - |
| `Password` | `varchar(160)` | **NO** | `-` | - | - |
| `SecretQuestionId` | `int(10,0)` | **NO** | `-` | - | - |
| `SecretQuestionAnswer` | `varchar(50)` | **NO** | `-` | - | - |
| `LastLoginDate` | `datetime(3)` | **NO** | `-` | - | - |
| `CreatedDate` | `datetime(3)` | YES | `-` | - | - |
| `IsConfirmed` | `bit` | **NO** | `-` | - | - |
| `GUID` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CodePageId` | `int(10,0)` | YES | `-` | - | - |
| `CharSet` | `int(10,0)` | YES | `-` | - | - |
| `SignUpMethod` | `int(10,0)` | **NO** | `-` | - | - |
| `IsUsingTempPassword` | `bit` | **NO** | `-` | - | - |
| `EmailFormatIsHTML` | `bit` | **NO** | `-` | - | - |
| `PhonePIN` | `varchar(4)` | **NO** | `-` | - | - |
| `GlobalUserId` | `bigint(19,0)` | YES | `-` | - | - |
| `GlobalUserRequired` | `bit` | **NO** | `-` | - | - |
| `ProfileImageHash` | `nvarchar(100)` | YES | `-` | - | - |
| `EmployeeId` | `nvarchar(50)` | YES | `-` | - | - |
| `ProPayPayerId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountingUserId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountingUserName` | `nvarchar(100)` | YES | `-` | - | - |
| `QBDAccountingUserId` | `nvarchar(100)` | YES | `-` | - | - |
| `QBDAccountingUserName` | `nvarchar(100)` | YES | `-` | - | - |
| `QBDTaxReferenceId` | `uniqueidentifier` | YES | `-` | - | - |
| `QBDSalesTaxId` | `uniqueidentifier` | YES | `-` | - | - |
| `PeopleGroupId` | `uniqueidentifier` | YES | `-` | - | - |
| `AddedToGroupAt` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |
| `ExternalId` | `nvarchar(50)` | YES | `-` | - | - |

## Indexes

- **`CharSet`** (NONCLUSTERED)
  - Columns: `CharSet`
- **`CodePageId`** (NONCLUSTERED)
  - Columns: `CodePageId`
- **`IDX_tblUsers_GlobalUserId_UserId`** (NONCLUSTERED)
  - Columns: `GlobalUserId INCLUDE (UserId)`
- **`IDX_tblUsers_Guid_GlobalUserId`** (NONCLUSTERED)
  - Columns: `GUID INCLUDE (GlobalUserId)`
- **`IDX_tblUsers_PeopleGroupId_UserIdUserName`** (NONCLUSTERED)
  - Columns: `PeopleGroupId INCLUDE (UserId, UserName)`
- **`PK_tblUsers`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `UserName`
- **`UX_tblUsers_GUID`** (UNIQUE NONCLUSTERED)
  - Columns: `GUID`
- **`UserId`** (NONCLUSTERED)
  - Columns: `UserId`
