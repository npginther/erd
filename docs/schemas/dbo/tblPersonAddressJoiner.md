# tblPersonAddressJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PersonId` | `int(10,0)` | **NO** | `-` | PK | - |
| `AddressTypeId` | `int(10,0)` | **NO** | `-` | PK | - |
| `AddressId` | `int(10,0)` | **NO** | `-` | PK<br/>FK->`tblAddress` | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblAddress`** 
  via `AddressId` → `AddressId` `ON DELETE CASCADE`

## Indexes

- **`PK_tblPersonAddressJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PersonId, AddressTypeId, AddressId`
