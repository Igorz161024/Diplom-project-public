import React, { useEffect, useState } from 'react';
import { getAdminData } from '../api/admin';

const AdminTable = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getAdminData().then(setData);
  }, []);

  return (
    <table>
      <thead>
        <tr><th>Admin Data</th></tr>
      </thead>
      <tbody>
        {data.map((item, idx) => (
          <tr key={idx}><td>{item.username}</td></tr>
        ))}
      </tbody>
    </table>
  );
};

export default AdminTable;
