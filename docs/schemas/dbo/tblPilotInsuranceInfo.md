# tblPilotInsuranceInfo

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (22)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PilotId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `InsuranceProvider` | `nvarchar(100)` | **NO** | `-` | - | - |
| `InsuranceAgent` | `nvarchar(100)` | **NO** | `-` | - | - |
| `InsuranceAgentPhone` | `nvarchar(35)` | **NO** | `-` | - | - |
| `InsuranceRenewalDate` | `varchar(20)` | **NO** | `-` | - | - |
| `NonOwnerInsurance` | `bit` | **NO** | `-` | - | - |
| `OwnerInsurance` | `bit` | **NO** | `-` | - | - |
| `FlightInstructorInsurance` | `bit` | **NO** | `-` | - | - |
| `InsurancePolicyNumber` | `nvarchar(50)` | YES | `-` | - | - |
| `InsuranceExpirationDate` | `datetime(3)` | YES | `-` | - | - |
| `OwnerProvider` | `nvarchar(100)` | YES | `-` | - | - |
| `OwnerPolicyNumber` | `nvarchar(50)` | YES | `-` | - | - |
| `OwnerAgentName` | `nvarchar(100)` | YES | `-` | - | - |
| `OwnerAgentPhone` | `nvarchar(50)` | YES | `-` | - | - |
| `OwnerExpirationDate` | `datetime(3)` | YES | `-` | - | - |
| `FlightInstructorProvider` | `nvarchar(100)` | YES | `-` | - | - |
| `FlightInstructorPolicyNumber` | `nvarchar(50)` | YES | `-` | - | - |
| `FlightInstructorAgentName` | `nvarchar(100)` | YES | `-` | - | - |
| `FlightInstructorAgentPhone` | `nvarchar(50)` | YES | `-` | - | - |
| `FlightInstructorExpirationDate` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_tblPilotInsuranceInfo`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PilotId`
