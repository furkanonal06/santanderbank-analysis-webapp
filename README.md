# **Customer Churn Prediction & Segmentation Dashboard**

**An interactive web app for customer churn prediction and risk analysis**

This project is a **data-driven dashboard** designed to help **Santander Bank** analyze customer churn and implement an **early warning system** to identify at-risk customers. The app integrates **machine learning models** for **churn prediction and customer segmentation**, providing actionable insights for retention strategies.

## **🔹 Live Dashboard**
**[Santander Bank Churn Analysis Web App](https://santanderbank-analysis-webapp.onrender.com/)**

## **🔹 Key Features**
✅ **Churn Prediction Model**: Uses an **XGBoost model** to estimate churn probability for each customer  
✅ **Customer Segmentation**: Applies **K-Means clustering** to group customers based on behavior and risk factors  
✅ **Risk Analysis Dashboard**: Provides business insights using interactive visualizations  
✅ **Real-time Prediction**: Allows users to input customer details and receive an instant churn risk score  
✅ **User-Friendly UI**: Built with **Plotly Dash** for seamless data exploration and navigation  

## **🔹 Technologies Used**
- Python
- Dash (Plotly)
- XGBoost
- Scikit-learn
- Pandas & NumPy

## **🔹 Data Preprocessing & Analysis**
The dataset was preprocessed and analyzed in a separate **GitHub repository**, which includes:  
📂 **[Santander Churn Data Analysis Repo](https://github.com/furkanonal06/santanderbank-analysis)**

## **🔹 Installation & Usage**
To run the dashboard locally:

### **1️⃣ Clone the repository:**
```bash
git clone https://github.com/furkanonal06/santanderbank-analysis-webapp.git
cd santanderbank-analysis-webapp
```

### **2️⃣ Install dependencies:**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the app:**
```bash
python app.py
```

### **4️⃣ Open in your browser:**
```
http://127.0.0.1:8050/
```

## **🔹 Project Structure**
```
santanderbank-analysis-webapp/
├── assets/                 # CSS files for styling
├── models/                 # Machine learning models
├── data/                   # Processed dataset (if applicable)
├── app.py                  # Main dashboard application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── utils.py                # Helper functions for model predictions
```

