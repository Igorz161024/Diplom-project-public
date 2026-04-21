import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginForm from "./components/LoginForm";
import Finance from "./components/Finance";
import HR from "./components/HR";
import Admin from "./components/Admin";
import Products from "./components/Products";
import PKash from "./components/PKash";
import Inventory from "./components/Inventory";
import Purchases from "./components/Purchases";
import Sales from "./components/Sales";
import Legal from "./components/Legal";
import ProtectedRoute from "./components/ProtectedRoute";

export default function App() {
  const [role, setRole] = useState(localStorage.getItem("role"));

  return (
    <Router>
      <Routes>
        {/* маршрут для логіну */}
        <Route path="/login" element={<LoginForm onLogin={(r) => setRole(r)} />} />

        {/* модулі ERP з перевіркою ролей */}
        <Route
          path="/finance"
          element={
            <ProtectedRoute role="Finance">
              <Finance />
            </ProtectedRoute>
          }
        />
        <Route
          path="/hr"
          element={
            <ProtectedRoute role="HR">
              <HR />
            </ProtectedRoute>
          }
        />
        <Route
          path="/admin"
          element={
            <ProtectedRoute role="Admin">
              <Admin />
            </ProtectedRoute>
          }
        />
        <Route
          path="/products"
          element={
            <ProtectedRoute role="Products">
              <Products />
            </ProtectedRoute>
          }
        />
        <Route
          path="/pkash"
          element={
            <ProtectedRoute role="PKash">
              <PKash />
            </ProtectedRoute>
          }
        />
        <Route
          path="/inventory"
          element={
            <ProtectedRoute role="Inventory">
              <Inventory />
            </ProtectedRoute>
          }
        />
        <Route
          path="/purchases"
          element={
            <ProtectedRoute role="Purchases">
              <Purchases />
            </ProtectedRoute>
          }
        />
        <Route
          path="/sales"
          element={
            <ProtectedRoute role="Sales">
              <Sales />
            </ProtectedRoute>
          }
        />
        <Route
          path="/legal"
          element={
            <ProtectedRoute role="Legal">
              <Legal />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
}


