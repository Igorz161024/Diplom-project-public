import React, { useEffect, useState } from 'react';
import { getPurchasesData } from '../api/purchases';

const PurchasesTable = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getPurchasesData().then(setData);
  }, []);

  return (
    <table>
      <thead>
        <tr><th>Purchases</th></tr>
      </thead>
      <tbody>
        {data.map((item, idx) => (
          <tr key={idx}><td>{item.purchaseName}</td></tr>
        ))}
      </tbody>
    </table>
  );
};

export default PurchasesTable;
