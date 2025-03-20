import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [formData, setFormData] = useState({
    budget: "",
    employees_impacted: "",
    duration_months: "",
    training_hours: "",
    communication_score: "",
    leadership_alignment: "",
    _avg_salary: "",
    _productivity_gain: "",
  });

  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const requestData = {
      input_data: {
        columns: Object.keys(formData),
        data: [
          [
            parseFloat(formData.budget),
            parseInt(formData.employees_impacted),
            parseInt(formData.duration_months),
            parseFloat(formData.training_hours),
            parseFloat(formData.communication_score),
            parseInt(formData.leadership_alignment),
            parseFloat(formData._avg_salary),
            parseFloat(formData._productivity_gain),
          ],
        ],
      },
    };

    try {
      const res = await axios.post("http://localhost:5000/inference", requestData);
      setResults(res.data);
    } catch (err) {
      setError(`Error: ${err.response ? err.response.data.detail : err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "800px", margin: "auto" }}>
      <h2>ROI Calculator for Transformation Success</h2>
      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <div key={key} style={{ marginBottom: "10px" }}>
            <label>{key.replace(/_/g, " ")}: </label>
            <input
              type="text"
              name={key}
              value={formData[key]}
              onChange={handleChange}
              required
            />
          </div>
        ))}
        <button type="submit" disabled={loading}>
          {loading ? "Processing..." : "Submit"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {results && (
        <div style={{ marginTop: "20px" }}>
          <h3>Results:</h3>
          <pre>{JSON.stringify(results, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default App;
