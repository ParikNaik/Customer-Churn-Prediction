CREATE TABLE `customerdata` (
  `customerID` varchar(20) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `SeniorCitizen` tinyint DEFAULT NULL,
  `Partner` varchar(3) DEFAULT NULL,
  `Dependents` varchar(3) DEFAULT NULL,
  `tenure` int DEFAULT NULL,
  `PhoneService` varchar(20) DEFAULT NULL,
  `MultipleLines` varchar(20) DEFAULT NULL,
  `InternetService` varchar(20) DEFAULT NULL,
  `OnlineSecurity` varchar(20) DEFAULT NULL,
  `OnlineBackup` varchar(20) DEFAULT NULL,
  `DeviceProtection` varchar(20) DEFAULT NULL,
  `TechSupport` varchar(20) DEFAULT NULL,
  `StreamingTV` varchar(20) DEFAULT NULL,
  `StreamingMovies` varchar(20) DEFAULT NULL,
  `Contract` varchar(20) DEFAULT NULL,
  `PaperlessBilling` varchar(3) DEFAULT NULL,
  `PaymentMethod` varchar(50) DEFAULT NULL,
  `MonthlyCharges` decimal(10,2) DEFAULT NULL,
  `TotalCharges` decimal(10,2) DEFAULT NULL,
  `Churn` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

