-- Create a new database if it doesn't exist (optional)
CREATE DATABASE IF NOT EXISTS blockchain_db;

-- Use the newly created database
USE blockchain_db;

-- Create a table to store Blockchain addresses and values
CREATE TABLE blockchain_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(255) NOT NULL,
    value DECIMAL(18, 8) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
