# AI Based Fake News Detection Tool

> **AI/ML Internship Project 3 – CODEVEDX**

---

# Project Overview

The **AI Based Fake News Detection Tool** is a Python-based Machine Learning application developed as part of the **CODEVEDX AI/ML Internship**. The system analyzes news articles using Natural Language Processing (NLP) techniques and predicts whether the news is **REAL** or **FAKE**.

The application converts textual data into numerical features using **TF-IDF Vectorization** and trains a **Logistic Regression** model for classification. It also displays prediction confidence, stores the trained model, maintains prediction history, and provides dataset analysis through a user-friendly console interface.

---

# Objectives

- Develop an AI-based Fake News Detection System.
- Perform text preprocessing using NLP.
- Train a Machine Learning classification model.
- Detect Fake and Real news articles.
- Display prediction confidence.
- Save the trained model.
- Improve Python programming and Machine Learning skills.

---

# Features

✅ View Dataset

✅ Dataset Summary

✅ Search News by Keyword

✅ Train Machine Learning Model

✅ Fake News Detection

✅ Prediction Confidence

✅ Prediction History

✅ Save Prediction History

✅ Model Information

✅ Exception Handling

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Dataset Handling |
| Scikit-learn | Machine Learning |
| TF-IDF Vectorizer | Text Feature Extraction |
| Logistic Regression | Classification Algorithm |
| Joblib | Save & Load Model |
| CSV | Dataset Storage |
| Visual Studio Code | Development Environment |

---

# Software Requirements

- Python 3.10 or above
- Visual Studio Code
- Pandas
- Scikit-learn
- Joblib

### Install Required Libraries

```bash
pip install pandas scikit-learn joblib
```

---

# Machine Learning Algorithm

## Logistic Regression

Logistic Regression is a supervised Machine Learning algorithm used for text classification. It predicts whether a news article is **REAL** or **FAKE** after learning patterns from the training dataset.

---

# NLP Technique

## TF-IDF Vectorization

TF-IDF (Term Frequency – Inverse Document Frequency) converts news articles into numerical vectors by assigning importance to words. These vectors are then used by the Machine Learning model for prediction.

---

# Dataset

### Dataset Name

```
Project3.csv
```

### Dataset Columns

| Column | Description |
|---------|-------------|
| text | News Article |
| label | REAL / FAKE |

---

# Project Structure

```
Project3_FakeNewsDetection/
│
├── Project3.py
├── Project3.csv
├── fake_news_model.pkl
├── README.md
├── Project3_Report.docx
└── Project3_Presentation.pptx
```

---

# How the Project Works

1. Load the dataset.
2. Display the main menu.
3. Train the Machine Learning model.
4. Save the trained model.
5. Enter a news article.
6. Predict whether the news is REAL or FAKE.
7. Display prediction confidence.
8. Save prediction history.

---

# Running the Project

Clone the repository

```bash
git clone https://github.com/viren-codewala/CODEVEDX.git
```

Install dependencies

```bash
pip install pandas scikit-learn joblib
```

Run the project

```bash
python Project3.py
```

---

# Console Menu

```text
=======================================================
      AI BASED FAKE NEWS DETECTION TOOL
=======================================================

1. View Dataset
2. Dataset Summary
3. Train Machine Learning Model
4. Detect Fake News
5. Search News in Dataset
6. Prediction History
7. Model Information
8. Exit
```

---

# Future Enhancements

- Develop a GUI using Tkinter
- Build a Flask Web Application
- Support Multiple Languages
- Integrate Live News APIs
- Improve Accuracy using Deep Learning (LSTM/BERT)
- Increase Dataset Size

---

# Learning Outcomes

After completing this project, I learned:

- Python Programming
- Natural Language Processing
- TF-IDF Vectorization
- Logistic Regression
- Machine Learning Workflow
- Dataset Handling using Pandas
- Joblib Model Storage
- Console Application Development

---

# Author

**Viren A. Bhosale**

AI/ML Intern

CODEVEDX Internship Program

---

# Acknowledgement

I sincerely thank **CODEVEDX** for providing me with the opportunity to work on this internship project. This project enhanced my understanding of Natural Language Processing, Machine Learning, Python programming, and text classification through practical implementation.

---

# License

This project has been developed for educational purposes as part of the **CODEVEDX AI/ML Internship Program**. It is intended solely for learning and demonstration purposes.
