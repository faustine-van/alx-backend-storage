-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- NB: An average score can be a decimal
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
  -- create varibale to store average
  DECLARE totalOfScore DECIMAL(10, 2);
  DECLARE numberOfScores INT;

  -- caculate or computes average  of a scores column for students.
  SELECT SUM(score), COUNT(*) INTO totalOfScore, numberOfScores
   FROM corrections WHERE user_id = user_id;

  IF numberOfScores > 0 THEN
    -- store the average score for a student
    UPDATE users SET average_score = totalOfScore / numberOfScores WHERE id = user_id;
  END IF;
END //

DELIMITER ;
