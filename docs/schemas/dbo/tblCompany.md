# tblCompany

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (109)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `int(10,0)` | **NO** | `-` | PK | - |
| `CompanyGuidId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `InternalCompanyName` | `nvarchar(100)` | **NO** | `-` | - | - |
| `CustomerCompanyName` | `nvarchar(100)` | **NO** | `-` | - | - |
| `GovernmentCompanyName` | `nvarchar(100)` | **NO** | `-` | - | - |
| `ParentCompanyId` | `int(10,0)` | YES | `-` | - | - |
| `TimeZoneOffset` | `int(10,0)` | **NO** | `-` | - | - |
| `Culture` | `int(10,0)` | **NO** | `-` | - | - |
| `UICulture` | `int(10,0)` | **NO** | `-` | - | - |
| `WebAddress` | `nvarchar(64)` | **NO** | `-` | - | - |
| `CreatedDate` | `datetime(3)` | YES | `-` | - | - |
| `StorageSpace` | `int(10,0)` | **NO** | `-` | - | - |
| `CreditCardNumber` | `nvarchar(50)` | **NO** | `-` | - | - |
| `NameOnCreditCard` | `nvarchar(50)` | **NO** | `-` | - | - |
| `CreditCardExpDate` | `datetime(3)` | YES | `-` | - | - |
| `CreditCardCCV` | `nchar(10)` | **NO** | `-` | - | - |
| `IsActive` | `bit` | **NO** | `-` | - | - |
| `CharSetId` | `int(10,0)` | **NO** | `-` | - | - |
| `CodePageId` | `int(10,0)` | **NO** | `-` | - | - |
| `IACO` | `char(10)` | **NO** | `-` | - | - |
| `EmailAddress` | `nvarchar(64)` | YES | `-` | - | - |
| `PhoneNumber` | `nvarchar(30)` | YES | `-` | - | - |
| `NumberOfAircraftId` | `int(10,0)` | YES | `-` | - | - |
| `NumberOfInstructorsId` | `int(10,0)` | YES | `-` | - | - |
| `NumberOfEmployeesId` | `int(10,0)` | YES | `-` | - | - |
| `NumberOfUsersId` | `int(10,0)` | YES | `-` | - | - |
| `EmailSubHeader` | `nvarchar(1000)` | **NO** | `-` | - | - |
| `EmailFooter` | `nvarchar(1000)` | **NO** | `-` | - | - |
| `PrimaryContactName` | `nvarchar(100)` | **NO** | `-` | - | - |
| `FaxNumber` | `nvarchar(30)` | **NO** | `-` | - | - |
| `GatewaySubHeader` | `nvarchar(1000)` | **NO** | `-` | - | - |
| `LogoutURL` | `nvarchar(100)` | **NO** | `-` | - | - |
| `ThemeID` | `int(10,0)` | **NO** | `-` | - | - |
| `AccountingPackageId` | `int(10,0)` | **NO** | `-` | - | - |
| `LoginURL` | `varchar(75)` | **NO** | `-` | - | - |
| `NewUserEmailAddress` | `varchar(75)` | **NO** | `-` | - | - |
| `IsInternal` | `bit` | **NO** | `-` | - | - |
| `IsInTrial` | `bit` | **NO** | `-` | - | - |
| `CCDeclined` | `bit` | **NO** | `-` | - | - |
| `MonthlyPayment` | `bit` | **NO** | `-` | - | - |
| `YearlyPayment` | `bit` | **NO** | `-` | - | - |
| `CreditCardPayment` | `bit` | **NO** | `-` | - | - |
| `CheckPayment` | `bit` | **NO** | `-` | - | - |
| `HasPhoneAccess` | `bit` | **NO** | `-` | - | - |
| `V2Pricing` | `bit` | **NO** | `-` | - | - |
| `V2AircraftFee` | `decimal(9,2)` | **NO** | `-` | - | - |
| `V2InstructorFee` | `decimal(9,2)` | **NO** | `-` | - | - |
| `V2CustomFee` | `decimal(9,2)` | **NO** | `-` | - | - |
| `TermStartedDate` | `datetime(3)` | YES | `-` | - | - |
| `InvoicePastDue` | `bit` | **NO** | `-` | - | - |
| `V31Pricing` | `bit` | **NO** | `-` | - | - |
| `ReferralText` | `varchar(100)` | **NO** | `-` | - | - |
| `V4Pricing` | `bit` | **NO** | `-` | - | - |
| `ProductId` | `uniqueidentifier` | YES | `-` | - | - |
| `CustomProductPrice` | `decimal(16,2)` | **NO** | `-` | - | - |
| `HasCustomPrice` | `bit` | **NO** | `-` | - | - |
| `LastActivityDate` | `datetime(3)` | YES | `-` | - | - |
| `SalesForceLeadId` | `varchar(50)` | YES | `-` | - | - |
| `AviationAuthority` | `int(10,0)` | YES | `-` | - | - |
| `SquawkLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `SquawksLabel` | `nvarchar(50)` | YES | `-` | - | - |
| `LogoImageHash` | `nvarchar(100)` | YES | `-` | - | - |
| `EmailLogoImageHash` | `nvarchar(100)` | YES | `-` | - | - |
| `EmailHeaderMarkdown` | `nvarchar(MAX)` | YES | `-` | - | - |
| `EmailFooterMarkdown` | `nvarchar(MAX)` | YES | `-` | - | - |
| `UpgradedToV4` | `bit` | YES | `-` | - | - |
| `UpgradeToV4Date` | `datetime(3)` | YES | `-` | - | - |
| `FspEmailMandrillSubAccount` | `nvarchar(50)` | YES | `-` | - | - |
| `FlightInstructionTypeEnabled` | `bit` | **NO** | `-` | - | - |
| `GroundInstructionTypeEnabled` | `bit` | **NO** | `-` | - | - |
| `SubscriptionTypeId` | `uniqueidentifier` | YES | `-` | - | - |
| `CCInvalid` | `bit` | YES | `-` | - | - |
| `CancellationDate` | `datetime(3)` | YES | `-` | - | - |
| `AccountingSyncPackage` | `nvarchar(25)` | YES | `-` | - | - |
| `AccountingSyncEnabled` | `bit` | YES | `-` | - | - |
| `AccoutingSyncConfig` | `nvarchar(MAX)` | YES | `-` | - | - |
| `AccountingSyncConfigExpiration` | `datetime(3)` | YES | `-` | - | - |
| `AccountingApiPassword` | `uniqueidentifier` | YES | `-` | - | - |
| `AccountingSyncNextRuntime` | `datetime(3)` | YES | `-` | - | - |
| `StandardAircraftRentalRateInvoicingAccountId` | `uniqueidentifier` | YES | `-` | - | - |
| `OwnerAircraftRentalRateEnabled` | `bit` | YES | `-` | - | - |
| `OwnerAircraftRentalRateInvoicingAccountId` | `uniqueidentifier` | YES | `-` | - | - |
| `FlightInstructionTypeInvoicingAccountId` | `uniqueidentifier` | YES | `-` | - | - |
| `GroundInstructionTypeInvoicingAccountId` | `uniqueidentifier` | YES | `-` | - | - |
| `FlightInstructionTypeBillable` | `bit` | YES | `-` | - | - |
| `GroundInstructionTypeBillable` | `bit` | YES | `-` | - | - |
| `InvoiceBillingSignupAllowed` | `bit` | YES | `-` | - | - |
| `AccountingLastPingUtc` | `datetime(3)` | YES | `-` | - | - |
| `AccountingLastPingIpAddress` | `nvarchar(50)` | YES | `-` | - | - |
| `AccountingLastAuthenticationUtc` | `datetime(3)` | YES | `-` | - | - |
| `AccountingLastAuthenticationUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `AccountingApiPasswordGeneratedAtUtc` | `datetime(3)` | YES | `-` | - | - |
| `CurrentDocumentUploadProviderId` | `int(10,0)` | **NO** | `-` | - | - |
| `PlanDowngradeDate` | `datetime(3)` | YES | `-` | - | - |
| `DocumentUploadsDeletedAfterCancellation` | `datetime(3)` | YES | `-` | - | - |
| `DocumentUploadsDeletedAfterDowngrade` | `datetime(3)` | YES | `-` | - | - |
| `HubSpotId` | `bigint(19,0)` | YES | `-` | - | - |
| `RemoveHubSpotSync` | `datetime(3)` | YES | `-` | - | - |
| `GroundAllSquawks` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `OperatorSize` | `int(10,0)` | YES | `-` | - | - |
| `ApiAccessEnabled` | `bit` | **NO** | `-` | - | - |
| `LogiAnalysisCreated` | `int(10,0)` | **NO** | `-` | - | - |
| `LogiDashboardsCreated` | `int(10,0)` | **NO** | `-` | - | - |
| `LogiCustomReportsCreated` | `int(10,0)` | **NO** | `-` | - | - |
| `LogiReportingItemsShared` | `int(10,0)` | **NO** | `-` | - | - |
| `LogiReportingItemsScheduled` | `int(10,0)` | **NO** | `-` | - | - |
| `MaintenanceHubEnabled` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblCompany`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
