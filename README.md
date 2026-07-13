
<h1 align="center">📊 A/B Testing Product Analytics Dashboard</h1>

<p align="center">
An end-to-end Product Analytics project built using <b>Python</b>, <b>MySQL</b>, <b>SQL</b>, and <b>Power BI</b> to evaluate website experiments and deliver business recommendations through interactive dashboards.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=for-the-badge&logo=powerbi)
![SQL](https://img.shields.io/badge/SQL-Analytics-blue?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-Version%20Control-red?style=for-the-badge&logo=git)

</p>

---

# 📌 Project Overview

This project simulates a real-world **A/B Testing Product Analytics workflow** used by modern technology companies to evaluate whether a new product experience should replace an existing one.

The project analyzes the performance of a **Current Website (Control Group)** and a **New Website (Variant Group)** using business metrics including:

- Revenue
- Conversion Rate
- Purchases
- Session Duration
- Pages Viewed
- User Segmentation
- Device Performance
- Browser Performance
- Traffic Sources

The complete pipeline includes data generation, database modeling, SQL analysis, Power BI dashboards, and executive business recommendations.

---

# 🎯 Business Objective

Determine whether the redesigned website delivers measurable business improvements compared to the current website.

The analysis answers questions such as:

- Which website generates higher revenue?
- Which website converts more users?
- Does user engagement improve?
- Should the new website be deployed to production?

---

# 🛠 Technology Stack

| Category | Tools |
|----------|-------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Data Generation | Faker |
| Database | MySQL |
| Query Language | SQL |
| Dashboard | Power BI |
| Analytics | DAX |
| Version Control | Git |
| Repository | GitHub |

---

# 🏗 Project Architecture

```text
Python
   │
Generate Synthetic Data
   │
CSV Files
   │
MySQL Database
   │
Star Schema
   │
SQL Analytics
   │
Power BI Dashboard
   │
Business Insights & Recommendations
```

---

# ⭐ Database Design

The project uses a **Star Schema** for efficient analytical reporting.

## Fact Table

- fact_experiment

## Dimension Tables

- dim_user
- dim_date
- dim_device
- dim_browser
- dim_traffic_source
- dim_experiment

---

# 📊 Dashboard Pages

## 1️⃣ Executive Overview

Provides a high-level summary of the experiment.

### KPIs

- Total Users
- Total Revenue
- Total Purchases
- Conversion Rate
- Average Session Duration
- Average Pages Viewed

### Visualizations

- Revenue Comparison
- Conversion Rate Comparison
- Executive KPIs
- Interactive Filters

---

## 2️⃣ Experiment Deep Dive

Detailed comparison between the Current Website and New Website.

Includes:

- Revenue Comparison
- Purchase Comparison
- Conversion Funnel
- Session Analysis
- User Engagement Analysis

---

## 3️⃣ User Segmentation Dashboard

Analyzes customer behavior across different user segments.

Includes:

- Users by Country
- Revenue by Device
- Revenue by Browser
- Traffic Source Analysis
- Gender Distribution

---

## 4️⃣ Business Insights & Recommendations

Executive summary of the experiment.

Includes:

- Winning Variant
- Revenue Lift
- Conversion Lift
- Executive Findings
- Business Recommendations
- KPI Comparison Table

---

# 📷 Dashboard Preview

## Executive Overview

<img src="Images/01_Executive_Overview.png" width="100%">

---

## Experiment Deep Dive

<img src="Images/02_Experiment_Deep_Dive.png" width="100%">

---

## User Segmentation Dashboard

<img src="Images/03_User_Segmentation.png" width="100%">

---

## Business Insights & Recommendations

<img src="Images/04_Business_Insights.png" width="100%">

---

# 📈 Key Findings

✅ The **New Website** generated significantly higher revenue.

✅ Conversion Rate improved substantially.

✅ Total Purchases increased.

✅ User engagement remained stable while business performance improved.

### Final Recommendation

**Deploy the New Website to all users.**

Continue monitoring:

- Customer Retention
- Checkout Funnel
- Product Pages
- User Engagement

---

# 📂 Repository Structure

```text
AB-Testing-Product-Analytics
│
├── Dataset
│   ├── fact_experiment.csv
│   ├── dim_user.csv
│   ├── dim_device.csv
│   ├── dim_browser.csv
│   ├── dim_date.csv
│   ├── dim_traffic_source.csv
│   └── dim_experiment.csv
│
├── Images
│   ├── banner.png
│   ├── 01_Executive_Overview.png
│   ├── 02_Experiment_Deep_Dive.png
│   ├── 03_User_Segmentation.png
│   └── 04_Business_Insights.png
│
├── Python
│
├── SQL
│
├── Power BI
│
├── README.md
│
└── requirements.txt
```

---

# 🚀 Skills Demonstrated

### Product Analytics

- A/B Testing
- Product Metrics
- Funnel Analysis
- User Segmentation

### Data Engineering

- Python ETL
- Synthetic Data Generation
- Data Cleaning
- Star Schema Modeling

### SQL

- Joins
- Aggregations
- Business Queries
- KPI Analysis

### Business Intelligence

- Power BI
- DAX
- Dashboard Design
- Interactive Reports

### Business Analysis

- Executive Reporting
- Data Storytelling
- KPI Development
- Decision Support

---

# 🔮 Future Improvements

- Statistical Significance Testing
- Bayesian A/B Testing
- Customer Lifetime Value (CLV)
- Cohort Analysis
- Retention Analysis
- Churn Prediction
- Azure SQL Integration
- Automated ETL Pipeline
- Real-Time Power BI Dashboard

---

# 👨‍💻 Author

## Souvik Saha

**Senior Process Engineer | Aspiring Product Analyst | Data Analytics Enthusiast**

📧 Email: your_email@example.com

💼 LinkedIn: https://linkedin.com/in/your-linkedin

💻 GitHub: https://github.com/your-github

---

<p align="center">

⭐ If you found this project useful, please consider giving it a star!

</p>
