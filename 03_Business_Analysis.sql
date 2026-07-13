USE ab_testing_platform;

SELECT
    e.ExperimentGroup,
    COUNT(*) AS TotalUsers,
    SUM(f.ClickedCTA) AS Clicks,
    SUM(f.AddedToCart) AS AddedToCart,
    SUM(f.Purchased) AS Purchases,
    ROUND(AVG(f.SessionDuration),2) AS AvgSessionDuration,
    ROUND(AVG(f.PagesViewed),2) AS AvgPagesViewed,
    ROUND(AVG(f.Revenue),2) AS AvgRevenue,
    ROUND(100 * AVG(f.ClickedCTA),2) AS CTR_Percent,
    ROUND(100 * AVG(f.AddedToCart),2) AS AddToCartRate,
    ROUND(100 * AVG(f.Purchased),2) AS PurchaseRate
FROM fact_experiment f
JOIN dim_experiment e
    ON f.ExperimentID = e.ExperimentID
GROUP BY e.ExperimentGroup;

-- 2. Device Performance

SELECT
    d.DeviceName,
    COUNT(*) AS TotalUsers,
    ROUND(AVG(f.Revenue),2) AS AvgRevenue,
    ROUND(100 * AVG(f.Purchased),2) AS PurchaseRate
FROM fact_experiment f
JOIN dim_device d
    ON f.DeviceID = d.DeviceID
GROUP BY d.DeviceName
ORDER BY PurchaseRate DESC;

-- 3. Browser Performance

SELECT
    b.BrowserName,
    COUNT(*) AS TotalUsers,
    ROUND(AVG(f.Revenue),2) AS AvgRevenue,
    ROUND(100 * AVG(f.Purchased),2) AS PurchaseRate
FROM fact_experiment f
JOIN dim_browser b
    ON f.BrowserID = b.BrowserID
GROUP BY b.BrowserName
ORDER BY PurchaseRate DESC;

-- 4. Traffic Source Performance

SELECT
    t.TrafficSourceName,
    COUNT(*) AS TotalUsers,
    ROUND(AVG(f.Revenue),2) AS AvgRevenue,
    ROUND(100 * AVG(f.Purchased),2) AS PurchaseRate
FROM fact_experiment f
JOIN dim_traffic_source t
    ON f.TrafficSourceID = t.TrafficSourceID
GROUP BY t.TrafficSourceName
ORDER BY PurchaseRate DESC;

-- 5. Monthly Revenue Trend

SELECT
    d.Year,
    d.Month,
    d.MonthName,
    ROUND(SUM(f.Revenue), 2) AS TotalRevenue,
    ROUND(100 * AVG(f.Purchased), 2) AS PurchaseRate
FROM fact_experiment f
JOIN dim_date d
    ON f.DateID = d.DateID
GROUP BY
    d.Year,
    d.Month,
    d.MonthName
ORDER BY
    d.Year,
    d.Month;
    
    -- 6. Funnel Analysis

SELECT
    COUNT(*) AS TotalVisitors,
    SUM(ClickedCTA) AS ClickedCTA,
    SUM(AddedToCart) AS AddedToCart,
    SUM(Purchased) AS Purchased,
    ROUND(100 * SUM(ClickedCTA) / COUNT(*), 2) AS CTR_Percent,
    ROUND(100 * SUM(AddedToCart) / COUNT(*), 2) AS CartRate_Percent,
    ROUND(100 * SUM(Purchased) / COUNT(*), 2) AS PurchaseRate_Percent
FROM fact_experiment;

-- 7. Funnel Analysis by Experiment Group

SELECT
    e.ExperimentGroup,
    COUNT(*) AS TotalVisitors,
    SUM(f.ClickedCTA) AS ClickedCTA,
    SUM(f.AddedToCart) AS AddedToCart,
    SUM(f.Purchased) AS Purchased,
    ROUND(100 * AVG(f.ClickedCTA), 2) AS CTR_Percent,
    ROUND(100 * AVG(f.AddedToCart), 2) AS CartRate_Percent,
    ROUND(100 * AVG(f.Purchased), 2) AS PurchaseRate_Percent
FROM fact_experiment f
JOIN dim_experiment e
    ON f.ExperimentID = e.ExperimentID
GROUP BY e.ExperimentGroup;

SELECT

u.Country,

COUNT(*) AS Users,

ROUND(SUM(f.Revenue),2) AS TotalRevenue,

ROUND(AVG(f.Revenue),2) AS AvgRevenue,

ROUND(100*AVG(f.Purchased),2) AS PurchaseRate

FROM fact_experiment f

JOIN dim_user u
ON f.UserID=u.UserID

GROUP BY u.Country

ORDER BY TotalRevenue DESC;

SELECT

u.Country,
u.State,

COUNT(*) AS Users,

ROUND(SUM(f.Revenue),2) AS TotalRevenue,

ROUND(AVG(f.Revenue),2) AS AvgRevenue,

ROUND(100*AVG(f.Purchased),2) AS PurchaseRate

FROM fact_experiment f

JOIN dim_user u
ON f.UserID=u.UserID

GROUP BY
u.Country,
u.State

ORDER BY TotalRevenue DESC;

SELECT

d.DeviceName,
b.BrowserName,

COUNT(*) AS Users,

ROUND(AVG(f.Revenue),2) AS AvgRevenue,

ROUND(100*AVG(f.Purchased),2) AS PurchaseRate

FROM fact_experiment f

JOIN dim_device d
ON f.DeviceID=d.DeviceID

JOIN dim_browser b
ON f.BrowserID=b.BrowserID

GROUP BY
d.DeviceName,
b.BrowserName

ORDER BY PurchaseRate DESC;

SELECT

t.TrafficSourceName,

e.ExperimentGroup,

COUNT(*) AS Users,

ROUND(AVG(f.Revenue),2) AS AvgRevenue,

ROUND(100*AVG(f.Purchased),2) AS PurchaseRate

FROM fact_experiment f

JOIN dim_traffic_source t
ON f.TrafficSourceID=t.TrafficSourceID

JOIN dim_experiment e
ON f.ExperimentID=e.ExperimentID

GROUP BY
t.TrafficSourceName,
e.ExperimentGroup

ORDER BY
t.TrafficSourceName,
e.ExperimentGroup;

SELECT

COUNT(*) AS TotalVisitors,

SUM(ClickedCTA) AS TotalClicks,

SUM(AddedToCart) AS TotalCart,

SUM(Purchased) AS TotalPurchases,

ROUND(SUM(Revenue),2) AS TotalRevenue,

ROUND(AVG(Revenue),2) AS AvgRevenuePerUser,

ROUND(100*AVG(ClickedCTA),2) AS CTR,

ROUND(100*AVG(AddedToCart),2) AS CartRate,

ROUND(100*AVG(Purchased),2) AS ConversionRate,

ROUND(AVG(SessionDuration),2) AS AvgSessionDuration,

ROUND(AVG(PagesViewed),2) AS AvgPagesViewed

FROM fact_experiment;