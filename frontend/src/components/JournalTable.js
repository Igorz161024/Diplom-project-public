import React, { useState, useEffect } from "react";
import { DataGrid } from "@mui/x-data-grid";
import "../styles/journal.css";

const JournalTable = () => {
  const [rows, setRows] = useState([]);
  const [theme, setTheme] = useState("light");

  useEffect(() => {
    setRows([
      { id: 1, date: "2026-04-10", operation: "Створення запису", status: "success" },
      { id: 2, date: "2026-04-11", operation: "Оновлення даних", status: "warning" },
      { id: 3, date: "2026-04-12", operation: "Видалення запису", status: "error" },
    ]);
  }, []);

  const columns = [
    { field: "date", headerName: "Дата", width: 150 },
    { field: "operation", headerName: "Операція", width: 250 },
    { field: "status", headerName: "Статус", width: 150 },
  ];

  return (
    <div>
      <button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
        Перемкнути тему
      </button>
      <table className={`journal-table ${theme}`}>
        <caption>Журнал операцій</caption>
        <thead>
          <tr>
            <th>Дата</th>
            <th>Операція</th>
            <th>Статус</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <tr key={row.id}>
              <td>{row.date}</td>
              <td>{row.operation}</td>
              <td className={row.status}>{row.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div style={{ height: 400, width: "100%", marginTop: "20px" }}>
        <DataGrid rows={rows} columns={columns} pageSize={5} />
      </div>
    </div>
  );
};

export default JournalTable;
