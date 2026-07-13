
<div align="center">

# 📊 A/B Testing Product Analytics Dashboard

### End-to-End Product Analytics Project using Python, MySQL, SQL & Power BI

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=for-the-badge&logo=powerbi)
![SQL](https://img.shields.io/badge/SQL-Analytics-blue?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?style=for-the-badge&logo=github)

</div>

---

# 📌 Project Overview

This project demonstrates an **end-to-end Product Analytics workflow** by analyzing an A/B experiment comparing a **Current Website (Control Group)** against a **New Website (Variant Group)**.

The objective is to determine whether the redesigned website improves business performance through data-driven decision making.

The project covers the complete analytics lifecycle:

- Data Generation
- Data Engineering
- Data Modeling
- SQL Analytics
- Statistical Analysis
- Dashboard Development
- Executive Business Recommendations

---

# 🎯 Business Objective

The company redesigned its website and wanted to answer one critical business question:

> **Should we replace the Current Website with the New Website?**

To answer this, we analyzed:

- Revenue
- Conversion Rate
- Purchases
- User Engagement
- Session Duration
- Device Performance
- Browser Performance
- Traffic Sources
- User Segmentation

---

# 🛠 Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Data Generation | Faker |
| Database | MySQL |
| Query Language | SQL |
| BI Tool | Power BI |
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

             Star Schema Model

                     │

               SQL Analysis

                     │

             Power BI Dashboard

                     │

        Executive Recommendations
```

---

# ⭐ Star Schema

```
                    dim_user

                        |

                    fact_experiment

      /          |          |          \

dim_device  dim_browser  dim_date  dim_experiment

                        |

             dim_traffic_source
```

---

# 📂 Dataset

The project contains approximately **100,000 experiment records**.

### Fact Table

- fact_experiment

### Dimension Tables

- dim_user
- dim_device
- dim_browser
- dim_date
- dim_traffic_source
- dim_experiment

---

# 📊 Dashboard Pages

---

## 📈 Executive Overview

High-level business KPIs.

### KPIs

- Total Users
- Revenue
- Purchases
- Conversion Rate
- Average Session Duration
- Average Pages Viewed

### Visualizations

- Revenue by Experiment
- Conversion Rate by Experiment
- Interactive Filters

---

## 🧪 Experiment Deep Dive

Compares the Control and Variant groups.

Includes

- Revenue Comparison
- Purchase Comparison
- Conversion Comparison
- User Engagement
- Conversion Funnel

---

## 👥 User Segmentation

Analyzes customer behavior by

- Country
- Device
- Browser
- Traffic Source
- Gender

---

## 💼 Business Insights & Recommendations

Executive Summary

Includes

- Winning Variant
- Revenue Lift
- Conversion Lift
- Key Findings
- Business Recommendations
- KPI Comparison

---

# 📷 Dashboard Preview

## Executive Overview

![Executive Overview](Images/01_Executive_Overview.png)

---

## Experiment Deep Dive

![Experiment Deep Dive](Images/02_Experiment_Deep_Dive.png)

---

## User Segmentation

![User Segmentation](Images/03_User_Segmentation.png)

---

## Business Insights

![Business Insights](Images/04_Business_Insights.png)

---

# 📈 Key Business Insights

### ✅ New Website outperformed the Current Website

Key observations

- Higher Revenue
- Higher Conversion Rate
- More Purchases
- Stronger Customer Engagement
- Better Overall Business Performance

---

# 💡 Final Recommendation

Deploy the **New Website** to all users.

Continue monitoring:

- Customer Retention
- Checkout Funnel
- Session Duration
- Purchase Frequency

Run additional A/B tests for:

- Product Pages
- Checkout Flow
- Pricing Strategy
- Landing Pages

---

# 📁 Repository Structure

```text
AB-Testing-Product-Analytics/

│

├── Dataset/

│   ├── dim_user.csv

│   ├── dim_device.csv

│   ├── dim_browser.csv

│   ├── dim_date.csv

│   ├── dim_traffic_source.csv

│   ├── dim_experiment.csv

│   └── fact_experiment.csv

│

├── Images/

│

├── Power BI/

│

├── Python/

│

├── SQL/

│

├── README.md

└── requirements.txt
```

---

# 🚀 Skills Demonstrated

### Product Analytics

- A/B Testing
- Experiment Design
- KPI Development
- Funnel Analysis

### Data Engineering

- Python ETL
- Data Cleaning
- Data Modeling
- Star Schema

### SQL

- Complex Joins
- Aggregations
- Business Queries
- Performance Analysis

### Business Intelligence

- Power BI
- DAX
- Dashboard Design
- Storytelling

### Business Analysis

- Executive Reporting
- Data Visualization
- Customer Segmentation
- Business Recommendations

---

# 🔮 Future Enhancements

- Bayesian A/B Testing
- Statistical Significance Testing
- Revenue Forecasting
- Customer Lifetime Value (CLV)
- Cohort Analysis
- Retention Analysis
- Churn Prediction
- Real-Time Dashboard
- Automated ETL Pipeline
- Cloud Deployment (Azure / AWS)

---

# 👤 Author

## Sneha Saha 

Software QA Analyst | Aspiring Product Analyst | Data Analytics Enthusiast

📧 Email: sneha.pes19@gmail.com

🔗 LinkedIn:https://www.linkedin.com/in/snehasaha2001/


💻 GitHub: https://github.com/Snehasaha1

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

</div>
