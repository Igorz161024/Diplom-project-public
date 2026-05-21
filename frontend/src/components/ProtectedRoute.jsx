import React from "react";
import { Navigate } from "react-router-dom";

export default function ProtectedRoute({ children, role }) {
  const tokenRole = localStorage.getItem("role");

  // якщо роль не співпадає — редірект на логін
  if (tokenRole !== role) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
