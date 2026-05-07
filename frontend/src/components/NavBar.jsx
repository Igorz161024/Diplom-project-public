// NavBar.jsx
import React from "react";
import { Link } from "react-router-dom";
import { rolesConfig } from "../auth/roles";

export default function NavBar() {
  const role = localStorage.getItem("role");

  if (!role) {
    return null; // якщо користувач не залогінений — меню не показуємо
  }

  const allowedPaths = rolesConfig[role] || [];

  return (
    <nav style={{ marginBottom: "20px" }}>
      {allowedPaths.includes("/") && <Link to="/">Головна</Link>} |{" "}
      {allowedPaths.includes("/journal") && <Link to="/journal">Журнал</Link>} |{" "}
      {allowedPaths.includes("/finance") && <Link to="/finance">Finance</Link>} |{" "}
      {allowedPaths.includes("/hr") && <Link to="/hr">HR</Link>} |{" "}
      {allowedPaths.includes("/admin") && <Link to="/admin">Admin</Link>} |{" "}
      {allowedPaths.includes("/products") && <Link to="/products">Products</Link>} |{" "}
      {allowedPaths.includes("/pkash") && <Link to="/pkash">PKash</Link>} |{" "}
      {allowedPaths.includes("/inventory") && <Link to="/inventory">Inventory</Link>} |{" "}
      {allowedPaths.includes("/purchases") && <Link to="/purchases">Purchases</Link>} |{" "}
      {allowedPaths.includes("/sales") && <Link to="/sales">Sales</Link>} |{" "}
      {allowedPaths.includes("/legal") && <Link to="/legal">Legal</Link>}
    </nav>
  );
}

