import './App.css';
import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

// MUI імпорти
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Button from '@mui/material/Button';
import SaveIcon from '@mui/icons-material/Save';

// Компоненти
import LoginForm from "./components/LoginForm";
import ProtectedRoute from "./components/ProtectedRoute";
import JournalTable from "./components/JournalTable";

// ERP модулі
import Finance from "./components/Finance";
import HR from "./components/HR";
import Admin from "./components/Admin";
import Products from "./components/Products";
import PKash from "./components/PKash";
import Inventory from "./components/Inventory";
import Purchases from "./components/Purchases";
import Sales from "./components/Sales";
import Legal from "./components/Legal";

export default function App() {
  const [role, setRole] = useState(localStorage.getItem("role"));

  const darkTheme = createTheme({
    palette: { mode: 'dark' },
  });

  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Router>
        <div className="App">
          {/* Навігаційне меню */}
          <nav>
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

          <Routes>
            {/* Головна */}
            <Route path="/" element={<h1>ERP Головна</h1>} />

            {/* Логін */}
            <Route path="/login" element={<LoginForm onLogin={(r) => setRole(r)} />} />

            {/* Журнал */}
            <Route path="/journal" element={<JournalTable />} />

            {/* ERP модулі з перевіркою ролей */}
            <Route path="/finance" element={
              <ProtectedRoute requiredRole="Finance" currentRole={role}>
                <Finance />
              </ProtectedRoute>
            }/>
            <Route path="/hr" element={
              <ProtectedRoute requiredRole="HR" currentRole={role}>
                <HR />
              </ProtectedRoute>
            }/>
            <Route path="/admin" element={
              <ProtectedRoute requiredRole="Admin" currentRole={role}>
                <Admin />
              </ProtectedRoute>
            }/>
            <Route path="/products" element={
              <ProtectedRoute requiredRole="Products" currentRole={role}>
                <Products />
              </ProtectedRoute>
            }/>
            <Route path="/pkash" element={
              <ProtectedRoute requiredRole="PKash" currentRole={role}>
                <PKash />
              </ProtectedRoute>
            }/>
            <Route path="/inventory" element={
              <ProtectedRoute requiredRole="Inventory" currentRole={role}>
                <Inventory />
              </ProtectedRoute>
            }/>
            <Route path="/purchases" element={
              <ProtectedRoute requiredRole="Purchases" currentRole={role}>
                <Purchases />
              </ProtectedRoute>
            }/>
            <Route path="/sales" element={
              <ProtectedRoute requiredRole="Sales" currentRole={role}>
                <Sales />
              </ProtectedRoute>
            }/>
            <Route path="/legal" element={
              <ProtectedRoute requiredRole="Legal" currentRole={role}>
                <Legal />
              </ProtectedRoute>
            }/>
          </Routes>

          {/* Кнопка збереження */}
          <div style={{ marginTop: "20px" }}>
            <Button variant="contained" color="primary" startIcon={<SaveIcon />}>
              Зберегти
            </Button>
          </div>
        </div>
      </Router>
    </ThemeProvider>
  );
}
