# tblAircraftImages

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (10)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `Id` | `int(10,0)` | **NO** | `-` | - | - |
| `AircraftId` | `uniqueidentifier` | **NO** | `-` | PK | - |
| `ContentType` | `varchar(50)` | **NO** | `-` | - | - |
| `FullImageSize` | `decimal(14,2)` | **NO** | `-` | - | - |
| `FullImageData` | `image(2147483647)` | **NO** | `-` | - | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `CroppedImageData` | `image(2147483647)` | **NO** | `-` | - | - |
| `CroppedImageSize` | `decimal(18,0)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblAircraftImages`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `AircraftId`
