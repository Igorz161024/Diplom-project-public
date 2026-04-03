import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import JournalTable from "./components/JournalTable";

const AccountantView = () => <h2>Accountant View</h2>;
const HRView = () => <h2>HR View</h2>;
const DirectorView = () => <h2>Director View</h2>;

function App() {
  return (
    <Router>
      <div className="App">
        <h1>Дипломный проект по ERP-системе</h1>
        <nav>
          <Link to="/">Головна</Link> |{" "}
          <Link to="/accountant">Бухгалтер</Link> |{" "}
          <Link to="/hr">HR</Link> |{" "}
          <Link to="/director">Директор</Link> |{" "}
          <Link to="/journal">Журнал операцій</Link>
        </nav>
        <Routes>
          <Route path="/" element={<JournalTable />} />
          <Route path="/accountant" element={<AccountantView />} />
          <Route path="/hr" element={<HRView />} />
          <Route path="/director" element={<DirectorView />} />
          <Route path="/journal" element={<JournalTable />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
