import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import AccountantView from "./AccountantView";
import HRView from "./HRView";
import DirectorView from "./DirectorView";

function App() {
  return (
    <Router>
      <div className="App">
        <h1>Дипломный проект по ERP-системе</h1>
        <nav>
          <Link to="/accountant">Бухгалтер</Link> |{" "}
          <Link to="/hr">HR</Link> |{" "}
          <Link to="/director">Директор</Link>
        </nav>
        <Routes>
          <Route path="/accountant" element={<AccountantView />} />
          <Route path="/hr" element={<HRView />} />
          <Route path="/director" element={<DirectorView />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;