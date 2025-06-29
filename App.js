import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [prediction, setPrediction] = useState("");
  const [history, setHistory] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });

      const data = await response.json();
      setPrediction(data.prediction === 1 ? "SPAM ❌" : "NOT SPAM ✅");
      setMessage("");
      fetchHistory();
    } catch (error) {
      console.error("Error:", error);
      setPrediction("Something went wrong. Please try again.");
    }
  };

  const fetchHistory = async () => {
    try {
      const res = await fetch("http://127.0.0.1:5000/history");
      const data = await res.json();
      setHistory(data);
    } catch (err) {
      console.error("Failed to fetch history", err);
    }
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  return (
    <div className="App">
      <h1>📩 Spam Message Detector</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message here..."
          required
        ></textarea>
        <br />
        <button type="submit">Check</button>
      </form>

      {prediction && (
        <div className={`result ${prediction.includes("SPAM") ? "spam" : "not-spam"}`}>
          <strong>Result:</strong> {prediction}
        </div>
      )}

      <h2>📜 Message History</h2>
      <ul className="history">
        {history.map((item, index) => (
          <li key={index} className={item.prediction.includes("SPAM") ? "spam" : "not-spam"}>
            <span>{item.message}</span>
            <strong>{item.prediction}</strong>
            <em>{new Date(item.timestamp).toLocaleString()}</em>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
