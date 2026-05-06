import React from "react";
import { Link } from "react-router-dom";

export default function NavBar() {
  return (
    <nav style={{ marginBottom: "20px" }}>
      <Link to="/">Головна</Link> |{" "}
      <Link to="/journal">Журнал</Link> |{" "}
      <Link to="/finance">Finance</Link> |{" "}
      <Link to="/hr">HR</Link> |{" "}
      <Link to="/admin">Admin</Link> |{" "}
      <Link to="/products">Products</Link> |{" "}
      <Link to="/pkash">PKash</Link> |{" "}
      <Link to="/inventory">Inventory</Link> |{" "}
      <Link to="/purchases">Purchases</Link> |{" "}
      <Link to="/sales">Sales</Link> |{" "}
      <Link to="/legal">Legal</Link>
    </nav>
  );
}
