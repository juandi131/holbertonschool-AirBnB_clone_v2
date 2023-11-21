-- Create database.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a user and define a password.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Define privileges.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Define privilege SELECT in the database performance_schema.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Actualizate privileges
FLUSH PRIVILEGES;
