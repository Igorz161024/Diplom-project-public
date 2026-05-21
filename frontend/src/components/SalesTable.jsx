import React, { useEffect, useState } from 'react';
import { getSalesData } from '../api/sales';

const SalesTable = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getSalesData().then(setData);
  }, []);

  return (
    <table>
      <thead>
        <tr><th>Sales</th></tr>
      </thead>
      <tbody>
        {data.map((item, idx) => (
          <tr key={idx}><td>{item.saleName}</td></tr>
        ))}
      </tbody>
    </table>
  );
};

export default SalesTable;
