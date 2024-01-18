-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- NB: An average score can be a decimal
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(input_id INT)
BEGIN
  -- create varibale to store average
  DECLARE average DECIMAL(10, 2);
  
  -- caculate or computes average  of a scores column for students.
  SELECT SUM(score) / COUNT(score) INTO average FROM corrections WHERE user_id = input_id;
  -- store the average score for a student
  UPDATE users SET average_score = average  WHERE id = input_id;
END //

DELIMITER ;
