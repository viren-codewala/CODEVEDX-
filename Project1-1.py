import os
import pandas as pd
from sklearn.linear_model import LinearRegression

FILE_NAME = "Project1.csv"

def create_sample_data():
    data = {
        "Day": list(range(1, 21)),
        "Electricity_Usage": [
            95, 98, 101, 99, 104,
            107, 110, 112, 115, 118,
            120, 123, 125, 128, 130,
            133, 136, 138, 141, 144
        ]
    }
    df = pd.DataFrame(data)
    df.to_csv(FILE_NAME, index=False)
    return df

def load_data():
    if not os.path.exists(FILE_NAME):
        return create_sample_data()

    try:
        df = pd.read_csv(FILE_NAME)
        if df.empty:
            return create_sample_data()
        return df
    except:
        return create_sample_data()

def save_data(df):
    df.to_csv(FILE_NAME, index=False)

def view_data():
    df = load_data()

    if df.empty:
        print("\nNo records found.")
    else:
        print("\nCurrent Records")
        print("-" * 30)
        print(df.to_string(index=False))
        print()

def add_data():
    df = load_data()

    try:
        day = int(input("Enter Day: "))

        if day in df["Day"].values:
            print("Day already exists.")
            return

        usage = float(input("Enter Electricity Usage: "))

        new_row = pd.DataFrame({
            "Day": [day],
            "Electricity_Usage": [usage]
        })

        df = pd.concat([df, new_row], ignore_index=True)
        df = df.sort_values("Day")
        save_data(df)

        print("Record Added Successfully.")

    except:
        print("Invalid Input.")

def update_data():
    df = load_data()

    if df.empty:
        print("No data available.")
        return

    try:
        day = int(input("Enter Day to Update: "))

        if day not in df["Day"].values:
            print("Day not found.")
            return

        usage = float(input("Enter New Usage: "))

        df.loc[df["Day"] == day, "Electricity_Usage"] = usage

        save_data(df)

        print("Record Updated Successfully.")

    except:
        print("Invalid Input.")

def delete_data():
    df = load_data()

    if df.empty:
        print("No data available.")
        return

    try:
        day = int(input("Enter Day to Delete: "))

        if day not in df["Day"].values:
            print("Day not found.")
            return

        df = df[df["Day"] != day]

        save_data(df)

        print("Record Deleted Successfully.")

    except:
        print("Invalid Input.")

def search_data():
    df = load_data()

    if df.empty:
        print("No data available.")
        return

    try:
        day = int(input("Enter Day to Search: "))

        result = df[df["Day"] == day]

        if result.empty:
            print("Record not found.")
        else:
            print("\nRecord Found")
            print(result.to_string(index=False))

    except:
        print("Invalid Input.")


def statistics():
    df = load_data()

    if df.empty:
        print("No data available.")
        return

    print("\nUsage Statistics")
    print("-" * 30)
    print(f"Average Usage : {df['Electricity_Usage'].mean():.2f}")
    print(f"Maximum Usage : {df['Electricity_Usage'].max():.2f}")
    print(f"Minimum Usage : {df['Electricity_Usage'].min():.2f}")


def predict_usage():
    df = load_data()

    if len(df) < 2:
        print("Not enough data for prediction.")
        return

    X = df[["Day"]]
    y = df["Electricity_Usage"]

    model = LinearRegression()
    model.fit(X, y)

    try:
        future_day = int(input("Enter Future Day: "))

        future = pd.DataFrame({"Day": [future_day]})

        prediction = model.predict(future)

        print(f"\nPredicted Electricity Usage on Day {future_day} : {prediction[0]:.2f} Units")

    except:
        print("Invalid Input.")


def menu():

    while True:

        print("\n" + "=" * 40)
        print("UTILITY USAGE PREDICTION TOOL")
        print("=" * 40)
        print("1. View Records")
        print("2. Add Record")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Search Record")
        print("6. Usage Statistics")
        print("7. Predict Future Usage")
        print("8. Exit")

        try:

            choice = int(input("\nEnter Choice: "))

            if choice == 1:
                view_data()

            elif choice == 2:
                add_data()

            elif choice == 3:
                update_data()

            elif choice == 4:
                delete_data()

            elif choice == 5:
                search_data()

            elif choice == 6:
                statistics()

            elif choice == 7:
                predict_usage()

            elif choice == 8:
                print("\nThank You!")
                break

            else:
                print("Invalid Choice.")

        except:
            print("Please enter a valid number.")


if __name__ == "__main__":
    menu()