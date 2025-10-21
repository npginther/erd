# tblPilotTSAVerification

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PilotId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `DocumentId` | `int(10,0)` | **NO** | `-` | - | - |
| `VerifiedInstructorStudentLogbook` | `bit` | **NO** | `-` | - | - |
| `VerifingUser` | `varchar(70)` | **NO** | `-` | - | - |
| `VerifingPhone` | `varchar(20)` | **NO** | `-` | - | - |
| `VerifiedDate` | `datetime(3)` | **NO** | `-` | - | - |
| `ExpirationDate` | `datetime(3)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | YES | `-` | - | - |

## Indexes

- **`PK_tblPilotTSAVerification`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PilotId`
