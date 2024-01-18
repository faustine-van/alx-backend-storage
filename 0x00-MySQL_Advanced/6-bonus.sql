-- SQL script that creates a stored procedure AddBonus
-- that adds a new correction for a student.
DELIMITER //
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
  DECLARE project_id INT;
  -- Get the project_id for the given project_name
  SELECT id INTO project_id FROM projects WHERE name = project_name;
  -- check if project exists
  IF project_id IS NULL THEN
    -- Project does not exist, insert a new project
    INSERT INTO projects (name) VALUES (project_name);
    -- Get the newly inserted project_id
    SELECT LAST_INSERT_ID() INTO project_id;
  END IF;
  -- insert new correction
  INSERT INTO corrections (user_id, project_id, score) VALUES
  (user_id, project_id, score);
END //
DELIMITER ;
