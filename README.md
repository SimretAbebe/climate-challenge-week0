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