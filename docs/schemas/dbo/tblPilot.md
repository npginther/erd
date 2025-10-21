# tblPilot

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (14)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PilotId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `PersonId` | `int(10,0)` | **NO** | `-` | - | - |
| `MedicalCertificateNumber` | `varchar(50)` | **NO** | `-` | - | - |
| `MedicalCertificateDate` | `varchar(20)` | **NO** | `-` | - | - |
| `MedicalCertificateType` | `int(10,0)` | **NO** | `-` | - | - |
| `BiennialFlightReview` | `varchar(20)` | **NO** | `-` | - | - |
| `LastFlight` | `varchar(20)` | **NO** | `-` | - | - |
| `SoloEndorsement` | `varchar(20)` | **NO** | `-` | - | - |
| `TotalHours` | `decimal(9,2)` | **NO** | `-` | - | - |
| `UserGUIDId` | `uniqueidentifier` | YES | `-` | - | - |
| `IsAStaffPilot` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_tblPilot_CompanyId`** (NONCLUSTERED)
  - Columns: `CompanyId`
- **`IDX_tblPilot_PersonId_PilotId`** (NONCLUSTERED)
  - Columns: `PersonId INCLUDE (PilotId)`
- **`IDX_tblPilot_UserGuidId_PilotId`** (NONCLUSTERED)
  - Columns: `UserGUIDId INCLUDE (PilotId)`
- **`PK_tblPilot`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PilotId`
- **`ix_CompanyId_Includes`** (NONCLUSTERED)
  - Columns: `CompanyId INCLUDE (PersonId)`
