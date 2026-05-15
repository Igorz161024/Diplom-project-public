import './App.css';
import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// MUI імпорти
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Button from '@mui/material/Button';
import SaveIcon from '@mui/icons-material/Save';

// Компоненти
import NavBar from "./components/NavBar";
import JournalTable from "./components/JournalTable";

// Авторизація
import LoginForm from "./auth/LoginForm";
import ProtectedRoute from "./auth/ProtectedRoute";

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
  const [darkMode, setDarkMode] = useState(true);

  useEffect(() => {
    if (role) localStorage.setItem("role", role);
  }, [role]);

  const theme = createTheme({
    palette: { mode: darkMode ? 'dark' : 'light' },
  });

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <div className="App">
          {/* Навігаційне меню */}
          <NavBar />

          <Routes>
            {/* Головна з логіном */}
            <Route path="/" element={
              !role 
                ? <LoginForm onLogin={(r) => setRole(r)} /> 
                : <h1>ERP Головна</h1>
            } />

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

          {/* Кнопки */}
          <div style={{ marginTop: "20px" }}>
            <Button 
              variant="contained" 
              color="primary" 
              startIcon={<SaveIcon />}
              onClick={() => alert("Збережено!")}
            >
              Зберегти
            </Button>

            <Button 
              variant="outlined" 
              style={{ marginLeft: "10px" }}
              onClick={() => setDarkMode(!darkMode)}
            >
              Перемкнути тему
            </Button>
          </div>
        </div>
      </Router>
    </ThemeProvider>
  );
}
