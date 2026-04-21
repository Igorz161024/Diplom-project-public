import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Inventory() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get("/api/inventory").then(res => setItems(res.data));
  }, []);

  return (
    <div>
      <h2>Inventory (Склад)</h2>
      <table>
        <thead>
          <tr><th>Товар</th><th>Кількість</th><th>Партія</th></tr>
        </thead>
        <tbody>
          {items.map((i, idx) => (
            <tr key={idx}><td>{i.name}</td><td>{i.qty}</td><td>{i.batch}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
