# SalesTransactionLineItemsDeleted

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (52)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `SalesTransactionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LineItemId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LineItemType` | `int(10,0)` | **NO** | `-` | - | - |
| `SalesTransactionDate` | `datetime(3)` | YES | `-` | - | - |
| `Quantity` | `decimal(8,2)` | YES | `-` | - | - |
| `UnitCost` | `decimal(15,6)` | YES | `-` | - | - |
| `GrossAmount` | `decimal(11,2)` | YES | `-` | - | - |
| `DiscountAmount` | `decimal(11,2)` | YES | `-` | - | - |
| `TaxableAmount` | `decimal(11,2)` | YES | `-` | - | - |
| `Tax1Amount` | `decimal(11,2)` | YES | `-` | - | - |
| `Tax2Amount` | `decimal(11,2)` | YES | `-` | - | - |
| `NetAmount` | `decimal(11,2)` | YES | `-` | - | - |
| `AccountId` | `uniqueidentifier` | YES | `-` | - | - |
| `Name` | `nvarchar(75)` | YES | `-` | - | - |
| `Note` | `nvarchar(500)` | YES | `-` | - | - |
| `OriginalUnitCost` | `decimal(15,6)` | YES | `-` | - | - |
| `DiscountType` | `int(10,0)` | YES | `-` | - | - |
| `DiscountValue` | `decimal(11,2)` | YES | `-` | - | - |
| `Tax1Id` | `uniqueidentifier` | YES | `-` | - | - |
| `Tax1Name` | `nvarchar(150)` | YES | `-` | - | - |
| `Tax1Percent` | `decimal(6,4)` | YES | `-` | - | - |
| `Tax2Id` | `uniqueidentifier` | YES | `-` | - | - |
| `Tax2Name` | `nvarchar(150)` | YES | `-` | - | - |
| `Tax2Percent` | `decimal(6,4)` | YES | `-` | - | - |
| `CustomDiscount` | `bit` | YES | `-` | - | - |
| `ProductId` | `uniqueidentifier` | YES | `-` | - | - |
| `ResourceId` | `uniqueidentifier` | YES | `-` | - | - |
| `ResourceType` | `int(10,0)` | YES | `-` | - | - |
| `ResourceName` | `nvarchar(100)` | YES | `-` | - | - |
| `RentalRateTypeId` | `int(10,0)` | YES | `-` | - | - |
| `InstructionTypeId` | `uniqueidentifier` | YES | `-` | - | - |
| `InstructionTypeName` | `nvarchar(50)` | YES | `-` | - | - |
| `InvoiceId` | `uniqueidentifier` | YES | `-` | - | - |
| `AccountPaymentId` | `uniqueidentifier` | YES | `-` | - | - |
| `AccountCreditValue` | `decimal(11,2)` | YES | `-` | - | - |
| `Description` | `nvarchar(500)` | YES | `-` | - | - |
| `AircraftMake` | `nvarchar(150)` | YES | `-` | - | - |
| `AircraftModel` | `nvarchar(150)` | YES | `-` | - | - |
| `CreditMustEqualPrice` | `bit` | YES | `-` | - | - |
| `ReturnAgainstLineItemId` | `uniqueidentifier` | YES | `-` | - | - |
| `ReturnAgainstSalesTransactionId` | `uniqueidentifier` | YES | `-` | - | - |
| `ItemTypeId` | `int(10,0)` | YES | `-` | - | - |
| `ServiceTypeId` | `int(10,0)` | YES | `-` | - | - |
| `TransactionType` | `int(10,0)` | YES | `-` | - | - |
| `AircraftBillingMeter` | `nvarchar(25)` | YES | `-` | - | - |
| `AircraftRateTypeId` | `uniqueidentifier` | YES | `-` | - | - |
| `AircraftRateTypeName` | `nvarchar(100)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `DeletedBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `DeletedAtUtc` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_SalesTransactionLineItemsDeleted`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`UK_SalesTransactionLineItemsDeleted`** (UNIQUE NONCLUSTERED)
  - Columns: `OperatorId, SalesTransactionId, LineItemId`
