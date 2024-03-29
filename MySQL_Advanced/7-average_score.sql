-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student. Note: An average score can be a decimal

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)

BEGIN

    DECLARE average FLOAT;

    SELECT AVG(score) INTO average FROM corrections WHERE corrections.user_id = user_id;

    UPDATE users SET average_score = average WHERE id = user_id;

END //

DELIMITER ;