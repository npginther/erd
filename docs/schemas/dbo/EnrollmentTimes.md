# EnrollmentTimes

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `EnrollmentTimeId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | PK | - |
| `EnrollmentId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `TimeFieldId` | `nvarchar(50)` | **NO** | `-` | PK | - |
| `LoggedTime` | `decimal(9,2)` | YES | `-` | - | - |
| `PreviousCredit` | `decimal(9,2)` | YES | `-` | - | - |
| `TotalTime` | `decimal(10,2)` | YES | `-` | - | - |
| `CreatedAt` | `datetime(3)` | YES | `-` | - | - |
| `UpdatedAt` | `datetime(3)` | YES | `-` | - | - |

## Indexes

- **`PK_EnrollmentTimes`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `OperatorId, EnrollmentId, TimeFieldId`
