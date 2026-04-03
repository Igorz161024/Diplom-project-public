import { fetchJournalData } from "../services/api";

import React, { useState, useEffect } from "react";
import "./journal.css";

const JournalTable = () => {
  const [theme, setTheme] = useState("dark");
  const [data, setData] = useState([]);

useEffect(() => {
  fetchJournalData().then((res) => setData(res));
}, []);

   return (
    <div className={`journal-table ${theme}`}>
      <button onClick={() => setTheme(theme === "dark" ? "light" : "dark")}>
        Перемкнути тему
      </button>
      <table>
        <thead>
          <tr>
            <th>Дата</th>
            <th>Документ</th>
            <th>Номер</th>
            <th>Контрагент</th>
            <th>Сума</th>
            <th>Статус</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              <td>{row.date}</td>
              <td>{row.doc}</td>
              <td>{row.num}</td>
              <td>{row.client}</td>
              <td>{row.sum}</td>
              <td>{row.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default JournalTable;
