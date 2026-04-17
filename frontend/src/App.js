import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import JournalTable from "./components/JournalTable";

// MUI імпорти
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Button from '@mui/material/Button';
import SaveIcon from '@mui/icons-material/Save';

function App() {
  // створюємо темну тему
  const darkTheme = createTheme({
    palette: {
      mode: 'dark',
    },
  });

  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Router>
        <div className="App">
          <nav>
            <Link to="/">Головна</Link> |{" "}
            <Link to="/journal">Журнал</Link>
          </nav>

          <Routes>
            <Route path="/" element={<h1>ERP Головна</h1>} />
            <Route path="/journal" element={<JournalTable />} />
          </Routes>

          <div style={{ marginTop: "20px" }}>
            <Button
              variant="contained"
              color="primary"
              startIcon={<SaveIcon />}
            >
              Зберегти
            </Button>
          </div>
        </div>
      </Router>
    </ThemeProvider>
  );
}

export default App;

