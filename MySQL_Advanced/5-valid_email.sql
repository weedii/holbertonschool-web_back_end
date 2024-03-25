-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed

DELIMITER //

CREATE TRIGGER reset_valid_email
AFTER UPDATE ON users
FOR EACH ROW
-- test test test test
BEGIN
    IF NEW.email != OLD.email THEN
    SET NEW.valid_email = 0;
    END IF;
END; //

DELIMITER ;