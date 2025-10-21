# PilotMedicalCertificate

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (16)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PilotId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `MedicalCertificateNumber` | `nvarchar(50)` | **NO** | `-` | - | - |
| `MedicalCertificateDate` | `datetime(3)` | YES | `-` | - | - |
| `MedicalCertificateType` | `int(10,0)` | **NO** | `-` | - | - |
| `FirstClassExpiration` | `datetime(3)` | YES | `-` | - | - |
| `SecondClassExpiration` | `datetime(3)` | YES | `-` | - | - |
| `ThirdClassExpiration` | `datetime(3)` | YES | `-` | - | - |
| `Restrictions` | `nvarchar(MAX)` | YES | `-` | - | - |
| `NotRequired` | `bit` | YES | `-` | - | - |
| `Revoked` | `bit` | **NO** | `-` | - | - |
| `DriversLicenseExpirationDate` | `datetime(3)` | YES | `-` | - | - |
| `HasHeldMedicalAfterJuly152006` | `bit` | YES | `-` | - | - |
| `MedicalEducationCourseDate` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_PilotMedicalCertificate`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PilotId`
