# 📊 Insurance Data Analysis (Basic Power BI Project)

## Project Overview

This project analyzes insurance data and customer feedback data to evaluate **operation effectiveness** and **customer satisfaction**, identify **service performance gaps** using sentiment analysis.

The dashboard was developed in **Power BI**, with sentiment scoring powered by **Python (TextBlob)**.

**Note**: Since I can't afford to use premium licence, `Text Analytics` in `AI Insights` is not included in my PowerBI Desktop. The similar operation was run using python script.

---

## 🎯 Objectives

* `Policy Number`, `Claimed Number` and `Customer ID` are used to filter all of the charts in REPORT view.
* Show `Premium Amount`, `Claimed Amount` and `Coverage Amount`
* Identify patterns in order to sentiment score
* Detect hidden trends affecting customer experience
* Provide actionable business insights

---

## Dataset Information

* Source 1: [Insurance Data.csv](https://github.com/user-attachments/files/26845606/Insurance.Data.csv)
* Source 2: [Insurance_customer_feedback.xlsx](https://github.com/user-attachments/files/26845618/insurance_customer_feedback.xlsx)

---

## ⚙️ Data Mining & Processing Steps

### Data Loading
* Imported `Insurance Data.csv` into SQL server to create database 
* Imported database file into Power BI for new practice
* Loaded `Insurance_customer_feedback.xlsx` 

---

### Data Cleaning

* Insurance dataset
    * Verify data type and structure
    * Standardized column names
    * Created conditional columns for `Age Group`
    * Created **Role Level Security**
    * Created **Pinned Dashboard**
* Customer Feedback dataset
    * Sentiment Feedback analysis using python script
    * Used **TextBlob** for sentiment scoring
    * Generated:
        * Polarity Score → range (-1 to +1)
        * Satisfaction Score → normalized (0 to 1)

```python
from textblob import TextBlob
import pandas as pd

# Clean column names (important for Power BI)
dataset.columns = dataset.columns.str.strip()

# Calculate polarity (-1 to +1)
dataset['Polarity'] = dataset['Feedback'].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity
)

# Convert to positive satisfaction score (0 to 1)
dataset['Satisfaction Score'] = dataset['Polarity'].apply(
    lambda x: round((x + 1) / 2, 4)
)
```

---

### Data Visualization (Power BI)
1. Overview
    * Stacked bar chart
    * Donut chart
    * 3 x Slicers
    * 3 x Cards
    * Ribbon chart
    * Matrix
    * Multi-row card
    * Line chart with shaded area

2. Table    
    * Show all the data of `Insurance` dataset

3. Feedback
    * WordCloud
    * Table
    * Stacked Bar Chart
---

### Data Mining

#### Insurance Data analysis

* Grouping Age

    |   Age   | Level  | Ratio  |
    | ------- | ------ | ------ |
    | &le; 30 | Youth  | 18.88% |
    | &le; 60 | Adult  | 42.92% |
    | >  60   | Senior | 38.19% |

👉 **Insight**:

As per Age Group statistics:- 
* Most of the Adult and Senior people are invested for insurance.
* The most total claim amount by age group is Adults followed by Seniors.
* Travel insurance is the most Premium and Claim Amount

#### Customer Feedback Analysis

* `Satisfaction` was grouped from `Sentiment Score`

| Sentiment Score    | Satisfaction        |No. of Customers|
| -------- | --------------------|----------------|
|&ge; 0.8  |  Excellent          |       27       |
|&ge; 0.6  |  Good               |       39       |
|   < 0.6  |  Need improvement   |       31       |


👉 **Insight**:
* Service is needed to be improved:-
    * Improve response time
    * Consider for price rating
    * Compact documentation
    * Reduce unnecessary procedures
    * Enhance communication clarity
    * Offer proactive support
---

## Conclusion

This analysis reveals that while customer sentiment is generally positive, there are significant opportunities to:

* Improve consistency
* Convert neutral users into satisfied customers
* Address recurring service issues

These improvements can lead to **higher retention and better customer experience**.

---

## Tools Used

* Power BI (Visualization)
* Python (TextBlob for NLP)
* Excel / CSV (Data Source)

---

## Contact

If you have any feedback or opportunities, feel free to connect!

* [LinkedIn](https://www.linkedin.com/in/htet-aung-lynn-64ba06146/)
* [GitHub](https://github.com/htetaunglynn94)

---
