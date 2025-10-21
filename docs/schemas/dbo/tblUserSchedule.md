# tblUserSchedule

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (8)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Counter` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `UserGuidId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `DayOfWeek` | `int(10,0)` | **NO** | `-` | - | - |
| `ShiftStart` | `datetime(3)` | **NO** | `-` | - | - |
| `ShiftEnd` | `datetime(3)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IX_tblUserSchedule`** (UNIQUE NONCLUSTERED)
  - Columns: `UserGuidId, CompanyId, DayOfWeek, ShiftStart`
- **`PK_tblUserSchedule`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Counter`
