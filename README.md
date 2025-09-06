# 📊 Sales Prediction using Advertising Data

## 📌 Project Overview
This project predicts **product sales** based on advertising spend across multiple platforms (**TV, Radio, Newspaper**). The goal is to analyze how marketing investments affect sales outcomes and provide actionable insights for business strategies.

We used **Linear Regression** to build a predictive model and analyzed the importance of each advertising channel.

---

## 📂 Dataset
- **File**: `advertising.csv`
- **Columns**:
  - `TV` – advertising budget spent on TV
  - `Radio` – advertising budget spent on Radio
  - `Newspaper` – advertising budget spent on Newspaper
  - `Sales` – product sales (target variable)

Dataset source: Standard *Advertising dataset* used in regression problems.

---

## ⚙️ Steps Performed
1. **Data Cleaning**  
   - Removed unnecessary index column (`Unnamed: 0`).  
   - Checked and confirmed no missing values.  

2. **Exploratory Data Analysis (EDA)**  
   - Correlation heatmap between TV, Radio, Newspaper, and Sales.  
   - Identified strongest relationships.  

3. **Feature Selection**  
   - Selected independent variables: `TV`, `Radio`, `Newspaper`.  
   - Target variable: `Sales`.  

4. **Model Training**  
   - Used **Linear Regression** model.  
   - Split data: 80% training, 20% testing.  

5. **Model Evaluation**  
   - R² Score & RMSE calculated.  
   - Feature coefficients analyzed.  

6. **Impact Analysis**  
   - Identified which advertising channel contributes most to sales.  

---

## 📈 Results
- **R² Score**: 0.8994  
- **RMSE**: 1.78  
- **TV & Radio** have the highest positive impact on Sales.  
- **Newspaper** has very low influence compared to TV & Radio.  
- Model explains ~90% of the variance in Sales.
  
---

## 🔑 Actionable Insights
1. Focus on **TV and Radio** campaigns to maximize sales impact.  
2. Spending more on **Newspaper ads** gives diminishing returns.  
3. Optimize ad budget allocation towards the most effective channels.  
4. Use regression model to simulate outcomes before deciding ad spend.  

---

## ▶️ How to Run
1. Clone this repository:  
   ```bash
   git clone https://github.com/shubhangi-kumari/Sales-Prediction-Advertising.git
   cd Sales-Prediction-Advertising
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run Jupyter Notebook:  
   ```bash
   jupyter notebook sales_prediction.ipynb
   ```

---

## 📌 Future Scope
- Implement **Time Series Forecasting** for long-term sales prediction.  
- Explore **Polynomial Regression / Random Forest** for better accuracy.  
- Build a simple **dashboard (Streamlit / Flask)** for interactive prediction.  

---

## 👩‍💻 Author
- Developed by *Shubhangi* as part of Sales Prediction task.

---
