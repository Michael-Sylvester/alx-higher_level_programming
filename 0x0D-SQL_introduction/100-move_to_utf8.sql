-- convert to utf-8
-- Convert the database to utf8mb4
ALTER DATABASE hbtn_0c_0 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Convert the table to utf8mb4
ALTER TABLE first_table 
CONVERT TO CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Convert the field `name` to utf8mb4
ALTER TABLE first_table 
MODIFY COLUMN name VARCHAR(255) 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
