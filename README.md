# 🚀 Spam Classifier Project

This is a machine learning project to classify messages as **spam** or **not spam** using text classification techniques. I followed a YouTube tutorial to understand the full ML workflow — from preprocessing to deployment.

---

## 🔍 What I Learned

### 📊 Feature Engineering & EDA
- Created custom features like:
  - Number of characters
  - Number of words
  - Number of sentences
- Analyzed data using correlation matrix

### 🧹 Text Preprocessing
- Converted text to lowercase
- Removed punctuation
- Tokenized text
- Used **TF-IDF Vectorizer** to convert text into numerical format

### 🧠 Model Training
- Trained and tested multiple models:
  - SVC, MultinomialNB, BernoulliNB, GaussianNB
  - Decision Tree, KNN, Random Forest
  - AdaBoost, Bagging, ExtraTrees, Gradient Boosting
- Evaluated models using Accuracy, Precision, and Confusion Matrix

✔️ **Best Model:** `ExtraTreesClassifier` (highest accuracy)

### 🐍 Python Concepts I Used
- Functions: `.isalnum()`, `" ".join()`, `msg.split()`, `.tolist()`
- Used `Pipeline` to combine preprocessing and model steps

---

## 🌐 Deployment
- Saved the model and vectorizer using **Pickle**
- Built a **Streamlit web app** to run the model in the browser

---

## ✅ Summary
This project helped me understand the end-to-end ML pipeline, from raw text to a deployed model. 
I got hands-on practice with text preprocessing, feature engineering, model comparison, and Streamlit deployment.

---


## 📬 Contact

If you'd like to connect or have any suggestions, feel free to reach out:

- **Name:** Prashant Singh  
- **Email:** [prashant41102@gmail.com]  


