import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

FILE_NAME = "Project2.csv"


def create_sample_data():

    sample_data = {
        "Student_ID": list(range(1, 21)),
        "Attendance": [
            90, 85, 70, 95, 80,
            88, 76, 92, 65, 98,
            82, 87, 73, 91, 78,
            84, 69, 94, 89, 96
        ],
        "Study_Hours": [
            5, 4, 2, 6, 3,
            5, 4, 6, 2, 7,
            4, 5, 3, 6, 4,
            5, 2, 6, 5, 7
        ],
        "Assignment_Score": [
            85, 80, 65, 90, 75,
            84, 72, 89, 60, 95,
            78, 83, 68, 90, 74,
            81, 63, 91, 86, 94
        ],
        "Internal_Marks": [
            80, 75, 60, 88, 72,
            82, 70, 90, 58, 94,
            76, 81, 66, 89, 73,
            80, 61, 90, 84, 93
        ],
        "Final_Marks": [
            84, 78, 62, 91, 74,
            85, 71, 92, 59, 96,
            77, 83, 67, 90, 74,
            81, 62, 91, 85, 95
        ]
    }

    df = pd.DataFrame(sample_data)

    df.to_csv(FILE_NAME, index=False)

    return df


def load_data():

    if not os.path.exists(FILE_NAME):

        print("\nDataset not found.")
        print("Creating sample dataset...\n")

        return create_sample_data()

    try:

        df = pd.read_csv(FILE_NAME)

        if df.empty:

            print("Dataset is empty.")
            print("Loading sample records...\n")

            return create_sample_data()

        return df

    except Exception:

        print("Unable to read dataset.")
        print("Creating new dataset...\n")

        return create_sample_data()


def view_dataset():

    df = load_data()

    print("\n========== Student Records ==========\n")

    print(df.to_string(index=False))

    print()


def dataset_summary():

    df = load_data()

    print("\n========== Dataset Summary ==========\n")

    print("Total Students :", len(df))
    print("Total Columns  :", len(df.columns))

    print("\nColumns")

    for column in df.columns:
        print("-", column)

    print("\nMissing Values")

    print(df.isnull().sum())

    print()


def train_model():

    df = load_data()

    X = df[
        [
            "Attendance",
            "Study_Hours",
            "Assignment_Score",
            "Internal_Marks"
        ]
    ]

    y = df["Final_Marks"]

    model = LinearRegression()

    model.fit(X, y)

    return model

def predict_marks():

    model = train_model()

    try:

        attendance = float(input("Enter Attendance (%): "))
        study_hours = float(input("Enter Study Hours: "))
        assignment = float(input("Enter Assignment Score: "))
        internal = float(input("Enter Internal Marks: "))

        data = pd.DataFrame({
            "Attendance": [attendance],
            "Study_Hours": [study_hours],
            "Assignment_Score": [assignment],
            "Internal_Marks": [internal]
        })

        prediction = model.predict(data)

        print(f"\nPredicted Final Marks : {prediction[0]:.2f}")

    except Exception:
        print("Invalid Input.")


def search_student():

    df = load_data()

    try:

        student_id = int(input("Enter Student ID: "))

        result = df[df["Student_ID"] == student_id]

        if result.empty:
            print("Student not found.")
        else:
            print("\nStudent Details\n")
            print(result.to_string(index=False))

    except Exception:
        print("Invalid Input.")


def top_performer():

    df = load_data()

    topper = df[df["Final_Marks"] == df["Final_Marks"].max()]

    print("\nTop Performer\n")

    print(topper.to_string(index=False))


def performance_statistics():

    df = load_data()

    print("\nPerformance Statistics\n")

    print(f"Average Final Marks : {df['Final_Marks'].mean():.2f}")
    print(f"Highest Marks       : {df['Final_Marks'].max()}")
    print(f"Lowest Marks        : {df['Final_Marks'].min()}")


def visualize_data():

    df = load_data()

    while True:

        print("\nVisualization Menu")
        print("1. Attendance vs Final Marks")
        print("2. Study Hours vs Final Marks")
        print("3. Return")

        try:

            choice = int(input("Enter Choice: "))

            if choice == 1:

                plt.figure(figsize=(6,4))

                plt.scatter(df["Attendance"], df["Final_Marks"])

                plt.title("Attendance vs Final Marks")
                plt.xlabel("Attendance")
                plt.ylabel("Final Marks")

                plt.show()

            elif choice == 2:

                plt.figure(figsize=(6,4))

                plt.scatter(df["Study_Hours"], df["Final_Marks"])

                plt.title("Study Hours vs Final Marks")
                plt.xlabel("Study Hours")
                plt.ylabel("Final Marks")

                plt.show()

            elif choice == 3:

                break

            else:

                print("Invalid Choice.")

        except Exception:

            print("Invalid Input.")

def menu():

    while True:

        print("\n" + "=" * 45)
        print("STUDENT PERFORMANCE PREDICTION SYSTEM")
        print("=" * 45)
        print("1. View Student Records")
        print("2. Dataset Summary")
        print("3. Search Student")
        print("4. Performance Statistics")
        print("5. Visualize Dataset")
        print("6. Predict Final Marks")
        print("7. Show Top Performer")
        print("8. Exit")

        try:

            choice = int(input("\nEnter Choice : "))

            if choice == 1:

                view_dataset()

            elif choice == 2:

                dataset_summary()

            elif choice == 3:

                search_student()

            elif choice == 4:

                performance_statistics()

            elif choice == 5:

                visualize_data()

            elif choice == 6:

                predict_marks()

            elif choice == 7:

                top_performer()

            elif choice == 8:

                print("\nThank You!")
                break

            else:

                print("Invalid Choice.")

        except Exception:

            print("Please Enter a Valid Number.")


if __name__ == "__main__":

    menu()