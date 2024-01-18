-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student
DELIMITER //
CREATE PROCEDURE  ComputeAverageWeightedScoreForUser(input_id INT)
BEGIN
  -- create varibale to store average
  DECLARE averageWeighted DECIMAL(10, 2);
  DECLARE total_score INT;
  DECLARE total_weight INT;

  -- collecting scores and weight for student from corrections
  SELECT SUM(c.score * p.weight), SUM(p.weight) INTO total_score, total_weight
  FROM corrections c
  JOIN projects p ON c.user_id = p.id
  WHERE c.user_id = input_id;
 
  -- calculate average score (if total_weight is not 0)
  IF  total_weight > 0 THEN
    SET averageWeighted = total_score / total_weight;
  ELSE
    SET averageWeighted = 0;
  END IF;
  -- update average weighted score for user_id specified
  UPDATE users SET average_score = averageWeighted WHERE id = input_id;

END //
DELIMITER ;