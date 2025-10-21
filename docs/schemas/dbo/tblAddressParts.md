# tblAddressParts

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AddressPartId` | `int(10,0)` | **NO** | `-` | PK | - |
| `AddressId` | `int(10,0)` | **NO** | `-` | FK->`tblAddress` | - |
| `AddressPartsTypeId` | `int(10,0)` | **NO** | `-` | - | - |
| `Data` | `nvarchar(100)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblAddress`** 
  via `AddressId` → `AddressId` `ON DELETE CASCADE`

## Indexes

- **`IDX_tblAddressParts_AddressId`** (NONCLUSTERED)
  - Columns: `AddressId`
- **`PK_tblAddressParts`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AddressPartId`
