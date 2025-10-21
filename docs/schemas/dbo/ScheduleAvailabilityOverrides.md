# ScheduleAvailabilityOverrides

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (6)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `OverrideId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `UserGuidId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `StartAtUtc` | `datetime2(7)` | **NO** | `-` | - | - |
| `EndAtUtc` | `datetime2(7)` | **NO** | `-` | - | - |
| `OverrideType` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_ScheduleStudentTimeOffOn`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `OverrideId`
