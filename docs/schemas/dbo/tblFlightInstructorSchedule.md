# tblFlightInstructorSchedule

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `InstructorId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | PK | - |
| `DayOfWeek` | `int(10,0)` | **NO** | `-` | PK | - |
| `ShiftStart` | `datetime(3)` | **NO** | `-` | PK | - |
| `ShiftEnd` | `datetime(3)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblFlightInstructorSchedule`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `InstructorId, CompanyId, DayOfWeek, ShiftStart`
