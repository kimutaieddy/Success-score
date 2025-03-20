import React from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  RadialBarChart,
  RadialBar,
} from "recharts";

// Custom Gauge Component with Needle (Risk Gauge)
const RiskGauge = ({ value = 50 }) => {
  // Chart dimensions
  const width = 400;
  const height = 250; // enough vertical space for the half-circle + needle

  // Define the center and radii
  const cx = 200;
  const cy = 200;
  const innerRadius = 90;
  const outerRadius = 140;

  // Define the three gauge segments (each roughly 33% of the half-circle)
  const segments = [
    { name: "Risk Appetite", value: 33.3, fill: "#8BC34A" },
    { name: "Risk Tolerance", value: 33.3, fill: "#FFC107" },
    { name: "Unacceptable Risk", value: 33.4, fill: "#F44336" },
  ];

  // Clamp the needle value between 0 and 100
  const needleValue = Math.max(0, Math.min(value, 100));

  // Convert needleValue to an angle in degrees:
  //   0% → 180° (far left)
  //   100% → 0° (far right)
  const angle = 180 - (needleValue / 100) * 180; // 180° range
  const rad = (Math.PI * angle) / 180; // convert to radians

  // Compute the needle endpoint (x2, y2) using the outerRadius
  const x2 = cx + outerRadius * Math.cos(rad);
  const y2 = cy + outerRadius * Math.sin(rad);

  return (
    <div style={{ textAlign: "center" }}>
      <h3>Risk Gauge</h3>
      {/* Use an SVG to combine the Recharts radial chart with the custom needle */}
      <svg width={width} height={height}>
        {/* Translate the chart upward so the half-circle fits */}
        <g transform="translate(0, -50)">
          <RadialBarChart
            cx={cx}
            cy={cy}
            innerRadius={innerRadius}
            outerRadius={outerRadius}
            startAngle={180}
            endAngle={0}
            barSize={10}
            width={width}
            height={400}
            data={segments}
          >
            {/* Draw the colored arcs */}
            <RadialBar minAngle={1} clockWise dataKey="value" />
            <Legend
              iconSize={10}
              layout="horizontal"
              verticalAlign="top"
              align="center"
              wrapperStyle={{ marginTop: 20 }}
            />
          </RadialBarChart>
        </g>
        {/* Draw the needle (shifted upward by 50 as above) */}
        <line
          x1={cx}
          y1={cy - 50}
          x2={x2}
          y2={y2 - 50}
          stroke="black"
          strokeWidth={4}
          strokeLinecap="round"
        />
        {/* Center pivot circle */}
        <circle cx={cx} cy={cy - 50} r={6} fill="black" />
        {/* Display the numeric value */}
        <text x={cx} y={cy + 30 - 50} textAnchor="middle" fontSize={16}>
          {needleValue}%
        </text>
      </svg>
    </div>
  );
};

// Main ROIChart Component
// This component receives ROI data from the backend and renders multiple charts.
const ROIChart = ({ data }) => {
  if (!data) return <p>Loading...</p>;

  // Transform the API response into a format for the BarChart.
  const barChartData = Object.entries(data).map(([key, value]) => ({
    name: key.replace(/_/g, " "),
    value: value,
  }));

  // Pie Chart for Success Probability.
  // (Assumes the backend returns a field called 'success_probability'; if not, it defaults to 50.)
  const successProbability = [
    { name: "Success", value: data.success_probability || 50 },
    { name: "Failure", value: 100 - (data.success_probability || 50) },
  ];
  const pieColors = ["#0088FE", "#FF8042"];

  // Risk Factors (Mocked for demonstration; replace with real data if available.)
  const riskData = [
    { risk: "Cost Overruns", level: Math.random() * 100 },
    { risk: "Low Adoption", level: Math.random() * 100 },
    { risk: "Technical Challenges", level: Math.random() * 100 },
    { risk: "Market Uncertainty", level: Math.random() * 100 },
  ];

  return (
    <div style={{ display: "grid", gap: "20px", gridTemplateColumns: "1fr 1fr" }}>
      {/* 1. ROI Breakdown Bar Chart */}
      <div>
        <h3>ROI Breakdown</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={barChartData}>
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="value" fill="#82ca9d" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 2. Custom Risk Gauge (with Needle) */}
      <div>
        <RiskGauge value={data.roi || 0} />
      </div>

      {/* 3. Success Probability Pie Chart */}
      <div>
        <h3>Success Probability</h3>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie data={successProbability} dataKey="value" outerRadius={100}>
              {successProbability.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={pieColors[index]} />
              ))}
            </Pie>
            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>

      {/* 4. Risk Factors (Heat Highlight) */}
      <div>
        <h3>Risk Factors</h3>
        <ul>
          {riskData.map((risk, index) => (
            <li
              key={index}
              style={{
                background: `rgba(255,0,0,${risk.level / 100})`,
                padding: "5px",
                marginBottom: "5px",
                color: "#fff",
              }}
            >
              {risk.risk}: {Math.round(risk.level)}%
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default ROIChart;

