# tblPerson

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (34)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PersonId` | `int(10,0)` | **NO** | `-` | PK | - |
| `UserId` | `int(10,0)` | **NO** | `-` | - | - |
| `FirstName` | `varchar(50)` | **NO** | `-` | - | - |
| `MiddleName` | `varchar(50)` | **NO** | `-` | - | - |
| `LastName` | `varchar(50)` | **NO** | `-` | - | - |
| `WebSiteURL` | `varchar(50)` | YES | `-` | - | - |
| `BirthDate` | `datetime(3)` | YES | `-` | - | - |
| `SSN` | `varbinary(68)` | YES | `-` | - | - |
| `PassportNumber` | `varbinary(68)` | YES | `-` | - | - |
| `Nationality` | `varbinary(68)` | YES | `-` | - | - |
| `IsMale` | `bit` | YES | `-` | - | - |
| `DriverLicenseNumber` | `varbinary(68)` | YES | `-` | - | - |
| `DriverLicenseState` | `varchar(50)` | **NO** | `-` | - | - |
| `GetsAdminNewsletter` | `bit` | **NO** | `-` | - | - |
| `GetsBasicNewsletter` | `bit` | **NO** | `-` | - | - |
| `Prefix` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Suffix` | `nvarchar(50)` | **NO** | `-` | - | - |
| `EmergContactName` | `nvarchar(50)` | **NO** | `-` | - | - |
| `EmergMobilePhone` | `nvarchar(25)` | **NO** | `-` | - | - |
| `EmergHomePhone` | `nvarchar(25)` | **NO** | `-` | - | - |
| `EmergWorkPhone` | `nvarchar(25)` | **NO** | `-` | - | - |
| `EmergEmailAddress` | `nvarchar(64)` | **NO** | `-` | - | - |
| `EmergRelationship` | `nvarchar(50)` | **NO** | `-` | - | - |
| `UICulture` | `int(10,0)` | **NO** | `-` | - | - |
| `TimeZone` | `int(10,0)` | **NO** | `-` | - | - |
| `Height` | `nvarchar(10)` | **NO** | `-` | - | - |
| `Weight` | `nvarchar(10)` | **NO** | `-` | - | - |
| `HairColor` | `nvarchar(15)` | **NO** | `-` | - | - |
| `EyeColor` | `nvarchar(15)` | **NO** | `-` | - | - |
| `CultureId` | `int(10,0)` | **NO** | `-` | - | - |
| `UserGUIDId` | `uniqueidentifier` | YES | `-` | - | - |
| `CompanyName` | `nvarchar(100)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`IDX_tblPerson_LastName_PersonIdUserId`** (NONCLUSTERED)
  - Columns: `LastName INCLUDE (PersonId, UserId)`
- **`IDX_tblPerson_UserGuidId_FirstNameLastName`** (NONCLUSTERED)
  - Columns: `UserGUIDId INCLUDE (FirstName, LastName)`
- **`IDX_tblPerson_UserId_PersonId`** (NONCLUSTERED)
  - Columns: `UserId INCLUDE (PersonId)`
- **`LastName`** (NONCLUSTERED)
  - Columns: `LastName`
- **`PK_tblPerson`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PersonId`
- **`TimeZone`** (NONCLUSTERED)
  - Columns: `TimeZone`
- **`UICulture`** (NONCLUSTERED)
  - Columns: `UICulture`
