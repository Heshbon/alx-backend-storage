-- Drop the trigger if it already exists to avoid conflicts
DROP TRIGGER IF EXISTS reset_valid_email;
DELIMITER $$

-- SQL script that creates a trigger that resets the attribute valid_email.
-- only when the email has been changed.
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$
DELIMITER ;
