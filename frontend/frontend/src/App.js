import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;
    setLoading(true);
    setResponse('');
    try {
      const res = await axios.post('http://localhost:8000/query', { query });
      setResponse(res.data.answer);
    } catch (error) {
      console.error(error);
      setResponse('⚠️ Error: Could not get a response from the backend.');
    } finally {
      setLoading(false);
      setQuery('');
    }
  };

  return (
    <div className="app-container">
      <h1 className="app-title">Chat AI</h1>
      <div className="chat-container">
        <div className="response-area">
          {loading ? (
            <div className="loading">Thinking<span className="dots">...</span></div>
          ) : response ? (
            <div className="response-text">{response}</div>
          ) : (
            <div className="placeholder">Ask me anything ✨</div>
          )}
        </div>
        <form onSubmit={handleSubmit} className="input-form">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Type your question..."
            className="input-box"
          />
          <button type="submit" className="send-button">Send</button>
        </form>
      </div>
    </div>
  );
}

export default App;
