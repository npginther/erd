# SalesTransactionsDeleted

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (54)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `SalesTransactionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TransactionNumber` | `int(10,0)` | **NO** | `-` | - | - |
| `TransactionType` | `int(10,0)` | **NO** | `-` | - | - |
| `Status` | `int(10,0)` | **NO** | `-` | - | - |
| `TotalDue` | `decimal(11,2)` | YES | `-` | - | - |
| `TotalPaid` | `decimal(11,2)` | YES | `-` | - | - |
| `AccuralSalesTotal` | `decimal(11,2)` | YES | `-` | - | - |
| `Date` | `datetime(3)` | YES | `-` | - | - |
| `LocationId` | `int(10,0)` | YES | `-` | - | - |
| `CustomerUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `CreatedByUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `CustomerMessage` | `text(2147483647)` | YES | `-` | - | - |
| `InternalNotes` | `text(2147483647)` | YES | `-` | - | - |
| `DiscountGroupId` | `uniqueidentifier` | YES | `-` | - | - |
| `DiscountGroupName` | `nvarchar(200)` | YES | `-` | - | - |
| `AircraftDiscount` | `decimal(5,2)` | YES | `-` | - | - |
| `InstructionDiscount` | `decimal(5,2)` | YES | `-` | - | - |
| `ProductsDiscount` | `decimal(5,2)` | YES | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | YES | `-` | - | - |
| `TailNumber` | `nvarchar(25)` | YES | `-` | - | - |
| `InstructorId` | `uniqueidentifier` | YES | `-` | - | - |
| `InstructorName` | `nvarchar(100)` | YES | `-` | - | - |
| `CustomerName` | `nvarchar(100)` | YES | `-` | - | - |
| `EmployeeName` | `nvarchar(100)` | YES | `-` | - | - |
| `ReservationId` | `uniqueidentifier` | YES | `-` | - | - |
| `ReturnInvoiceId` | `uniqueidentifier` | YES | `-` | - | - |
| `TotalReturned` | `decimal(11,2)` | YES | `-` | - | - |
| `AccountingInvoiceId` | `nvarchar(100)` | YES | `-` | - | - |
| `Locked` | `bit` | YES | `-` | - | - |
| `BatchSyncId` | `uniqueidentifier` | YES | `-` | - | - |
| `AccountingSyncStatus` | `int(10,0)` | YES | `-` | - | - |
| `PurchaseMethod` | `int(10,0)` | **NO** | `-` | - | - |
| `DiscountGroupMinimum` | `decimal(11,2)` | YES | `-` | - | - |
| `LocationName` | `nvarchar(50)` | YES | `-` | - | - |
| `LocationPhone` | `nvarchar(50)` | YES | `-` | - | - |
| `LocationAddress` | `nvarchar(500)` | YES | `-` | - | - |
| `LocationEmail` | `nvarchar(150)` | YES | `-` | - | - |
| `LocationAdditionalInformation` | `text(2147483647)` | YES | `-` | - | - |
| `IsFuelReimbursement` | `bit` | **NO** | `-` | - | - |
| `ReservationNumber` | `bigint(19,0)` | YES | `-` | - | - |
| `ResultingAccountBalance` | `decimal(11,2)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `ActivityDate` | `datetime(3)` | YES | `-` | - | - |
| `ReservationForName` | `nvarchar(100)` | YES | `-` | - | - |
| `ReservationForGroupName` | `nvarchar(200)` | YES | `-` | - | - |
| `CreatedAt` | `datetime(3)` | YES | `-` | - | - |
| `DeletedBy` | `uniqueidentifier` | **NO** | `-` | - | - |
| `DeletedAtUtc` | `datetime(3)` | **NO** | `-` | - | - |
| `ReservationForUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `ReservationForPeopleGroupId` | `uniqueidentifier` | YES | `-` | - | - |
| `CustomerPeopleGroupId` | `uniqueidentifier` | YES | `-` | - | - |
| `CustomerPeopleGroupName` | `nvarchar(200)` | YES | `-` | - | - |

## Indexes

- **`PK_SalesTransactionsDeleted`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`UK_SalesTransactionsDeleted`** (UNIQUE NONCLUSTERED)
  - Columns: `OperatorId, SalesTransactionId`
