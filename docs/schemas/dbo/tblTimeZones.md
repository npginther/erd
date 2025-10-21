# tblTimeZones

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `int(10,0)` | **NO** | `-` | PK | - |
| `Offset` | `decimal(4,2)` | **NO** | `-` | - | - |
| `FriendlyName` | `nvarchar(75)` | **NO** | `-` | - | - |
| `DaylightSavingTimeOffsetValue` | `decimal(4,2)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblTimeZones`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `Id`
