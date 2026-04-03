import React from "react";

const JournalTable = () => {
  const data = [
    { id: 1, operation: "Оплата постачальнику", amount: 5000 },
    { id: 2, operation: "Продаж товару", amount: 12000 },
    { id: 3, operation: "Зарплата співробітникам", amount: 8000 },
  ];

  return (
    <table border="1" style={{ marginTop: "20px", width: "100%" }}>
      <thead>
        <tr>
          <th>ID</th>
          <th>Операція</th>
          <th>Сума</th>
        </tr>
      </thead>
      <tbody>
        {data.map((row) => (
          <tr key={row.id}>
            <td>{row.id}</td>
            <td>{row.operation}</td>
            <td>{row.amount}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default JournalTable;
