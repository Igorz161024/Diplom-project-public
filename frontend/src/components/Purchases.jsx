import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Purchases() {
  const [contracts, setContracts] = useState([]);

  useEffect(() => {
    axios.get("/api/purchases").then(res => setContracts(res.data));
  }, []);

  return (
    <div>
      <h2>Purchases (Закупівлі)</h2>
      <ul>
        {contracts.map((c, idx) => (
          <li key={idx}>{c.supplier} – {c.country} – {c.amount} USD</li>
        ))}
      </ul>
    </div>
  );
}
