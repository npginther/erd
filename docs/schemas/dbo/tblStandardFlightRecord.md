# tblStandardFlightRecord

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (15)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `FlightRecordId` | `uniqueidentifier` | **NO** | `-` | PK<br/>FK->`tblFlightRecord` | - |
| `InstructorPreFlightMinutes` | `int(10,0)` | **NO** | `-` | - | - |
| `InstructorPostFlightMinutes` | `int(10,0)` | **NO** | `-` | - | - |
| `InstructionHours` | `decimal(5,2)` | **NO** | `-` | - | - |
| `PreFlightInstructionHours` | `decimal(5,2)` | **NO** | `-` | - | - |
| `PostFlightInstructionHours` | `decimal(5,2)` | **NO** | `-` | - | - |
| `ExpectedFlightHours` | `decimal(5,2)` | **NO** | `-` | - | - |
| `IsCrossCountry` | `bit` | **NO** | `-` | - | - |
| `IsVFR` | `bit` | **NO** | `-` | - | - |
| `FlightRoute` | `varchar(500)` | **NO** | `-` | - | - |
| `ReferenceNumber` | `varchar(25)` | **NO** | `-` | - | - |
| `InvoiceId` | `uniqueidentifier` | YES | `-` | - | - |
| `_RowId` | `bigint(19,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Foreign Key Relationships

### This Table References (Parent Tables):

- **`dbo.tblFlightRecord`** 
  via `FlightRecordId` → `FlightRecordId` `ON DELETE CASCADE`

## Indexes

- **`CX_tblStandardFlightRecord`** (UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`PK_tblStandardFlightRecord`** (PRIMARY KEY UNIQUE NONCLUSTERED)
  - Columns: `FlightRecordId`
