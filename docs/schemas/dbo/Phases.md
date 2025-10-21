# Phases

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `PhaseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `StageId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `CourseId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(100)` | **NO** | `-` | - | - |
| `Objectives` | `nvarchar(MAX)` | YES | `-` | - | - |
| `Order` | `int(10,0)` | **NO** | `-` | - | - |
| `Visible` | `bit` | **NO** | `-` | - | - |
| `IsLocked` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_Phases`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_Phases_PhaseId`** (UNIQUE NONCLUSTERED)
  - Columns: `PhaseId`
- **`nci_wi_Phases_63B661663F46C4D0137F4C76C60099B6`** (NONCLUSTERED)
  - Columns: `CourseId, OperatorId, StageId INCLUDE (Name, Objectives, Order, PhaseId)`
