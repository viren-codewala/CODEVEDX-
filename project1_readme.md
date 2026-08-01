# Utility Usage Prediction Tool

> **AI/ML Internship Project 1 – CODEVEDX**

---

## Project Overview

The **Utility Usage Prediction Tool** is a Python-based console application developed as part of the **CODEVEDX AI/ML Internship**. The application enables users to manage electricity usage records stored in a CSV file and estimate future electricity consumption using a Machine Learning model.

The system follows a menu-driven approach and allows users to add, update, delete, and view electricity usage records. It uses the **Linear Regression** algorithm from the Scikit-learn library to predict electricity usage for future days based on historical data.

This project demonstrates the integration of **Python programming**, **CSV file handling**, and **Machine Learning** in a simple real-world application.

---

# Objectives

- Develop a menu-driven console application.
- Implement CRUD (Create, Read, Update, Delete) operations.
- Store and manage records using CSV files.
- Learn data manipulation using Pandas.
- Apply Linear Regression for prediction.
- Improve Python programming and exception handling skills.
- Understand the basics of Machine Learning.

---

# Features

- ✅ Menu-driven console interface
- ✅ Add electricity usage records
- ✅ Update existing records
- ✅ Delete records
- ✅ View all stored records
- ✅ Automatic CSV file creation (if missing)
- ✅ Sample dataset generation
- ✅ Future electricity usage prediction
- ✅ Exception handling for invalid inputs
- ✅ Easy-to-use interface

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | CSV File Handling |
| Scikit-learn | Machine Learning Model |
| Linear Regression | Prediction Algorithm |
| CSV | Data Storage |
| Visual Studio Code | Development Environment |

---

# Software Requirements

- Python 3.10 or above
- Visual Studio Code
- Pandas Library
- Scikit-learn Library

### Install Required Libraries

```bash
pip install pandas scikit-learn
```

---

# Machine Learning Algorithm

## Linear Regression

Linear Regression is a supervised Machine Learning algorithm used for predicting continuous numerical values. In this project, the algorithm learns the relationship between the **day number** and **electricity consumption** from historical data. Based on this relationship, it predicts electricity usage for future days.

---

#  Dataset

### Dataset Name

```
Project1.csv
```

### Dataset Columns

| Column | Description |
|---------|-------------|
| Day | Day Number |
| Electricity_Usage | Electricity Consumption (Units) |

### Sample Dataset

| Day | Electricity Usage |
|----:|------------------:|
|1|120|
|2|125|
|3|130|
|4|128|
|5|135|
|...|...|
|30|203|

---

# Project Structure

```
Project1_UtilityUsage/
│
├── project1_Screenshots/
│
├── Project1.py
│
├── Project1.csv
│
├── project1_read.md
│
├── Project1_Report.docx
│
└── Project1_Presentation.pptx
```

---

# How the Project Works

1. Start the application.
2. Load or create the CSV dataset.
3. Display the main menu.
4. Perform CRUD operations on electricity records.
5. Save updated records to the CSV file.
6. Train the Linear Regression model using the available data.
7. Enter a future day number.
8. Display the predicted electricity usage.
9. Exit the application.

---

# Running the Project

Clone the repository:

```bash
git clone https://github.com/viren-codewala/CODEVEDX.git
```

Open the project folder.

Install dependencies:

```bash
pip install pandas scikit-learn
```

Run the application:

```bash
python Project1.py
```

---

# Console Menu

```
==========================================
      UTILITY USAGE PREDICTION TOOL
==========================================

1. Add Record
2. Update Record
3. Delete Record
4. View Records
5. Predict Usage
6. Exit
```

---

# Future Enhancements

- Develop a Graphical User Interface (GUI)
- Integrate MySQL Database
- Add graphical visualization using Matplotlib
- Export prediction reports as PDF
- Monthly and yearly usage analytics
- Support multiple utility types (Electricity, Water, Gas)

---

# Learning Outcomes

After completing this project, I learned:

- Python Programming Fundamentals
- CSV File Handling using Pandas
- Data Manipulation Techniques
- Exception Handling
- Linear Regression
- Basic Machine Learning Workflow
- Git & GitHub
- Console Application Development

---

# Author

**Viren A. Bhosale**

AI/ML Intern

CODEVEDX Internship Program

---

# Acknowledgement

I sincerely thank **CODEVEDX** for providing the opportunity to work on this internship project. This project helped me strengthen my understanding of Python programming, data handling, and Machine Learning concepts through practical implementation.

---

# License

This project has been developed for educational purposes as part of the **CODEVEDX AI/ML Internship Program**. It is intended solely for learning and demonstration purposes.