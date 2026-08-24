CREATE DATABASE IF NOT EXISTS `Customer_Support_Ticket_System` 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_0900_ai_ci;

USE `Customer_Support_Ticket_System`;

CREATE TABLE IF NOT EXISTS `Customers` (
  `customer_id` INT UNSIGNED AUTO_INCREMENT,
  `customer_name` VARCHAR(150) NOT NULL,
  `street` VARCHAR(255) DEFAULT NULL,
  `city` VARCHAR(100) DEFAULT NULL,
  `state` VARCHAR(100) DEFAULT NULL,
  `country` VARCHAR(100) DEFAULT NULL,
  `phone` VARCHAR(30) DEFAULT NULL,
  `email` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `idx_unique_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `Service_Representatives` (
  `service_rep_id` INT UNSIGNED AUTO_INCREMENT,
  `service_rep_name` VARCHAR(150) NOT NULL,
  `phone` VARCHAR(30) DEFAULT NULL,
  `email` VARCHAR(150) NOT NULL,
  `start_date` DATE DEFAULT NULL,
  `specialization` VARCHAR(100) DEFAULT NULL,
  PRIMARY KEY (`service_rep_id`),
  UNIQUE KEY `idx_unique_rep_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `Support_Tickets` (
  `ticket_id` INT UNSIGNED AUTO_INCREMENT,
  `model_name` VARCHAR(100) DEFAULT NULL,
  `model_number` VARCHAR(100) DEFAULT NULL,
  `scope_of_work` TEXT DEFAULT NULL,
  `ticket_creation_timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `customer_id` INT UNSIGNED NOT NULL,
  `service_rep_notes` TEXT DEFAULT NULL,
  `repair_completion` ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending',
  PRIMARY KEY (`ticket_id`),
  CONSTRAINT `fk_tickets_customer` 
    FOREIGN KEY (`customer_id`) 
    REFERENCES `Customers` (`customer_id`) 
    ON DELETE RESTRICT 
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `Historical_Ticket_Records` (
  `ticket_id` INT UNSIGNED NOT NULL,
  `service_rep_id` INT UNSIGNED NOT NULL,
  `ticket_assigned_timestamp` TIMESTAMP NULL DEFAULT NULL,
  `ticket_completion_timestamp` TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (`ticket_id`, `service_rep_id`),
  CONSTRAINT `fk_history_ticket` 
    FOREIGN KEY (`ticket_id`) 
    REFERENCES `Support_Tickets` (`ticket_id`) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE,
  CONSTRAINT `fk_history_rep` 
    FOREIGN KEY (`service_rep_id`) 
    REFERENCES `Service_Representatives` (`service_rep_id`) 
    ON DELETE RESTRICT 
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;