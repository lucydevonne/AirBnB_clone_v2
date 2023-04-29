# Creates the database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

# Creates the user hbnb_test and sets the password to hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

# Grants all privileges to hbnb_test on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

# Grants SELECT privilege to hbnb_test on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

# Flushes the privileges to ensure that the changes take effect
FLUSH PRIVILEGES;

