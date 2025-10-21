# tblSquawk

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (24)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TailNumber` | `varchar(10)` | **NO** | `-` | - | - |
| `TachHours` | `decimal(16,2)` | **NO** | `-` | - | - |
| `Discrepancy` | `varchar(1000)` | **NO** | `-` | - | - |
| `SubmittedBy` | `varchar(50)` | **NO** | `-` | - | - |
| `DateSubmitted` | `datetime(3)` | **NO** | `-` | - | - |
| `IsGroundable` | `bit` | **NO** | `-` | - | - |
| `CorrectiveAction` | `varchar(1000)` | **NO** | `-` | - | - |
| `CorrectedBy` | `varchar(50)` | **NO** | `-` | - | - |
| `CorrectedByCertificateNumber` | `varchar(25)` | **NO** | `-` | - | - |
| `DateCorrected` | `datetime(3)` | **NO** | `-` | - | - |
| `InspectedBy` | `varchar(50)` | **NO** | `-` | - | - |
| `InspectedByCertificateNumber` | `varchar(25)` | **NO** | `-` | - | - |
| `InspectionDate` | `datetime(3)` | **NO** | `-` | - | - |
| `Resolution` | `int(10,0)` | **NO** | `-` | - | - |
| `UserName` | `varchar(50)` | **NO** | `-` | - | - |
| `FlightRecordId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CustomSquawkResolutionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `SubmittedByUserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `SubmittedAtUtc` | `datetime2(7)` | YES | `-` | - | - |

## Indexes

- **`IDX_tblSquawk_DateSubmitted`** (NONCLUSTERED)
  - Columns: `DateSubmitted INCLUDE (AircraftId, CustomSquawkResolutionId, Discrepancy, IsGroundable, Resolution, SubmittedBy, TailNumber)`
- **`IDX_tblSquawk_SubmittedAtUtc`** (NONCLUSTERED)
  - Columns: `SubmittedAtUtc INCLUDE (AircraftId, CustomSquawkResolutionId, Discrepancy, IsGroundable, Resolution, SubmittedBy, TailNumber)`
- **`PK_tblSquawk`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
- **`ix_tblSquawk_CompanyId_AircraftId_IsGroundable`** (NONCLUSTERED)
  - Columns: `CompanyId, AircraftId, IsGroundable`
- **`ix_tblSquawk_FlightRecordId`** (NONCLUSTERED)
  - Columns: `FlightRecordId`
