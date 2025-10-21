# tblMeterRecords

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (15)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `MeterRecordId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `FlightRecordId` | `uniqueidentifier` | **NO** | `-` | FK->`tblFlightRecord` | - |
| `MeterType` | `int(10,0)` | **NO** | `-` | - | - |
| `MeterIndex` | `int(10,0)` | **NO** | `-` | - | - |
| `MeterInValue` | `decimal(9,2)` | **NO** | `-` | - | - |
| `MeterOutValue` | `decimal(9,2)` | **NO** | `-` | - | - |
| `MeterOutOriginal` | `decimal(9,2)` | **NO** | `-` | - | - |
| `MeterOutVerified` | `bit` | **NO** | `-` | - | - |
| `MeterOutVerifiedByUserId` | `uniqueidentifier` | YES | `-` | - | - |
| `_RowId` | `bigint(19,0)` | **NO** | `-` | - | - |
| `MeterInMismatch` | `bit` | YES | `-` | - | - |
| `MeterOutMismatch` | `bit` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |
| `MeterFormat` | `int(10,0)` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblFlightRecord`** 
  via `FlightRecordId` → `FlightRecordId` `ON DELETE CASCADE`

## Indexes

- **`CX_tblMeterRecords`** (UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`IDX_tblMeterRecords_FlightRecordId`** (NONCLUSTERED)
  - Columns: `FlightRecordId`
- **`PK_tblMeterRecords`** (PRIMARY KEY UNIQUE NONCLUSTERED)
  - Columns: `MeterRecordId`
