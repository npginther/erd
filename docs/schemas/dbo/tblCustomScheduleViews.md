# tblCustomScheduleViews

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (8)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `PersonId` | `int(10,0)` | **NO** | `-` | - | - |
| `DefaultView` | `bit` | **NO** | `-` | - | - |
| `Name` | `varchar(150)` | **NO** | `-` | - | - |
| `Data` | `text(2147483647)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblCustomScheduleViews`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
- **`ix_tblCustomScheduleViews_CompanyId_PersonId`** (NONCLUSTERED)
  - Columns: `CompanyId, PersonId`
