import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Legal() {
  const [docs, setDocs] = useState([]);

  useEffect(() => {
    axios.get("/api/legal").then(res => setDocs(res.data));
  }, []);

  return (
    <div>
      <h2>Legal (Юрист)</h2>
      <ul>
        {docs.map((d, idx) => (
          <li key={idx}>{d.contract} – {d.partner} – {d.status}</li>
        ))}
      </ul>
    </div>
  );
}
