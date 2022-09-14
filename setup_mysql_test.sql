-- Script that prepares a MySQL server for the project.
-- A database hbnb_dev_db
-- A new use hbnb_dev in localhost.
-- The password hbnb_dev_pwd.
-- The database hbnb_dev_db

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS `hbnb_test`@`localhost`
    IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
   ON `hbnb_test_db`.*
   TO `hbnb_test`@`localhost`;
GRANT SELECT
   ON `performance_schema`.*
   TO `hbnb_test`@`localhost`;
FLUSH PRIVILEGES;
