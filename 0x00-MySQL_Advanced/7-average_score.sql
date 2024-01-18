-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- NB: An average score can be a decimal

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
  -- create varibale to store average
  DECLARE average_score DECIMAL(10, 2);

  -- caculate or computes average  of a scores column for students.
  SELECT AVG(score)INTO average_score FROM corrections WHERE user_id = user_id;

  -- store the average score for a student
  UPDATE users SET average_score = average_score WHERE id = user_id;
END //
DELIMITER ;
