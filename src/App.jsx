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
            <ProtectedRoute requiredRole="Finance" currentRole={role}>
              <Finance />
            </ProtectedRoute>
          }
        />
        <Route
          path="/hr"
          element={
            <ProtectedRoute requiredRole="HR" currentRole={role}>
              <HR />
            </ProtectedRoute>
          }
        />
        <Route
          path="/admin"
          element={
            <ProtectedRoute requiredRole="Admin" currentRole={role}>
              <Admin />
            </ProtectedRoute>
          }
        />
        <Route
          path="/products"
          element={
            <ProtectedRoute requiredRole="Products" currentRole={role}>
              <Products />
            </ProtectedRoute>
          }
        />
        <Route
          path="/pkash"
          element={
            <ProtectedRoute requiredRole="PKash" currentRole={role}>
              <PKash />
            </ProtectedRoute>
          }
        />
        <Route
          path="/inventory"
          element={
            <ProtectedRoute requiredRole="Inventory" currentRole={role}>
              <Inventory />
            </ProtectedRoute>
          }
        />
        <Route
          path="/purchases"
          element={
            <ProtectedRoute requiredRole="Purchases" currentRole={role}>
              <Purchases />
            </ProtectedRoute>
          }
        />
        <Route
          path="/sales"
          element={
            <ProtectedRoute requiredRole="Sales" currentRole={role}>
              <Sales />
            </ProtectedRoute>
          }
        />
        <Route
          path="/legal"
          element={
            <ProtectedRoute requiredRole="Legal" currentRole={role}>
              <Legal />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
}
