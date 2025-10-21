# tblInvoicingPreferences

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (120)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `CompanyId` | `int(10,0)` | **NO** | `-` | PK | - |
| `CurrencyCode` | `nvarchar(3)` | **NO** | `-` | - | - |
| `CurrencySymbol` | `nvarchar(10)` | **NO** | `-` | - | - |
| `DefaultTerms` | `text(2147483647)` | **NO** | `-` | - | - |
| `ProcessorType` | `uniqueidentifier` | YES | `-` | - | - |
| `ProcessorConfig` | `text(2147483647)` | **NO** | `-` | - | - |
| `AircraftInvoicingMeter` | `int(10,0)` | **NO** | `-` | - | - |
| `AllowableBalanceToMakeReservations` | `decimal(9,2)` | YES | `-` | - | - |
| `CustomerCanViewBalanceAndTransactions` | `bit` | **NO** | `-` | - | - |
| `CashPaymentEnabled` | `bit` | YES | `-` | - | - |
| `CheckPaymentEnabled` | `bit` | YES | `-` | - | - |
| `AccountPaymentEnabled` | `bit` | YES | `-` | - | - |
| `GiftCardPaymentEnabled` | `bit` | YES | `-` | - | - |
| `CCNoAuthEnabled` | `bit` | YES | `-` | - | - |
| `CCKeyedEnabled` | `bit` | YES | `-` | - | - |
| `CCSwipeEnabled` | `bit` | YES | `-` | - | - |
| `TrackLocations` | `bit` | YES | `-` | - | - |
| `TrackFuelReimbursements` | `bit` | YES | `-` | - | - |
| `FuelReimbursementAccountId` | `uniqueidentifier` | YES | `-` | - | - |
| `InvoiceLogoHash` | `nvarchar(100)` | YES | `-` | - | - |
| `FuelReimbursementAccountingId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountPaymentAccountingId` | `nvarchar(100)` | YES | `-` | - | - |
| `FuelReimbursementAccountingName` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountPaymentAccountingName` | `nvarchar(100)` | YES | `-` | - | - |
| `CheckingAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `CheckingAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountsReceivableAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountsReceivableAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `InvoiceLineItemDiscountAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `InvoiceLineItemDiscountAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `CashPaymentMethodAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `CashPaymentMethodAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `CashPaymentMethodDepositToAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `CashPaymentMethodDepositToAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `CheckPaymentMethodAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `CheckPaymentMethodAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `CheckPaymentMethodDepositToAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `CheckPaymentMethodDepositToAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `CcNoAuthPaymentMethodAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `CcNoAuthPaymentMethodAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `CcNoAuthPaymentMethodDepositToAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `CcNoAuthPaymentMethodDepositToAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `VisaPaymentMethodAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `VisaPaymentMethodAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `VisaPaymentMethodDepositToAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `VisaPaymentMethodDepositToAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `MastercardPaymentMethodAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `MastercardPaymentMethodAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `MastercardPaymentMethodDepositToAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `MastercardPaymentMethodDepositToAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `DiscoverPaymentMethodAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `DiscoverPaymentMethodAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `DiscoverPaymentMethodDepositToAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `DiscoverPaymentMethodDepositToAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `AmexPaymentMethodAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `AmexPaymentMethodAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `AmexPaymentMethodDepositToAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `AmexPaymentMethodDepositToAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `CashPaymentMethodQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `CashPaymentMethodQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `CashPaymentMethodDepositToQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `CashPaymentMethodDepositToQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `CheckPaymentMethodQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `CheckPaymentMethodQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `CheckPaymentMethodDepositToQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `CheckPaymentMethodDepositToQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `CcNoAuthPaymentMethodQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `CcNoAuthPaymentMethodQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `CcNoAuthPaymentMethodDepositToQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `CcNoAuthPaymentMethodDepositToQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `VisaPaymentMethodQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `VisaPaymentMethodQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `VisaPaymentMethodDepositToQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `VisaPaymentMethodDepositToQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `MastercardPaymentMethodQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `MastercardPaymentMethodQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `MastercardPaymentMethodDepositToQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `MastercardPaymentMethodDepositToQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `DiscoverPaymentMethodQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `DiscoverPaymentMethodQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `DiscoverPaymentMethodDepositToQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `DiscoverPaymentMethodDepositToQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `AmexPaymentMethodQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `AmexPaymentMethodQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `AmexPaymentMethodDepositToQBDAccountId` | `nvarchar(200)` | YES | `-` | - | - |
| `AmexPaymentMethodDepositToQBDAccountName` | `nvarchar(200)` | YES | `-` | - | - |
| `InvoiceLineItemDiscountQBDAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `InvoiceLineItemDiscountQBDAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountPaymentQBDAccountingId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountPaymentQBDAccountingName` | `nvarchar(100)` | YES | `-` | - | - |
| `FuelReimbursementQBDAccountingId` | `nvarchar(100)` | YES | `-` | - | - |
| `FuelReimbursementQBDAccountingName` | `nvarchar(100)` | YES | `-` | - | - |
| `BonusReturnQBDAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `BonusReturnQBDAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountsReceivableQBDAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountsReceivableQBDAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `FuelReimbursementQBDTaxReferenceId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountPaymentQBDTaxReferenceId` | `nvarchar(100)` | YES | `-` | - | - |
| `FuelReimbursementQBDARAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `FuelReimbursementQBDARAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `AutoSendStatements` | `bit` | **NO** | `-` | - | - |
| `SendStatementsToUserWithBalanceOnly` | `bit` | **NO** | `-` | - | - |
| `SendStatementsToUserWithActivityOnly` | `bit` | **NO** | `-` | - | - |
| `SendStatementsToTheseRoleIdsOnly` | `nvarchar(MAX)` | YES | `-` | - | - |
| `StatementPhone` | `nvarchar(50)` | YES | `-` | - | - |
| `StatementEmail` | `nvarchar(255)` | YES | `-` | - | - |
| `StatementAddress` | `nvarchar(MAX)` | YES | `-` | - | - |
| `StatementDefaultMessage` | `nvarchar(MAX)` | YES | `-` | - | - |
| `StatementLogoHash` | `nvarchar(100)` | YES | `-` | - | - |
| `RefundBankAccountQBDAccountId` | `nvarchar(100)` | YES | `-` | - | - |
| `RefundBankAccountQBDAccountName` | `nvarchar(100)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `WirePaymentEnabled` | `bit` | YES | `-` | - | - |
| `CreditMemoTaxAccountingId` | `nvarchar(200)` | YES | `-` | - | - |
| `CreditMemoTaxAccountingName` | `nvarchar(200)` | YES | `-` | - | - |
| `CreditMemoItemAccountingId` | `nvarchar(200)` | YES | `-` | - | - |
| `CreditMemoItemAccountingName` | `nvarchar(200)` | YES | `-` | - | - |
| `DebitMemoItemAccountingId` | `nvarchar(200)` | YES | `-` | - | - |
| `DebitMemoItemAccountingName` | `nvarchar(200)` | YES | `-` | - | - |

## Indexes

- **`PK_tblInvoicingPreferences`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `CompanyId`
