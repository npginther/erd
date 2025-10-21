# tblFlightInstructorScheduleAdjustments

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `AdjustmentId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `InstructorId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `RecurringId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TimeOff` | `bit` | **NO** | `-` | - | - |
| `Starting` | `datetime(3)` | **NO** | `-` | - | - |
| `Ending` | `datetime(3)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblFlightInstructorScheduleAdjustments`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AdjustmentId`
