-- SQL script that creates the first letter of name
ALTER TABLE names ADD INDEX idx_name_first (name(1));
