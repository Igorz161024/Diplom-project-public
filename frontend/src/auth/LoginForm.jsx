// LoginForm.jsx
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const LoginForm = ({ onLogin }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:5000/token", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
      });

      const data = await response.json();

      if (data.access_token) {
        localStorage.setItem("token", data.access_token);
        localStorage.setItem("role", data.role);
        localStorage.setItem("username", username);

        // оновлюємо стан ролі у App.jsx
        onLogin(data.role);

        // після логіну перенаправляємо на головну
        navigate("/");
      } else {
        alert("Login failed");
      }
    } catch (err) {
      alert("Error during login");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Username:</label>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>

      <div>
        <label>Password:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>

      <button type="submit">Login</button>
    </form>
  );
};

export default LoginForm;
