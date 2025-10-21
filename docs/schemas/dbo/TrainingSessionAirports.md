# TrainingSessionAirports

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `LessonId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StudentId` | `uniqueidentifier` | YES | `-` | - | - |
| `EnrollmentId` | `uniqueidentifier` | YES | `-` | - | - |
| `TrainingSessionId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `AirportId` | `nvarchar(10)` | **NO** | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_TrainingSessionAirports`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_TrainingSessionAirports_TrainingSessionIdAirportIdOrder`** (UNIQUE NONCLUSTERED)
  - Columns: `TrainingSessionId, AirportId, Order`
