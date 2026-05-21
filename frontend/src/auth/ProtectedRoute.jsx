// ProtectedRoute.jsx
import React from "react";
import { Navigate } from "react-router-dom";

const ProtectedRoute = ({ children, requiredRole, currentRole }) => {
  // якщо користувач не залогінений → редирект на головну
  if (!currentRole) {
    return <Navigate to="/" replace />;
  }

  // якщо роль не співпадає → редирект на головну
  if (requiredRole && currentRole !== requiredRole) {
    return <Navigate to="/" replace />;
  }

  // якщо все ок → показуємо компонент
  return children;
};

export default ProtectedRoute;
