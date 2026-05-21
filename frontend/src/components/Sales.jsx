import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Sales() {
  const [sales, setSales] = useState([]);

  useEffect(() => {
    axios.get("/api/sales").then(res => setSales(res.data));
  }, []);

  return (
    <div>
      <h2>Sales (Продажі)</h2>
      <ul>
        {sales.map((s, idx) => (
          <li key={idx}>{s.client} – {s.invoice} – {s.total} грн</li>
        ))}
      </ul>
    </div>
  );
}
