# tblFlightRecordResources

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `FlightRecordId` | `uniqueidentifier` | **NO** | `-` | PK<br/>FK->`tblFlightRecord` | - |
| `ItemId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `ResourceType` | `int(10,0)` | **NO** | `-` | - | - |
| `_RowId` | `bigint(19,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblFlightRecord`** 
  via `FlightRecordId` → `FlightRecordId` `ON DELETE CASCADE`

## Indexes

- **`CX_tblFlightRecordResources`** (UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`PK_tblFlightRecordResources`** (PRIMARY KEY UNIQUE NONCLUSTERED)
  - Columns: `FlightRecordId, ItemId`
- **`ix_FlightRecordId_CompanyId_Includes`** (NONCLUSTERED)
  - Columns: `FlightRecordId, CompanyId INCLUDE (ItemId, ResourceType)`
- **`ix_ItemId_CompanyId_Includes`** (NONCLUSTERED)
  - Columns: `ItemId, CompanyId INCLUDE (FlightRecordId)`
