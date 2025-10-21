# tblPostItems

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (16)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `ID` | `int(10,0)` | **NO** | `-` | PK | - |
| `PostDate` | `datetime(3)` | **NO** | `-` | - | - |
| `Title` | `varchar(100)` | **NO** | `-` | - | - |
| `Description` | `varchar(100)` | YES | `-` | - | - |
| `Body` | `varchar(8000)` | **NO** | `-` | - | - |
| `PostUntilDate` | `datetime(3)` | YES | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `IsNews` | `bit` | YES | `-` | - | - |
| `IsBulletinBoard` | `bit` | YES | `-` | - | - |
| `IsAlert` | `bit` | YES | `-` | - | - |
| `StartDate` | `datetime(3)` | YES | `-` | - | - |
| `Author` | `varchar(150)` | **NO** | `-` | - | - |
| `IsSaved` | `bit` | **NO** | `-` | - | - |
| `CreatedByUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

### Referenced By (Child Tables):

- **`dbo.tblPostItemRoleIds`** 
  via `PostItemId` → `ID`

## Indexes

- **`IDX_tblPostItems_CompanyIdIsBulletinBoardPostUntilDateStartDate`** (NONCLUSTERED)
  - Columns: `CompanyId, IsBulletinBoard, PostUntilDate, StartDate`
- **`PK_tblPostItems`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `ID`
