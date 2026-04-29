import React, { useEffect, useState } from 'react';
import { getInventoryData } from '../api/inventory';

const InventoryTable = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getInventoryData().then(setData);
  }, []);

  return (
    <table>
      <thead>
        <tr><th>Inventory</th></tr>
      </thead>
      <tbody>
        {data.map((item, idx) => (
          <tr key={idx}><td>{item.itemName}</td></tr>
        ))}
      </tbody>
    </table>
  );
};

export default InventoryTable;
