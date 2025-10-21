# tblAddressFormat

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (3)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `CountryId` | `int(10,0)` | **NO** | `-` | PK | - |
| `AddressFormatString` | `varchar(500)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblAddressFormat`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `CountryId`
