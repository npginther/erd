# tblPropeller

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (16)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `PropellerId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `Description` | `varchar(250)` | **NO** | `-` | - | - |
| `SerialNumber` | `varchar(100)` | **NO** | `-` | - | - |
| `CurrentTime` | `decimal(9,2)` | **NO** | `-` | - | - |
| `LastMOHTime` | `decimal(9,2)` | YES | `-` | - | - |
| `LastMOHDate` | `datetime(3)` | YES | `-` | - | - |
| `TBOHours` | `decimal(9,2)` | YES | `-` | - | - |
| `TBOMonths` | `int(10,0)` | YES | `-` | - | - |
| `CurrentTimeAdjustment` | `decimal(9,2)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `CurrentTimeMeterType` | `int(10,0)` | YES | `-` | - | - |
| `CurrentTimeMeterIndex` | `int(10,0)` | YES | `-` | - | - |
| `TSOHAdjustment` | `decimal(9,2)` | YES | `-` | - | - |
| `TSOH` | `decimal(9,2)` | YES | `-` | - | - |

## Indexes

- **`PK_tblPropeller`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `PropellerId`
