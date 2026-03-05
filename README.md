# Credit Risk Prediction using Machine Learning

## 📌 Project Overview

This project is an **end-to-end Machine Learning application** that predicts whether a loan applicant has **Good Credit Risk or Bad Credit Risk** based on financial and personal information.

The project includes:

* Data preprocessing and feature encoding
* Machine Learning model training
* Model serialization using Joblib
* Deployment of the model using a **Streamlit web application**

Users can enter applicant details through the web interface and receive **real-time credit risk predictions**.

---

## 🚀 Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-Learn**
* **XGBoost**
* **Streamlit**
* **Joblib**

---

## 📂 Project Structure

```
credit-risk-prediction/
│
├── app.py                          # Streamlit web application
├── model_training.ipynb            # Model training notebook
├── extra_trees_credit_model.pkl    # Trained ML model
├── Sex_label_encoder.pkl
├── Housing_label_encoder.pkl
├── Saving accounts_label_encoder.pkl
├── Checking account_label_encoder.pkl
├── Purpose_label_encoder.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/credit-risk-prediction.git
cd credit-risk-prediction
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit web application:

```
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Input Features

The model predicts credit risk based on the following features:

* Age
* Sex
* Job
* Housing
* Saving Accounts
* Checking Account
* Credit Amount
* Duration (months)
* Purpose of Credit

---

## 🤖 Machine Learning Model

The project uses the **Extra Trees Classifier**, an ensemble learning method that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

Model pipeline includes:

* Data preprocessing
* Label encoding for categorical variables
* Feature selection
* Model training and evaluation

---

## 📷 Application Preview

Users input applicant details and click **Predict Risk** to get the result:

* ✅ **Good Credit Risk**
* ❌ **Bad Credit Risk**

---

## 📈 Future Improvements

* Add **probability score for predictions**
* Add **feature importance visualization**
* Deploy the app on **Streamlit Cloud**
* Improve UI with better design

---

## 👤 Author

**Ankan Ghosh**

* M.Tech in Data Science
* 4+ years experience in Operations & Data Analysis
* Skills: SQL | Python | Machine Learning | Tableau | Dashboarding

---

## ⭐ If you like this project

Give the repository a **star ⭐ on GitHub**.
