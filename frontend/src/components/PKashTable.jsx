import React, { useEffect, useState } from 'react';
import { getPKashData } from '../api/pkash';

const PKashTable = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getPKashData().then(setData);
  }, []);

  return (
    <table>
      <thead>
        <tr><th>PKash</th></tr>
      </thead>
      <tbody>
        {data.map((item, idx) => (
          <tr key={idx}><td>{item.transaction}</td></tr>
        ))}
      </tbody>
    </table>
  );
};

export default PKashTable;
