# Certifications

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (5)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowId` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `CertificationId` | `uniqueidentifier` | **NO** | `-` | - | - |
| `RegulationId` | `int(10,0)` | **NO** | `-` | - | - |
| `Name` | `nvarchar(250)` | **NO** | `-` | - | - |
| `IsActive` | `bit` | **NO** | `-` | - | - |

## Indexes

- **`PK_Certifications`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowId`
- **`UK_Certifications_CertificationId`** (UNIQUE NONCLUSTERED)
  - Columns: `CertificationId`
