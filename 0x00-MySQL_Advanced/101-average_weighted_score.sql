-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  -- create varibale to store average
  DECLARE averageWeighted INT DEFAULT 0;
  DECLARE total_score INT DEFAULT 0;
  DECLARE total_weight INT DEFAULT 0;

  -- collecting scores and weight for student from corrections
  SELECT SUM(c.score * p.weight), SUM(p.weight) INTO total_score, total_weight
  FROM corrections c
  JOIN projects p ON c.project_id = p.id;
 
  -- calculate average score (if total_weight is not 0)
  IF  total_weight > 0 THEN
    -- SET averageWeighted = total_score / total_weight;
    -- update average weighted score for user_id specified
    UPDATE users SET average_score = total_score / total_weight;
  ELSE
    -- SET averageWeighted = 0;
    UPDATE users SET average_score = 0;
  END IF;

END //
DELIMITER ;
