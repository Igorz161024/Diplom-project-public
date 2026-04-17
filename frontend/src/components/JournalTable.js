import React, { useState, useEffect } from "react";
import { DataGrid } from "@mui/x-data-grid";
import "../styles/journal.css";

const JournalTable = () => {
  const [rows, setRows] = useState([]);
  const [theme, setTheme] = useState("light");

  useEffect(() => {
    fetch("http://localhost:8000/api/journal")
      .then(res => res.json())
      .then(data => {
        const rowsWithId = data.map((row, index) => ({
          id: index + 1,
          ...row
        }));
        setRows(rowsWithId);
        console.log("Отримані рядки:", rowsWithId);
      })
      .catch(err => console.error("Помилка завантаження журналу:", err));
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

      {/* HTML-таблиця */}
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

      {/* DataGrid */}
      <div style={{ height: 400, width: "100%", marginTop: "20px" }}>
        <DataGrid
          rows={rows}
          columns={columns}
          initialState={{
            pagination: { paginationModel: { pageSize: 5 } },
          }}
          pageSizeOptions={[5]}
        />
      </div>
    </div>
  );
};

export default JournalTable;
