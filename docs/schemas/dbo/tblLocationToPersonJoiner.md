# tblLocationToPersonJoiner

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `LocationId` | `int(10,0)` | **NO** | `-` | PK<br/>FK->`tblLocations` | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `PersonId` | `int(10,0)` | **NO** | `-` | PK | - |
| `Approved` | `bit` | **NO** | `-` | - | - |
| `IsDefault` | `bit` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblLocations`** 
  via `LocationId` → `Id` `ON DELETE CASCADE`

## Indexes

- **`IDX_tblLocationToPersonJoiner_PersonId`** (NONCLUSTERED)
  - Columns: `PersonId`
- **`PK_tblLocationToPersonJoiner`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `LocationId, PersonId`
- **`ix_tblLocationToPersonJoiner_CompanyId_Approved`** (NONCLUSTERED)
  - Columns: `CompanyId, Approved`
