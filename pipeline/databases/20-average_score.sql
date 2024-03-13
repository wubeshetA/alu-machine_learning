-- Procedure to add a bonus to a user for a project
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN p_user_id INT,
)

BEGIN
    DECLARE average_score FLOAT;

    -- Compute average score
    SELECT AVG(score) INTO average_score FROM corrections WHERE user_id = p_user_id;

    -- Update user
    UPDATE users SET average_score = average_score WHERE id = p_user_id;
END $$