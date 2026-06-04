import React from "react";
import FinanceReportTable from "./FinanceReportTable";
import FinancePlot from "./FinancePlot";

export default function Finance() {
  return (
    <div style={{ padding: "20px" }}>
      <h2>Finance (Фінанси)</h2>
      <p>Модуль фінансів ERP: звіти та графіки.</p>

      {/* Таблиця з /report */}
      <section style={{ marginBottom: "40px" }}>
        <h3>Звіт</h3>
        <FinanceReportTable />
      </section>

      {/* Графік з /plot */}
      <section>
        <h3>Графік</h3>
        <FinancePlot />
      </section>
    </div>
  );
}

