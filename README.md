# Climate Challenge: Africa Climate Resilience (COP32)

## Overview
This project focuses on analyzing historical climate data (2015–2026) for five critical African regions: **Ethiopia, Nigeria, Kenya, Sudan, and Tanzania**. The goal is to provide a "Gold Standard" cleaned dataset and localized exploratory insights to support **COP32 Resilience Planning**.

## Project Architecture
The repository is designed for modularity and professional data engineering workflows:

```text
climate-challenge-week0/
├── .github/workflows/         # CI/CD Pipelines
├── app/                       # Streamlit interactive dashboard
├── data/                      # Local data storage (Git-ignored)
├── notebooks/                 # Standardized EDA for 5 Regions
├── src/                       # Modular logic & functions
├── scripts/                   # Automation scripts
├── tests/                     # Quality assurance tests
└── requirements.txt           # Dependency management
```

## Reproducibility Guide
Follow these steps to set up the development environment on your local machine:

**1. Clone the Repository**
```bash
git clone https://github.com/SimretAbebe/climate-challenge-week0.git
cd climate-challenge-week0
```

**2. Initialize Virtual Environment**
```bash
python -m venv venv
# Windows: venv\Scripts\activate | macOS/Linux: source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## Interim Report: Tasks 1 & 2

### Task 1 Summary: Git & Environment Setup
- **Repository Management:** Successfully initialized the `climate-challenge-week0` repository with a standardized folder structure.
- **Branching Strategy:** Followed a feature-branching workflow (`task-1`, `eda-sudan`, `eda-tanzania`, etc.) to maintain a clean `main` branch and ensure structured collaboration.
- **CI/CD:** Configured a GitHub Actions workflow (`unittests.yml`) to automatically verify dependencies and code integrity on every push.
- **Environment:** Created a `requirements.txt` file and documented setup steps to ensure full reproducibility across different local environments.

---

### Task 2 Approach: Data Profiling & Cleaning
- **Data Standardization:** Developed a "Gold Standard" EDA template in Jupyter Notebooks to ensure consistent analysis across multiple African regions, including **Ethiopia, Sudan, and Tanzania**.
- **Cleaning Pipeline:**
    - **Handling Sentinel Values:** Identified and converted NASA sentinel values (`-999`) to `NaN` to prevent statistical skewing.
    - **Integrity Check:** Verified data consistency, achieving a 0% missing value report across the dataset (4,108 days per region).
    - **Statistical Analysis:** Used **Z-score analysis** (threshold > 3) to identify extreme climatic outliers.
- **Outlier Strategy:** Chose to **retain** extreme events (e.g., intense tropical rainfall peaks in Tanzania) rather than removing them, as these "climatic pulses" are vital for accurate resilience modeling.
- **EDA & Visualization:**
    - **Time-Series Analysis:** Generated monthly average temperature and rainfall plots with annotations for historical peaks and lows.
    - **Correlation Studies:** Used heatmaps to identify strong inverse relationships between temperature ranges and humidity.
    - **Distribution & Intensity:** Utilized Histograms (Log-Scale for rainfall) and Bubble Charts to visualize the link between thermal "sweet spots" and rainfall intensity.
- **Export:** All processed data was exported as clean `.csv` files for downstream modeling, while keeping large data files excluded from version control via `.gitignore`.

---
### Task 3 Approach: Cross-Country Climate Comparison
- **Modular Codebase:** Refactored individual region notebooks to use centralized data cleaning logic located in `src/data_utils.py`, improving maintainability and ensuring DRY (Don't Repeat Yourself) principles.
- **Statistical Significance:** Conducted a One-way ANOVA test on temperature (T2M) across all 5 countries, yielding a *p*-value < 0.05. This statistically proved significant regional climatic disparities.
- **Extreme Event Metrics:** Aggregated the "Gold Standard" datasets to calculate the frequency of extreme heat days ($T_{max} > 35^\circ C$) and Maximum Consecutive Dry Days.
- **COP32 Ranking:** Developed a Climate Vulnerability Ranking based on multi-country aggregated data, supporting policy decisions with hard scientific observations.
- **Git Governance:** Utilized a clean "Paper Trail" by creating dedicated branches, opening documented Pull Requests with explicit evidence, and merging them cleanly into `main` based on reviewer feedback.

---

## **Data Governance & Dictionary**
To ensure transparency and reproducibility, all data follows a strict naming and storage convention:

| Data Type | Location | Naming Convention |
| :--- | :--- | :--- |
| **Raw Data** | `/data/raw/` | `NASA_POWER_[Country]_Yearly.csv` |
| **Processed Data** | `/data/processed/` | `[country]_clean.csv` |

**Naming Convention:** Files are prefixed with the data source (**NASA_POWER**) or suffixed with the status (**_clean**) to ensure compatibility with automated ingestion and modeling scripts.

---

## Bonus Phase

### Bonus Task: Interactive Streamlit Dashboard
- **Dynamic Analysis:** Built an interactive web application using **Streamlit** to dynamically explore temperature trends and precipitation distributions across the 5 African regions.
- **Custom Styling:** The dashboard features a premium dark-mode UI with customized KPI metric cards and exact style-matching for scientific charts (using the *viridis* palette) derived from the Jupyter notebooks.
- **Data Pipeline:** Implemented a robust data loading utility (`app/utils.py`) to seamlessly pull and aggregate processed CSVs from the `data/processed/` directory.

#### **How to Run the Dashboard Locally:**
1. Ensure your virtual environment is active and dependencies are installed.
2. Run the Streamlit application:
```bash
streamlit run app/main.py
```

