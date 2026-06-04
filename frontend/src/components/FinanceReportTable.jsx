import React, { useEffect, useState } from "react";
import { DataGrid } from "@mui/x-data-grid";
import axios from "axios";

const FinanceReportTable = () => {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    axios.get("/api/finance/report")
      .then(response => {
        setRows(response.data);
      })
      .catch(error => {
        console.error("Error fetching report:", error);
      });
  }, []);

  const columns = [
    { field: "date", headerName: "Date", width: 150 },
    { field: "operation", headerName: "Operation", width: 200 },
    { field: "status", headerName: "Status", width: 150 },
    { field: "amount", headerName: "Amount", width: 150, type: "number" }
  ];

  return (
    <div style={{ height: 400, width: "100%" }}>
      <DataGrid
        rows={rows}
        columns={columns}
        getRowId={(row) => row.id}
        pageSize={5}
        rowsPerPageOptions={[5, 10, 20]}
      />
    </div>
  );
};

export default FinanceReportTable;
