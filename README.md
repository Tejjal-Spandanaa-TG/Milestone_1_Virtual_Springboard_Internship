# ReviewSense – Customer Feedback Analysis

## Milestone 1 & Topic Classification (Keyword-Based)

## Project Overview

**ReviewSense** is a customer feedback analysis project designed to extract insights from raw customer feedback data.
The project consists of two major stages:

**Milestone 1 – Data Ingestion & Text Cleaning**

* Collects customer feedback data from Excel or fallback CSV
* Cleans noisy text by removing URLs, numbers, punctuation, stopwords, and extra spaces
* Produces a standardized cleaned dataset ready for analysis

**Milestone 2 – Topic Classification (Keyword-Based)**

* Classifies customer feedback into predefined categories using keyword matching
* Categories:

  * Delivery
  * Product
  * Support
  * Price
  * General

This project uses **rule-based keyword classification**, not Machine Learning or AI models.

---

## Objectives

* Read customer feedback dataset
* Clean textual feedback
* Perform keyword-based topic classification
* Display feedback along with detected category
* Save processed outputs into CSV files

---

## Technologies Used

* Python
* Pandas
* OpenPyXL
* Regular Expressions (re)
* String processing
* Matplotlib (optional visualization)

---

## Project Workflow

1. Load raw feedback data from Excel
2. Clean text (remove noise, stopwords, punctuation)
3. Generate cleaned feedback dataset
4. Apply keyword-based classification
5. Assign appropriate category
6. Save classified dataset
7. Display category distribution and sample outputs

---

## Input Files

* `ReviewSense_Customer_Feedback_5000.xlsx` (Primary input)
* `Milestone1_Cleaned_Feedback.csv` (Generated cleaned dataset)

---

## Output Files

* `Milestone1_Cleaned_Feedback.csv` – Cleaned feedback dataset
* `Classified_Feedback.csv` – Feedback with assigned categories

---

## Installation

Install required libraries:

```bash
pip install pandas openpyxl matplotlib
```

---

## How to Run

### Step 1 – Text Cleaning (Milestone 1)

```bash
python milestone1.py
```

### Step 2 – Topic Classification

```bash
python classify.py
```

---

## Key Features

* Robust file loading (Excel preferred → CSV fallback)
* Automatic skipping of redundant cleaning
* Keyword-based topic classification
* Category distribution summary
* CSV output generation for further analysis

---

## Advantages

* Simple, interpretable rule-based system
* No machine learning required
* Fast processing for large feedback datasets
* Easy to extend with additional keywords

---

## Future Enhancements

* Expand keyword dictionary for higher accuracy
* Add visualization dashboard using Streamlit
* Integrate sentiment analysis module
* Implement machine learning comparison models

---

## Author

**ReviewSense – Customer Feedback Insight Extraction**
Infosys Springboard Milestone Submission

