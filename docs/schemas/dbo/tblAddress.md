# tblAddress

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (4)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AddressId` | `int(10,0)` | **NO** | `-` | PK | - |
| `CountryId` | `int(10,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.tblCompanyAddressJoiner`** 
  via `AddressId` → `AddressId`
- **`dbo.tblAddressParts`** 
  via `AddressId` → `AddressId`
- **`dbo.tblPersonAddressJoiner`** 
  via `AddressId` → `AddressId`

## Indexes

- **`PK_tblAddress`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AddressId`
