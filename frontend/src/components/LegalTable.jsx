import React, { useEffect, useState } from 'react';
import { getLegalData } from '../api/legal';

const LegalTable = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getLegalData().then(setData);
  }, []);

  return (
    <table>
      <thead>
        <tr><th>Legal</th></tr>
      </thead>
      <tbody>
        {data.map((item, idx) => (
          <tr key={idx}><td>{item.caseName}</td></tr>
        ))}
      </tbody>
    </table>
  );
};

export default LegalTable;
