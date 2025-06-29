import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier

# Step 1: Load your dataset
df = pd.read_csv("spam_data.csv")

# Step 2: Features and labels
X = df["message"]
y = df["label"]

# Step 3: Vectorize text
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Step 4: Train a model
model = DecisionTreeClassifier()
model.fit(X_vectorized, y)

# Step 5: Save model and vectorizer
with open("spam_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved successfully.")
