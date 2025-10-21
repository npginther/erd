# tblUserScheduleAdjustments

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Counter` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `AdjustmentId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `UserGuidId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `RecurringId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `TimeOff` | `bit` | **NO** | `-` | - | - |
| `Starting` | `datetime(3)` | **NO** | `-` | - | - |
| `Ending` | `datetime(3)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`IDX_tblUserScheduleAdjustments_UserGuidIdCompanyId_AdjustmentIdRecurringIdTimeOffStartingEnding`** (NONCLUSTERED)
  - Columns: `UserGuidId, CompanyId INCLUDE (AdjustmentId, Ending, RecurringId, Starting, TimeOff)`
- **`PK_tblUserScheduleAdjustments`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Counter`
- **`ix_tblUserScheduleAdjustments_AdjustmentId`** (NONCLUSTERED)
  - Columns: `AdjustmentId`
