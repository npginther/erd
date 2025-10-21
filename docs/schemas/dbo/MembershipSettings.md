# MembershipSettings

**Schema:** `dbo`  
**Type:** BASE TABLE  
**Database:** fsp-165587 (Operator Replica)

## Description

*No description available*

## Columns (11)

| Column | Type | Nullable | Default | Keys | Description |
|--------|------|----------|---------|------|-------------|
| `_RowNumber` | `bigint(19,0)` | **NO** | `-` | PK | - |
| `OperatorId` | `int(10,0)` | **NO** | `-` | - | - |
| `InactivateUserOnPastDue` | `bit` | YES | `-` | - | - |
| `AssignToRoleOnPastDue` | `int(10,0)` | YES | `-` | - | - |
| `SendNotificationOnPastDue` | `bit` | YES | `-` | - | - |
| `InactivateUserOnCancelled` | `bit` | YES | `-` | - | - |
| `AssignToRoleOnCancelled` | `int(10,0)` | YES | `-` | - | - |
| `SendNotificationOnCancelled` | `bit` | YES | `-` | - | - |
| `RequireTOSAcceptance` | `bit` | YES | `-` | - | - |
| `TOSUrl` | `nvarchar(500)` | YES | `-` | - | - |
| `LastModifiedTime` | `datetime(3)` | **NO** | `-` | - | - |

## Indexes

- **`PK_MembershipSettings`** (PRIMARY KEY UNIQUE CLUSTERED)
  - Columns: `_RowNumber`
