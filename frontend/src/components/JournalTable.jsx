import React, { useEffect, useState } from "react";
import {
  Table, TableBody, TableCell, TableContainer,
  TableHead, TableRow, Paper, Switch
} from "@mui/material";

export default function JournalTable() {
  const [rows, setRows] = useState([]);
  const [darkMode, setDarkMode] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/api/journal")
      .then(res => res.json())
      .then(data => setRows(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: "20px", backgroundColor: darkMode ? "#121212" : "#fff" }}>
      <Switch
        checked={darkMode}
        onChange={() => setDarkMode(!darkMode)}
        color="primary"
      />
      <TableContainer component={Paper} style={{ backgroundColor: darkMode ? "#1e1e1e" : "#fafafa" }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell style={{ color: darkMode ? "#fff" : "#000" }}>Date</TableCell>
              <TableCell style={{ color: darkMode ? "#fff" : "#000" }}>Operation</TableCell>
              <TableCell style={{ color: darkMode ? "#fff" : "#000" }}>Status</TableCell>
              <TableCell style={{ color: darkMode ? "#fff" : "#000" }}>Amount</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row, idx) => (
              <TableRow key={idx}>
                <TableCell style={{ color: darkMode ? "#fff" : "#000" }}>{row.date}</TableCell>
                <TableCell style={{ color: darkMode ? "#fff" : "#000" }}>{row.operation}</TableCell>
                <TableCell style={{ color: darkMode ? "#fff" : "#000" }}>{row.status}</TableCell>
                <TableCell style={{ color: darkMode ? "#fff" : "#000" }}>{row.amount}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}
