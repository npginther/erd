# tblInvoicingLineItems

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (24)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `LineItemId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Status` | `int(10,0)` | **NO** | `-` | - | - |
| `Description` | `varchar(500)` | **NO** | `-` | - | - |
| `UnitCost` | `decimal(15,6)` | **NO** | `-` | - | - |
| `ParentId` | `uniqueidentifier` | YES | `-` | - | - |
| `Name` | `varchar(100)` | **NO** | `-` | - | - |
| `AccountId` | `uniqueidentifier` | YES | `-` | - | - |
| `ItemTypeId` | `int(10,0)` | YES | `-` | - | - |
| `ServiceTypeId` | `int(10,0)` | YES | `-` | - | - |
| `RentalRateTypeId` | `int(10,0)` | YES | `-` | - | - |
| `InstructionTypeId` | `uniqueidentifier` | YES | `-` | - | - |
| `ResourceId` | `uniqueidentifier` | YES | `-` | - | - |
| `AccountingProductId` | `nvarchar(100)` | YES | `-` | - | - |
| `AccountingProductName` | `nvarchar(100)` | YES | `-` | - | - |
| `V4LineItem` | `bit` | YES | `-` | - | - |
| `TaxReferenceId` | `uniqueidentifier` | YES | `-` | - | - |
| `QBDAccountingProductId` | `nvarchar(200)` | YES | `-` | - | - |
| `QBDAccountingProductName` | `nvarchar(200)` | YES | `-` | - | - |
| `QBDTaxReferenceId` | `uniqueidentifier` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `FuelProductId` | `uniqueidentifier` | YES | `-` | - | - |
| `FuelUnitsPerHour` | `decimal(7,2)` | YES | `-` | - | - |

## Indexes

- **`IDX_CompanyIdStatusV4LineItem_LineItemIdDescriptionUnitCostNameItemTypeIdServiceTypeIdResourceId`** (NONCLUSTERED)
  - Columns: `CompanyId, Status, V4LineItem INCLUDE (Description, ItemTypeId, LineItemId, Name, ResourceId, ServiceTypeId, UnitCost)`
- **`IDX_tblInvoicingLineItems_CompanyIdStatusV4LineItemItemTypeId_Name`** (NONCLUSTERED)
  - Columns: `CompanyId, Status, V4LineItem, ItemTypeId INCLUDE (Name)`
- **`PK_tblInvoicingLineItems`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `LineItemId`
