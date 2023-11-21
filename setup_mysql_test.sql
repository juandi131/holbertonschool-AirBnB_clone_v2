-- Create database.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a user and define a password.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Define privileges.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Define privilege SELECT in the database performance_schema.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Update privileges.
FLUSH PRIVILEGES;
