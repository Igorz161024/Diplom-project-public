// ProtectedRoute.jsx
import React from "react";
import { Navigate } from "react-router-dom";
import { hasAccess } from "./roles";

const ProtectedRoute = ({ path, children }) => {
  const storedRole = localStorage.getItem("role");

  // якщо ролі немає — редірект на логін
  if (!storedRole) {
    return <Navigate to="/login" replace />;
  }

  // якщо роль не має доступу до цього маршруту — редірект на логін
  if (!hasAccess(storedRole, path)) {
    return <Navigate to="/login" replace />;
  }

  // якщо все ок — показуємо компонент
  return children;
};

export default ProtectedRoute;
