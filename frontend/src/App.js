import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState({ satellites: [], debris_cloud: [] });

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/visualization/snapshot")
      .then(res => res.json())
      .then(res => setData(res));
  }, []);

  return (
    <div style={{ textAlign: "center" }}>
      <h1>🚀 Orbital Insight Dashboard</h1>

      <div style={{
        width: "800px",
        height: "400px",
        border: "2px solid black",
        margin: "auto",
        position: "relative"
      }}>

        {/* Satellites */}
        {data.satellites.map((sat, i) => (
          <div key={i} style={{
            position: "absolute",
            left: `${sat.lat * 5}px`,
            top: `${sat.lon * 2}px`,
            width: "10px",
            height: "10px",
            backgroundColor: "blue",
            borderRadius: "50%"
          }}></div>
        ))}

        {/* Debris */}
        {data.debris_cloud.map((deb, i) => (
          <div key={i} style={{
            position: "absolute",
            left: `${deb[1] * 5}px`,
            top: `${deb[2] * 2}px`,
            width: "5px",
            height: "5px",
            backgroundColor: "red"
          }}></div>
        ))}

      </div>
    </div>
  );
}

export default App;