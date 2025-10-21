# tblLocationToCompanyJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `int(10,0)` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | PK | - |
| `LocationId` | `int(10,0)` | **NO** | `-` | PK<br/>FK->`tblLocations` | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblLocations`** 
  via `LocationId` → `Id` `ON DELETE CASCADE`

## Indexes

- **`PK_tblLocationToCompanyJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `CompanyId, LocationId`
