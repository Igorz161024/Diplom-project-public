import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { getFinanceData } from '../api/finance';

const FinanceTable = () => {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    getFinanceData().then((data) => {
      // додаємо унікальний id для кожного рядка
      const withId = data.map((item, idx) => ({ id: idx + 1, ...item }));
      setRows(withId);
    });
  }, []);

  const columns = [
    { field: 'id', headerName: 'ID', width: 90 },
    { field: 'amount', headerName: 'Amount', width: 150 },
    { field: 'description', headerName: 'Description', width: 250 },
    { field: 'date', headerName: 'Date', width: 180 },
  ];

  return (
    <div style={{ height: 400, width: '100%' }}>
      <h2>Finance (Фінанси)</h2>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5, 10]}
        disableSelectionOnClick
      />
    </div>
  );
};

export default FinanceTable;

