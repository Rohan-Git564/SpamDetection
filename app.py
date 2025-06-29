from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import sqlite3
import datetime

app = Flask(__name__)
CORS(app)

# Load trained model and vectorizer
with open("spam_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            prediction INTEGER NOT NULL,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "No message provided"}), 400

    vector = vectorizer.transform([message])
    prediction = model.predict(vector)[0]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages (message, prediction, timestamp) VALUES (?, ?, ?)",
        (message, int(prediction), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    )
    conn.commit()
    conn.close()

    return jsonify({"prediction": int(prediction)})

@app.route("/history", methods=["GET"])
def get_history():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT message, prediction, timestamp FROM messages ORDER BY id DESC LIMIT 20")
    rows = cursor.fetchall()
    conn.close()

    history = [
        {"message": row[0], "prediction": "SPAM ❌" if row[1] == 1 else "NOT SPAM ✅", "timestamp": row[2]}
        for row in rows
    ]
    return jsonify(history)

if __name__ == "__main__":
    app.run(debug=True)
