-- ================================================================
-- SQL Queries to Export Database Schema Information
-- For building a comprehensive data dictionary
-- ================================================================

-- Run each query and export results to CSV with the specified filename

-- ================================================================
-- 1. COLUMNS.csv - Complete column information
-- ================================================================
-- This is the CORE of your data dictionary
-- Contains: column names, data types, lengths, nullability, defaults
SELECT 
    TABLE_CATALOG,
    TABLE_SCHEMA,
    TABLE_NAME,
    COLUMN_NAME,
    ORDINAL_POSITION,
    COLUMN_DEFAULT,
    IS_NULLABLE,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH,
    CHARACTER_OCTET_LENGTH,
    NUMERIC_PRECISION,
    NUMERIC_PRECISION_RADIX,
    NUMERIC_SCALE,
    DATETIME_PRECISION,
    CHARACTER_SET_NAME,
    COLLATION_NAME
FROM INFORMATION_SCHEMA.COLUMNS
ORDER BY TABLE_SCHEMA, TABLE_NAME, ORDINAL_POSITION;


-- ================================================================
-- 2. TABLES.csv - Table metadata
-- ================================================================
-- Distinguishes between tables, views, and table types
SELECT 
    TABLE_CATALOG,
    TABLE_SCHEMA,
    TABLE_NAME,
    TABLE_TYPE
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
ORDER BY TABLE_SCHEMA, TABLE_NAME;


-- ================================================================
-- 3. KEY_COLUMN_USAGE.csv - Key column details
-- ================================================================
-- Shows which columns are part of PRIMARY KEY, FOREIGN KEY, UNIQUE constraints
SELECT 
    CONSTRAINT_CATALOG,
    CONSTRAINT_SCHEMA,
    CONSTRAINT_NAME,
    TABLE_CATALOG,
    TABLE_SCHEMA,
    TABLE_NAME,
    COLUMN_NAME,
    ORDINAL_POSITION
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
ORDER BY TABLE_SCHEMA, TABLE_NAME, ORDINAL_POSITION;


-- ================================================================
-- 4. CHECK_CONSTRAINTS.csv - Check constraint definitions
-- ================================================================
-- Shows business rules enforced at database level
SELECT 
    CONSTRAINT_CATALOG,
    CONSTRAINT_SCHEMA,
    CONSTRAINT_NAME,
    CHECK_CLAUSE
FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS
ORDER BY CONSTRAINT_SCHEMA, CONSTRAINT_NAME;


-- ================================================================
-- 5. VIEWS.csv - View definitions
-- ================================================================
-- Contains the SQL that defines each view
SELECT 
    TABLE_CATALOG,
    TABLE_SCHEMA,
    TABLE_NAME,
    VIEW_DEFINITION,
    CHECK_OPTION,
    IS_UPDATABLE
FROM INFORMATION_SCHEMA.VIEWS
ORDER BY TABLE_SCHEMA, TABLE_NAME;


-- ================================================================
-- 6. ROUTINES.csv - Stored procedures and functions
-- ================================================================
-- Documents all stored procedures and functions
SELECT 
    ROUTINE_CATALOG,
    ROUTINE_SCHEMA,
    ROUTINE_NAME,
    ROUTINE_TYPE,
    DATA_TYPE,
    ROUTINE_DEFINITION,
    CREATED,
    LAST_ALTERED
FROM INFORMATION_SCHEMA.ROUTINES
ORDER BY ROUTINE_SCHEMA, ROUTINE_NAME;


-- ================================================================
-- 7. PARAMETERS.csv - Stored procedure/function parameters
-- ================================================================
-- Shows parameters for stored procedures and functions
SELECT 
    SPECIFIC_CATALOG,
    SPECIFIC_SCHEMA,
    SPECIFIC_NAME,
    ORDINAL_POSITION,
    PARAMETER_MODE,
    PARAMETER_NAME,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH,
    NUMERIC_PRECISION,
    NUMERIC_SCALE
FROM INFORMATION_SCHEMA.PARAMETERS
ORDER BY SPECIFIC_SCHEMA, SPECIFIC_NAME, ORDINAL_POSITION;


-- ================================================================
-- 8. INDEXES (SQL Server specific - not in INFORMATION_SCHEMA)
-- ================================================================
-- Shows all indexes for performance analysis
SELECT 
    DB_NAME() AS DatabaseName,
    s.name AS SchemaName,
    t.name AS TableName,
    i.name AS IndexName,
    i.type_desc AS IndexType,
    i.is_unique AS IsUnique,
    i.is_primary_key AS IsPrimaryKey,
    i.is_unique_constraint AS IsUniqueConstraint,
    COL_NAME(ic.object_id, ic.column_id) AS ColumnName,
    ic.key_ordinal AS KeyOrdinal,
    ic.is_included_column AS IsIncludedColumn
FROM sys.indexes i
INNER JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
INNER JOIN sys.tables t ON i.object_id = t.object_id
INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
WHERE i.name IS NOT NULL
ORDER BY s.name, t.name, i.name, ic.key_ordinal;


-- ================================================================
-- 9. TABLE_SIZES.csv (SQL Server specific)
-- ================================================================
-- Shows row counts and storage space used
SELECT 
    s.name AS SchemaName,
    t.name AS TableName,
    p.rows AS RowCount,
    SUM(a.total_pages) * 8 AS TotalSpaceKB,
    SUM(a.used_pages) * 8 AS UsedSpaceKB,
    (SUM(a.total_pages) - SUM(a.used_pages)) * 8 AS UnusedSpaceKB
FROM sys.tables t
INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
INNER JOIN sys.indexes i ON t.object_id = i.object_id
INNER JOIN sys.partitions p ON i.object_id = p.object_id AND i.index_id = p.index_id
INNER JOIN sys.allocation_units a ON p.partition_id = a.container_id
WHERE t.is_ms_shipped = 0
    AND i.object_id > 255
GROUP BY s.name, t.name, p.rows
ORDER BY s.name, t.name;


-- ================================================================
-- 10. EXTENDED_PROPERTIES.csv (SQL Server specific)
-- ================================================================
-- Captures MS_Description and other custom documentation
SELECT 
    s.name AS SchemaName,
    o.name AS ObjectName,
    o.type_desc AS ObjectType,
    c.name AS ColumnName,
    ep.name AS PropertyName,
    CAST(ep.value AS NVARCHAR(MAX)) AS PropertyValue
FROM sys.extended_properties ep
LEFT JOIN sys.objects o ON ep.major_id = o.object_id
LEFT JOIN sys.schemas s ON o.schema_id = s.schema_id
LEFT JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id
WHERE ep.class_desc IN ('OBJECT_OR_COLUMN')
ORDER BY s.name, o.name, c.name, ep.name;


-- ================================================================
-- BONUS: Column Statistics (SQL Server specific)
-- ================================================================
-- Useful for understanding data distribution
SELECT 
    s.name AS SchemaName,
    t.name AS TableName,
    c.name AS ColumnName,
    st.name AS StatisticName,
    st.auto_created AS IsAutoCreated,
    st.user_created AS IsUserCreated,
    STATS_DATE(st.object_id, st.stats_id) AS LastUpdated
FROM sys.stats st
INNER JOIN sys.stats_columns sc ON st.object_id = sc.object_id AND st.stats_id = sc.stats_id
INNER JOIN sys.columns c ON sc.object_id = c.object_id AND sc.column_id = c.column_id
INNER JOIN sys.tables t ON st.object_id = t.object_id
INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
WHERE t.is_ms_shipped = 0
ORDER BY s.name, t.name, c.name;

