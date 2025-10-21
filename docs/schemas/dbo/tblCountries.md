# tblCountries

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `int(10,0)` | **NO** | `-` | PK | - |
| `CountryName` | `varchar(50)` | **NO** | `-` | - | - |
| `DisplayOrderId` | `int(10,0)` | **NO** | `-` | - | - |
| `Abbreviation` | `char(2)` | **NO** | `-` | - | - |
| `Abbreviation-3char` | `char(3)` | **NO** | `-` | - | - |
| `TopLevelDomain` | `char(2)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_Countries`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
