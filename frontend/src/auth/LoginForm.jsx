// LoginForm.jsx
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [role, setRole] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    // тут можна додати перевірку логіну/паролю
    if (username && role) {
      localStorage.setItem("role", role);
      navigate("/"); // після логіну перенаправляємо на головну
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
        <label>Role:</label>
        <select value={role} onChange={(e) => setRole(e.target.value)}>
          <option value="">Select role</option>
          <option value="Admin">Admin</option>
          <option value="Buchgalter">Buchgalter</option>
          <option value="HR">HR</option>
          <option value="Legal">Legal</option>
          <option value="Sales">Sales</option>
          <option value="Purchases">Purchases</option>
        </select>
      </div>

      <button type="submit">Login</button>
    </form>
  );
};

export default LoginForm;
