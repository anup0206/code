CREATE DATABASE feedback_db;

USE feedback_db;

CREATE TABLE submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    feedback_type ENUM('suggestion', 'complaint', 'praise') NOT NULL,
    satisfaction ENUM('very-satisfied', 'satisfied', 'neutral', 'dissatisfied') NOT NULL,
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);