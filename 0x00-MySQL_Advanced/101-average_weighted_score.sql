-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
 BEGIN 
  DECLARE user_id_param INT;
  -- Declare variables to store scores and weights for each user
  DECLARE total_score INT;
  DECLARE total_weight INT;
  DECLARE done BOOLEAN;

  -- Declare a cursor to loop through user IDs
  DECLARE user_cursor CURSOR FOR SELECT id FROM users;
  -- control what happens when a cursor reaches the end or
  -- If no more rows are available
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;


  -- open cursor
  OPEN user_cursor;

    -- Start looping through users
    use_loop: LOOP
  
      -- fetching next user_id from cursor
      FETCH user_cursor INTO user_id_param;
      -- check if no more users
      -- IF user_id_param IS NULL THEN
      IF done THEN
        LEAVE use_loop;
      END IF;

      SET total_score = 0;
      SET total_weight = 0;

      -- collecting scores and weight for student from corrections
      SELECT IFNULL(SUM(c.score * p.weight), 0), IFNULL(SUM(p.weight), 0)
      INTO total_score, total_weight
      FROM corrections c
      JOIN projects p ON c.project_id = p.id
      WHERE c.user_id = user_id_param;
  
      -- calculate average score (if total_weight is not 0)
      IF  total_weight > 0 THEN
         -- update average weighted score for user_id specified
         UPDATE users SET average_score = total_score / total_weight
         WHERE id = user_id_param;
      ELSE
         UPDATE users SET average_score = 0
         WHERE id = user_id_param;
      END IF;
    END LOOP;
  -- Close the cursor
  CLOSE user_cursor;

 END //
DELIMITER //
