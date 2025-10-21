# tblAircraftRatingsCertsEndorsements

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (23)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `SoloRating` | `bit` | **NO** | `-` | - | - |
| `PrivateRating` | `bit` | **NO** | `-` | - | - |
| `CommercialRating` | `bit` | **NO** | `-` | - | - |
| `ATPCertificate` | `bit` | **NO** | `-` | - | - |
| `MERating` | `bit` | **NO** | `-` | - | - |
| `InstrumentRating` | `bit` | **NO** | `-` | - | - |
| `SeaPlaneRating` | `bit` | **NO** | `-` | - | - |
| `HelicopterRating` | `bit` | **NO** | `-` | - | - |
| `ComplexEndorsement` | `bit` | **NO** | `-` | - | - |
| `HighPerformanceEndorsement` | `bit` | **NO** | `-` | - | - |
| `PressurizedEndorsement` | `bit` | **NO** | `-` | - | - |
| `TailWheelEndorsement` | `bit` | **NO** | `-` | - | - |
| `CFII` | `bit` | **NO** | `-` | - | - |
| `CFIME` | `bit` | **NO** | `-` | - | - |
| `IFRCertified` | `bit` | **NO** | `-` | - | - |
| `CFI` | `bit` | **NO** | `-` | - | - |
| `Sport` | `bit` | **NO** | `-` | - | - |
| `Student` | `bit` | **NO** | `-` | - | - |
| `Recreational` | `bit` | **NO** | `-` | - | - |
| `CFISP` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_tblAircraftRatingsCertsEndorsements`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AircraftId`
