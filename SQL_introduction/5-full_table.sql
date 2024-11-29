-- 5-full_table.sql
SELECT 
    table_name AS 'Table', 
    CONCAT(
        'CREATE TABLE `', table_name, '` (',
        GROUP_CONCAT(
            CONCAT(
                '`', column_name, '` ', column_type, 
                IF(is_nullable = 'NO', ' NOT NULL', ''),
                IF(column_default IS NOT NULL, CONCAT(' DEFAULT ', column_default), ''),
                IF(extra = 'auto_increment', ' AUTO_INCREMENT', '')
            ) SEPARATOR ', '
        ),
        ') ENGINE=', engine, 
        ' DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
    ) AS 'Create Table'
FROM 
    information_schema.tables 
JOIN 
    information_schema.columns 
ON 
    tables.table_name = columns.table_name
WHERE 
    tables.table_schema = DATABASE() 
    AND tables.table_name = 'first_table'
GROUP BY 
    tables.table_name;
