import React, { useEffect, useState } from 'react';
import { getHRData } from '../api/hr';

const HRTable = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getHRData().then(setData);
  }, []);

  return (
    <table>
      <thead>
        <tr><th>HR Data</th></tr>
      </thead>
      <tbody>
        {data.map((item, idx) => (
          <tr key={idx}><td>{item.name}</td></tr>
        ))}
      </tbody>
    </table>
  );
};

export default HRTable;
