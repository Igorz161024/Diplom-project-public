import React, { useEffect, useState } from "react";
import axios from "axios";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Title,
  Tooltip,
  Legend
} from "chart.js";

// Реєструємо модулі Chart.js
ChartJS.register(
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Title,
  Tooltip,
  Legend
);

export default function FinancePlot() {
  const [chartData, setChartData] = useState({ labels: [], datasets: [] });

  useEffect(() => {
    axios.get("/api/finance/plot")
      .then(res => {
        const data = res.data;
        setChartData({
          labels: data.map(item => item.date),
          datasets: [
            {
              label: "Amount",
              data: data.map(item => item.amount),
              borderColor: "rgba(75,192,192,1)",
              backgroundColor: "rgba(75,192,192,0.2)",
              fill: true,
              tension: 0.3
            }
          ]
        });
      })
      .catch(err => console.error("Error fetching plot:", err));
  }, []);

  return (
    <div style={{ width: "100%", height: "400px" }}>
      <Line data={chartData} />
    </div>
  );
}
