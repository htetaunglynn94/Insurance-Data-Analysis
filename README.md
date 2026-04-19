# 📊 Insurance Data Analysis (Power BI Project)

## Project Overview

This project analyzes insurance operational data and customer feedback to evaluate **business performance** and **customer satisfaction**. The objective is to identify **service gaps**, uncover **behavioral patterns**, and generate **data-driven insights** using sentiment analysis.

The dashboard was developed using **Power BI**, with sentiment scoring implemented via **Python (TextBlob)**.

**PowerBI Project Link**: [Insurance Data Analysis.pbix](https://app.powerbi.com/links/Amp_dpANyx?ctid=35ae1710-01c9-4681-aee5-aefcb73885b1&pbi_source=linkShare)

> **Note:** Due to the limitations of the Power BI Free version, the built-in *AI Insights (Text Analytics)* feature was not available. Therefore, sentiment analysis was performed using Python scripting.

---

## Objectives

🔹 Enable interactive filtering using `Policy Number`, `Claim Number`, and `Customer ID`

🔹 Analyze key financial metrics:  
  * Premium Amount
  * Claim Amount
  * Coverage Amount

🔹 Evaluate Active vs Inactive policy distribution  
🔹 Analyze customer segmentation by Age Group  
🔹 Examine insurance investment patterns by gender  
🔹 Measure customer satisfaction using sentiment analysis  
🔹 Provide actionable business insights

---

## Dataset Information

* Source 1: [Insurance Data.csv](https://github.com/user-attachments/files/26845606/Insurance.Data.csv)
* Source 2: [Insurance Customer Feedback.xlsx](https://github.com/user-attachments/files/26845618/insurance_customer_feedback.xlsx)

---

## Data Mining & Processing Steps

### 1️⃣ Data Loading

* Imported `Insurance Data.csv` into **SQL Server** to simulate a database environment
* Connected SQL Server database to **Power BI**
* Loaded customer feedback dataset (`.xlsx`) into Power BI

---

### 2️⃣ Data Preprocessing

#### 🔹 Insurance Dataset

* Validated data types and structure
* Standardized column naming conventions
* Created derived column: **Age Group**
* Implemented **Row-Level Security (RLS)**
* Published and configured **Pinned Dashboard**

#### 🔹 Customer Feedback Dataset

* Performed sentiment analysis using Python
* Applied **TextBlob** for NLP scoring
* Generated:

  * **Polarity Score** (range: -1 to +1)
  * **Satisfaction Score** (normalized: 0 to 1)

```python
from textblob import TextBlob
import pandas as pd

dataset.columns = dataset.columns.str.strip()

dataset['Polarity'] = dataset['Feedback'].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity
)

dataset['Satisfaction Score'] = dataset['Polarity'].apply(
    lambda x: round((x + 1) / 2, 4)
)
```

---

### 3️⃣ Data Visualization (Power BI)

#### Report Pages

**Overview**

* Stacked Bar Chart
* Donut Chart
* Slicer
* KPI Card
* Ribbon Chart
* Matrix
* Multi-row Card
* Line Chart with Area

**Table**

* Detailed tabular view of insurance dataset

**Feedback**

* Word Cloud
* Table
* Stacked Bar Chart

**Insights**

* Summary visuals highlighting key findings

---

### 4️⃣ Data Analysis & Insights

#### Insurance Data Analysis

**Age Group Distribution**

| Age Range | Group  | Ratio  |
| --------- | ------ | ------ |
| ≤ 30      | Youth  | 18.88% |
| ≤ 60      | Adult  | 42.92% |
| > 60      | Senior | 38.19% |

**Key Insights**

* Adults and Seniors represent the **largest proportion of policyholders**
* The **highest claim amounts** are observed in the Adult group, followed by Seniors
* **Travel insurance** has the highest adoption rate among policy types
* Gender-based investment patterns:

  * `Males` → higher in **Health** and **Home** insurance
  * `Females` → higher in **Travel** and **Life** insurance
* Observed anomaly:

  * Total **Claim Amount exceeds Premium Amount**, indicating potential issues such as:

    * aggregation bias
    * missing non-claim records
    * data inconsistency or
    * incompleted dataset
    
* **Coverage Amount** remains highest as it represents maximum insured limits

---

#### Customer Feedback Analysis

**Satisfaction Classification**

| Sentiment Score | Satisfaction Level | No. of Customers |
| --------------- | ------------------ | ---------------- |
| ≥ 0.8           | Excellent          | 27               |
| ≥ 0.6           | Good               | 39               |
| < 0.6           | Needs Improvement  | 31               |

**Key Insights**

* A significant portion of customers fall into the **“Needs Improvement”** category
* Common improvement areas identified:

  * Response time
  * Pricing perception
  * Documentation complexity
  * Process efficiency
  * Communication clarity
  * Proactive customer support

---

## Conclusion

This analysis highlights that while the insurance business demonstrates **strong customer participation**, there are notable opportunities to improve both **operational efficiency** and **customer experience**.

From an operational perspective, the imbalance between **Claim Amount and Premium Amount** suggests potential data limitations or structural inefficiencies that require further validation and refinement. Additionally, customer distribution indicates that **Adults and Seniors are the primary contributors** to both revenue and claims.

From a customer experience perspective, sentiment analysis reveals that although many customers report satisfactory experiences, a considerable segment remains **unsatisfied or neutral**, indicating gaps in service delivery. Key drivers of dissatisfaction include **slow response times, complex procedures, and unclear communication**.

Overall, improving service consistency, simplifying processes, and enhancing responsiveness can significantly increase customer satisfaction and business performance. Furthermore, incorporating more comprehensive data (including non-claim records) and advanced analytics models would strengthen future insights.

---

## Tools Used

* Power BI (Data Visualization)
* Python (TextBlob for Sentiment Analysis)
* SQL Server (Data Storage & Integration)
* Excel / CSV (Data Sources)

---

## Contact

If you have feedback or opportunities, feel free to connect:

* [LinkedIn](https://www.linkedin.com/in/htet-aung-lynn-64ba06146/)
* [GitHub](https://github.com/htetaunglynn94)

---
