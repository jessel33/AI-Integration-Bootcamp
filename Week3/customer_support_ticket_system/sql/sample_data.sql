USE `Customer_Support_Ticket_System`;

SET FOREIGN_KEY_CHECKS = 0;
DELETE FROM `Historical_Ticket_Records`;
DELETE FROM `Support_Tickets`;
DELETE FROM `Service_Representatives`;
DELETE FROM `Customers`;
SET FOREIGN_KEY_CHECKS = 1;

ALTER TABLE `Customers` AUTO_INCREMENT = 1;
ALTER TABLE `Service_Representatives` AUTO_INCREMENT = 1;
ALTER TABLE `Support_Tickets` AUTO_INCREMENT = 1;

INSERT INTO `Customers` (`customer_id`, `customer_name`, `street`, `city`, `state`, `country`, `phone`, `email`) VALUES
(1, 'Alice Smith', '123 Maple St', 'Los Angeles', 'California', 'USA', '555-0192', 'alice.smith@example.com'),
(2, 'Bob Jones', '456 Oak Ave', 'New York', 'New York', 'USA', '555-0143', 'bob.jones@example.com'),
(3, 'Charlie Brown', '789 Pine Rd', 'Toronto', 'Ontario', 'Canada', '555-0177', 'charlie.b@example.com'),
(4, 'Diana Prince', '101 Gateway Blvd', 'London', 'England', 'UK', '555-0188', 'diana.p@example.com');

INSERT INTO `Service_Representatives` (`service_rep_id`, `service_rep_name`, `phone`, `email`, `start_date`, `specialization`) VALUES
(1, 'John Doe', '555-9001', 'john.doe@support.com', '2024-01-15', 'Hardware Diagnostics'),
(2, 'Jane Doe', '555-9002', 'jane.doe@support.com', '2024-06-01', 'Software Configuration'),
(3, 'Alex Wong', '555-9003', 'alex.wong@support.com', '2025-03-10', 'Network Connectivity');

INSERT INTO `Support_Tickets` (`ticket_id`, `model_name`, `model_number`, `scope_of_work`, `ticket_creation_timestamp`, `customer_id`, `service_rep_notes`, `repair_completion`) VALUES
(1, 'QuantumBook Pro', 'QB-2026X', 'Screen flickering and intermittent power failure.', '2026-08-20 09:15:00', 1, 'Replaced the display cable. Power issue resolved after firmware flash.', 'Completed'),
(2, 'SpeedRoute 5G', 'SR-500', 'Router drops Wi-Fi signals every 20 minutes.', '2026-08-21 14:30:00', 2, 'Monitoring signal strength. Suspicion of overheating hardware.', 'In Progress'),
(3, 'EcoWash 9000', 'EW-9K-A', 'Leaking water from the front door during rinse cycle.', '2026-08-22 11:00:00', 3, NULL, 'Pending'),
(4, 'QuantumBook Pro', 'QB-2026X', 'Keyboard keys R and T are unresponsive.', '2026-08-23 08:00:00', 1, 'Ordered replacement keyboard membrane.', 'In Progress');

INSERT INTO `Historical_Ticket_Records` (`ticket_id`, `service_rep_id`, `ticket_assigned_timestamp`, `ticket_completion_timestamp`) VALUES
(1, 1, '2026-08-20 10:00:00', '2026-08-21 16:45:00'),
(2, 3, '2026-08-21 15:00:00', NULL),
(4, 2, '2026-08-23 08:30:00', NULL);