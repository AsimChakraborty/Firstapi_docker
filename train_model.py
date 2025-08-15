import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Load the dataset
df = pd.read_csv("data/heart.csv")

# Preprocess the data
X = df.drop("target", axis=1)
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "heart_model_random_forest.joblib")
print("Random Forest model trained and saved.")



# Logistic Regression
logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
joblib.dump(logistic_model, "heart_model_logistic.joblib")
print("Logistic Regression model trained and saved.")