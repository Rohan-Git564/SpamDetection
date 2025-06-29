# 📩 Spam Text Detection Using Machine Learning

This project aims to detect whether a given text message is **spam or not spam** using a trained machine learning model. It demonstrates a real-world application of Natural Language Processing (NLP), Flask API integration, and a clean React frontend for interaction.

---

## 🚀 Project Overview

- 🔍 Uses **TF-IDF vectorization** to convert text into numerical features
- 🧠 Trained with **Multinomial Naive Bayes**, ideal for text classification
- 🔗 Built with a **Flask backend** to serve predictions
- 🎨 Integrated with a **React.js frontend** for a professional UI
- 💾 Stores predictions in a **SQLite database** (optional)

---

## 🛠️ Tech Stack

| Layer      | Technology            |
|------------|------------------------|
| ML Model   | Scikit-learn, Pandas   |
| Backend    | Python Flask           |
| Frontend   | React.js               |
| Database   | SQLite                 |
| Others     | HTML, CSS, JavaScript  |

---

## 📁 Folder Structure

spam-detection/
│
├── backend/
│ ├── app.py # Flask server
│ ├── spam_model.pkl # Trained ML model
│ ├── tfidf_vectorizer.pkl # TF-IDF vectorizer
│ ├── save_model.py # Model training script
│ ├── database.db # SQLite DB (optional)
│ └── requirements.txt # Python dependencies
│
├── frontend/
│ ├── public/
│ ├── src/
│ ├── package.json
│ └── ... # React UI files
│
├── README.md # Project info

yaml
Copy
Edit

---

## 🧪 How to Run the Project

### 🧰 Backend (Flask API)
1. Open terminal:
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
The server will start at http://localhost:5000

🖥️ Frontend (React App)
Open new terminal:

bash
Copy
Edit
cd frontend
npm install
npm start
Visit http://localhost:3000 to use the app

📨 Example
Input:

Congratulations! You've won a free iPhone. Click here to claim.

Output:

Spam

💡 Features
Real-time prediction of spam messages

Clean and responsive user interface

Accurate classification with minimal false positives

Easy-to-understand codebase

Modular and scalable design

📦 Installation Requirements
Python packages:

bash
Copy
Edit
Flask
scikit-learn
pandas
joblib
Install using:

bash
Copy
Edit
pip install -r requirements.txt
React dependencies are in frontend/package.json.

👨‍💻 Developed By
Rohan Biradar
Computer Science Student | Software Developer Enthusiast
