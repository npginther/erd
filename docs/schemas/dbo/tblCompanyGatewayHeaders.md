# tblCompanyGatewayHeaders

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (7)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `id` | `int(10,0)` | **NO** | `-` | PK | - |
| `CompanyId` | `int(10,0)` | **NO** | `-` | - | - |
| `ContentType` | `varchar(50)` | **NO** | `-` | - | - |
| `ImageSize` | `decimal(14,2)` | **NO** | `-` | - | - |
| `Data` | `image(2147483647)` | **NO** | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |

## Indexes

- **`PK_tblCompanyGatewayHeaders`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `id`
