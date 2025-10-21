# tblAddressPartsType

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (8)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AddressPartsTypeId` | `int(10,0)` | **NO** | `-` | PK | - |
| `CountryId` | `int(10,0)` | **NO** | `-` | - | - |
| `PartNumber` | `int(10,0)` | **NO** | `-` | - | - |
| `Label` | `varchar(75)` | **NO** | `-` | - | - |
| `IsRequired` | `bit` | **NO** | `-` | - | - |
| `ValidationString` | `varchar(250)` | **NO** | `-` | - | - |
| `ValidationTable` | `varchar(50)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblAddressPartsType`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AddressPartsTypeId`
