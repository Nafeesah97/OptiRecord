-- Prepare my server for the project

CREATE DATABASE IF NOT EXISTS  optirecord_db;
CREATE USER IF NOT EXISTS 'optirecord'@'localhost' IDENTIFIED BY 'psword';
GRANT ALL PRIVILEGES ON `optirecord_db`.* TO 'optirecord'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'optirecord'@'localhost';
FLUSH PRIVILEGES;