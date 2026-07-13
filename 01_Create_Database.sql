DROP DATABASE IF EXISTS ab_testing_platform;

CREATE DATABASE ab_testing_platform;

USE ab_testing_platform;

CREATE TABLE ab_test_data (

    UserID INT PRIMARY KEY,

    UserName VARCHAR(100),

    Age INT,

    Gender VARCHAR(20),

    Country VARCHAR(50),

    State VARCHAR(100),

    ExperimentGroup CHAR(1),

    Device VARCHAR(30),

    Browser VARCHAR(30),

    TrafficSource VARCHAR(50),

    SessionDuration DECIMAL(6,2),

    PagesViewed INT,

    ClickedCTA BOOLEAN,

    AddedToCart BOOLEAN,

    Purchased BOOLEAN,

    Revenue DECIMAL(10,2),

    Date DATE

);