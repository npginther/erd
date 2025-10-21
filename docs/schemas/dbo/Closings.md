# Closings

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (9)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `ClosingId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(50)` | **NO** | `-` | - | - |
| `Message` | `nvarchar(500)` | YES | `-` | - | - |
| `StartDate` | `datetime(3)` | **NO** | `-` | - | - |
| `EndDate` | `datetime(3)` | **NO** | `-` | - | - |
| `AllDay` | `bit` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_Closings`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
- **`UK_Closings`** (UNIQUE NONCLUSTERED)
  - Columns: `ClosingId`
