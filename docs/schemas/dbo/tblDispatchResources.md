# tblDispatchResources

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `DispatchId` | `uniqueidentifier` | **NO** | `-` | PK<br/>FK->`tblDispatchRecords` | - |
| `ItemId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `ResourceType` | `int(10,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblDispatchRecords`** 
  via `DispatchId` → `Id` `ON DELETE CASCADE`

## Indexes

- **`PK_tblDispatchResources`** (PRIMARY KEY UNIQUE NONCLUSTERED)
  - Columns: `DispatchId, ItemId`
