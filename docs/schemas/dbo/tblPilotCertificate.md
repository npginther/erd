# tblPilotCertificate

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (40)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PilotId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CertificateNumber` | `varchar(50)` | **NO** | `-` | - | - |
| `CertificateDate` | `varchar(20)` | **NO** | `-` | - | - |
| `Sport` | `bit` | **NO** | `-` | - | - |
| `Private` | `bit` | **NO** | `-` | - | - |
| `Commercial` | `bit` | **NO** | `-` | - | - |
| `AirlineTransport` | `bit` | **NO** | `-` | - | - |
| `CFI` | `bit` | **NO** | `-` | - | - |
| `CFII` | `bit` | **NO** | `-` | - | - |
| `CFIME` | `bit` | **NO** | `-` | - | - |
| `Solo` | `bit` | **NO** | `-` | - | - |
| `MultiEngine` | `bit` | **NO** | `-` | - | - |
| `InstrumentRating` | `bit` | **NO** | `-` | - | - |
| `SeaPlane` | `bit` | **NO** | `-` | - | - |
| `Helicopter` | `bit` | **NO** | `-` | - | - |
| `Complex` | `bit` | **NO** | `-` | - | - |
| `HighPerformance` | `bit` | **NO** | `-` | - | - |
| `Pressurized` | `bit` | **NO** | `-` | - | - |
| `TailWheel` | `bit` | **NO** | `-` | - | - |
| `Student` | `bit` | **NO** | `-` | - | - |
| `Recreational` | `bit` | **NO** | `-` | - | - |
| `CFI-SP` | `bit` | **NO** | `-` | - | - |
| `CertificateType` | `int(10,0)` | **NO** | `-` | - | - |
| `ASEL` | `bit` | **NO** | `-` | - | - |
| `AMEL` | `bit` | **NO** | `-` | - | - |
| `ASES` | `bit` | **NO** | `-` | - | - |
| `AMES` | `bit` | **NO** | `-` | - | - |
| `GYRO` | `bit` | **NO** | `-` | - | - |
| `LTAA` | `bit` | **NO** | `-` | - | - |
| `LTAB` | `bit` | **NO** | `-` | - | - |
| `PPL` | `bit` | **NO** | `-` | - | - |
| `PPS` | `bit` | **NO** | `-` | - | - |
| `WSCL` | `bit` | **NO** | `-` | - | - |
| `WSCS` | `bit` | **NO** | `-` | - | - |
| `SoloExpiration` | `datetime(3)` | YES | `-` | - | - |
| `StudentExpiration` | `datetime(3)` | YES | `-` | - | - |
| `Restrictions` | `nvarchar(MAX)` | YES | `-` | - | - |
| `GLIDER` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_tblPilotCertificate`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PilotId`
