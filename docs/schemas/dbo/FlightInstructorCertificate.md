# FlightInstructorCertificate

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (24)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `UserId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `CertificateNumber` | `nvarchar(50)` | **NO** | `-` | - | - |
| `IssuedDate` | `datetime(3)` | YES | `-` | - | - |
| `ExpirationDate` | `datetime(3)` | **NO** | `-` | - | - |
| `Restrictions` | `nvarchar(MAX)` | YES | `-` | - | - |
| `ASEL` | `bit` | **NO** | `-` | - | - |
| `AMEL` | `bit` | **NO** | `-` | - | - |
| `ASES` | `bit` | **NO** | `-` | - | - |
| `AMES` | `bit` | **NO** | `-` | - | - |
| `HELI` | `bit` | **NO** | `-` | - | - |
| `GYRO` | `bit` | **NO** | `-` | - | - |
| `LTAA` | `bit` | **NO** | `-` | - | - |
| `LTAB` | `bit` | **NO** | `-` | - | - |
| `PPL` | `bit` | **NO** | `-` | - | - |
| `PPS` | `bit` | **NO** | `-` | - | - |
| `WSCL` | `bit` | **NO** | `-` | - | - |
| `WSCS` | `bit` | **NO** | `-` | - | - |
| `Instrument` | `bit` | **NO** | `-` | - | - |
| `Sport` | `bit` | **NO** | `-` | - | - |
| `GLIDER` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_FlightInstructorCertificate`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_FlightInstructorCertificate`** (UNIQUE NONCLUSTERED)
  - Columns: `UserId`
