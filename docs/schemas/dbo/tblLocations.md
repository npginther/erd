# tblLocations

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `int(10,0)` | **NO** | `-` | PK | - |
| `Name` | `varchar(50)` | **NO** | `-` | - | - |
| `PhoneNumber` | `varchar(20)` | **NO** | `-` | - | - |
| `EmailAddress` | `varchar(64)` | **NO** | `-` | - | - |
| `LocationIdent` | `varchar(15)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.tblLocationToCompanyJoiner`** 
  via `LocationId` → `Id`
- **`dbo.tblLocationToPersonJoiner`** 
  via `LocationId` → `Id`
- **`dbo.LocationToIcaoLocationsJoiner`** 
  via `LocationId` → `Id`

## Indexes

- **`PK_tblLocations`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
