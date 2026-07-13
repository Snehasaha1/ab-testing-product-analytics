
USE ab_testing_platform;

-- =====================================================
-- USER DIMENSION
-- =====================================================

CREATE TABLE dim_user (

    UserID INT PRIMARY KEY,

    UserName VARCHAR(100),

    Age INT,

    Gender VARCHAR(20),

    Country VARCHAR(100),

    State VARCHAR(100)

);

-- =====================================================
-- DEVICE DIMENSION
-- =====================================================

CREATE TABLE dim_device (

    DeviceID INT PRIMARY KEY,

    DeviceName VARCHAR(50)

);

-- =====================================================
-- BROWSER DIMENSION
-- =====================================================

CREATE TABLE dim_browser (

    BrowserID INT PRIMARY KEY,

    BrowserName VARCHAR(50)

);

-- =====================================================
-- TRAFFIC SOURCE DIMENSION
-- =====================================================

CREATE TABLE dim_traffic_source (

    TrafficSourceID INT PRIMARY KEY,

    TrafficSourceName VARCHAR(100)

);

-- =====================================================
-- DATE DIMENSION
-- =====================================================

CREATE TABLE dim_date (

    DateID INT PRIMARY KEY,

    Date DATE,

    Day INT,

    Month INT,

    MonthName VARCHAR(20),

    Quarter VARCHAR(5),

    Year INT,

    Week INT,

    DayOfWeek INT,

    DayName VARCHAR(20),

    IsWeekend VARCHAR(10)

);

-- =====================================================
-- EXPERIMENT DIMENSION
-- =====================================================

CREATE TABLE dim_experiment (

    ExperimentID INT PRIMARY KEY,

    ExperimentGroup VARCHAR(10),

    ExperimentName VARCHAR(100),

    Description VARCHAR(200)

);

-- =====================================================
-- FACT TABLE
-- =====================================================

CREATE TABLE fact_experiment (

    FactID INT PRIMARY KEY,

    UserID INT,

    DeviceID INT,

    BrowserID INT,

    TrafficSourceID INT,

    DateID INT,

    ExperimentID INT,

    SessionDuration DECIMAL(10,2),

    PagesViewed INT,

    ClickedCTA TINYINT,

    AddedToCart TINYINT,

    Purchased TINYINT,

    Revenue DECIMAL(10,2),

    FOREIGN KEY (UserID)
        REFERENCES dim_user(UserID),

    FOREIGN KEY (DeviceID)
        REFERENCES dim_device(DeviceID),

    FOREIGN KEY (BrowserID)
        REFERENCES dim_browser(BrowserID),

    FOREIGN KEY (TrafficSourceID)
        REFERENCES dim_traffic_source(TrafficSourceID),

    FOREIGN KEY (DateID)
        REFERENCES dim_date(DateID),

    FOREIGN KEY (ExperimentID)
        REFERENCES dim_experiment(ExperimentID)

);