import os
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

FILE_NAME = "Project3.csv"
MODEL_NAME = "fake_news_model.pkl"
HISTORY_FILE = "prediction_history.csv"


def create_sample_data():

    sample_data = {
        "text": [
            "Government launches new education policy for students",
            "Scientists discover water on Mars",
            "Free iPhone for everyone click this link now",
            "Aliens have landed in New York City",
            "New railway line inaugurated by government",
            "Celebrity adopts 100 orphan children",
            "Fake miracle medicine cures every disease instantly",
            "NASA announces successful satellite launch",
            "Breaking: Earth will stop rotating tomorrow",
            "Local hospital opens new cancer treatment center"
        ],

        "label": [
            "REAL",
            "REAL",
            "FAKE",
            "FAKE",
            "REAL",
            "REAL",
            "FAKE",
            "REAL",
            "FAKE",
            "REAL"
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

            return create_sample_data()

        return df

    except Exception:

        return create_sample_data()


def view_dataset():

    df = load_data()

    print("\n========== DATASET ==========\n")

    print(df.to_string(index=False))

    print()


def dataset_summary():

    df = load_data()

    print("\n========== DATASET SUMMARY ==========\n")

    print("Rows :", len(df))
    print("Columns :", len(df.columns))

    print("\nColumn Names")

    for column in df.columns:

        print("-", column)

    print("\nMissing Values")

    print(df.isnull().sum())

    print("\nNews Count")

    print(df["label"].value_counts())


def search_news():

    df = load_data()

    keyword = input("\nEnter Keyword : ").lower()

    result = df[df["text"].str.lower().str.contains(keyword)]

    if result.empty:

        print("\nNo Matching News Found.")

    else:

        print("\nMatching News\n")

        print(result.to_string(index=False))


def train_model():

    df = load_data()

    X = df["text"]

    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    model = Pipeline([

        ("vectorizer", TfidfVectorizer()),

        ("classifier", LogisticRegression())

    ])

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    joblib.dump(model, MODEL_NAME)

    print(f"\nModel Trained Successfully.")
    print(f"Accuracy : {accuracy*100:.2f}%")

    return model

def load_model():

    if os.path.exists(MODEL_NAME):

        return joblib.load(MODEL_NAME)

    print("\nNo trained model found.")
    print("Training a new model...\n")

    return train_model()


def create_history_file():

    if not os.path.exists(HISTORY_FILE):

        history = pd.DataFrame(
            columns=[
                "News",
                "Prediction",
                "Confidence (%)"
            ]
        )

        history.to_csv(HISTORY_FILE, index=False)


def save_prediction(news, prediction, confidence):

    create_history_file()

    history = pd.read_csv(HISTORY_FILE)

    new_record = pd.DataFrame({

        "News": [news],
        "Prediction": [prediction],
        "Confidence (%)": [round(confidence, 2)]

    })

    history = pd.concat([history, new_record], ignore_index=True)

    history.to_csv(HISTORY_FILE, index=False)


def prediction_history():

    create_history_file()

    history = pd.read_csv(HISTORY_FILE)

    if history.empty:

        print("\nNo Prediction History Found.")

    else:

        print("\n========== Prediction History ==========\n")

        print(history.to_string(index=False))


def detect_fake_news():

    model = load_model()

    news = input("\nEnter News Text:\n\n")

    result = model.predict([news])[0]

    probability = model.predict_proba([news])

    confidence = max(probability[0]) * 100

    print("\n" + "=" * 45)
    print("        AI NEWS ANALYSIS REPORT")
    print("=" * 45)

    print(f"Prediction : {result}")
    print(f"Confidence : {confidence:.2f}%")

    if confidence >= 90:

        print("Risk Level : HIGH")

    elif confidence >= 70:

        print("Risk Level : MEDIUM")

    else:

        print("Risk Level : LOW")

    print("=" * 45)

    save_prediction(news, result, confidence)


def model_information():

    model = load_model()

    print("\n========== MODEL INFORMATION ==========\n")

    print("Algorithm      : Logistic Regression")
    print("Vectorizer     : TF-IDF")
    print("Pipeline Ready : Yes")

    if os.path.exists(MODEL_NAME):

        print("Saved Model    : Available")

    else:

        print("Saved Model    : Not Available")

def menu():

    while True:

        print("\n" + "=" * 50)
        print("      AI FAKE NEWS DETECTION SYSTEM")
        print("=" * 50)
        print("1. View Dataset")
        print("2. Dataset Summary")
        print("3. Search News")
        print("4. Train Machine Learning Model")
        print("5. Detect Fake News")
        print("6. Prediction History")
        print("7. Model Information")
        print("8. Exit")

        try:

            choice = int(input("\nEnter Choice : "))

            if choice == 1:

                view_dataset()

            elif choice == 2:

                dataset_summary()

            elif choice == 3:

                search_news()

            elif choice == 4:

                train_model()

            elif choice == 5:

                detect_fake_news()

            elif choice == 6:

                prediction_history()

            elif choice == 7:

                model_information()

            elif choice == 8:

                print("\nThank You!")
                print("Exiting Program...")
                break

            else:

                print("Invalid Choice.")

        except Exception:

            print("Please Enter a Valid Number.")


if __name__ == "__main__":

    create_history_file()

    menu()