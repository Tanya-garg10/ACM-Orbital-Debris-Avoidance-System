# 🚀 Orbital Insight Dashboard

A real-time space objects monitoring dashboard built for the **National Space Hackathon 2026**.  
Tracks satellites, debris clouds, and simulates basic orbital maneuvers using physics models.

## 📂 Project Structure

```

project/
│
├── backend/
│   ├── main.py              # FastAPI backend
│   ├── physics/             # Physics modules (gravity, maneuvers)
│   ├── api/                 # Maneuver APIs
│   ├── models/              # Optional DB/models if needed
|   ├── requirements.txt        # Python dependencies
│
├── frontend/                # React dashboard
│
├── data/
│   └── ground_stations.csv  # Ground station coordinates
│
├── Dockerfile               # Container setup
└── README.md

````

## 🧩 Features

- Real-time satellite and debris visualization
- Basic orbital physics simulation
- Collision detection and warnings
- Maneuver execution with fuel calculation
- REST APIs for telemetry, simulation, and snapshots
- Interactive React frontend dashboard

## ⚡ Getting Started

### 1️⃣ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
pip install -r requirements.txt
uvicorn main:app --reload
````

* Backend runs on: `http://127.0.0.1:8000/`
* Test API:

```bash
curl http://127.0.0.1:8000/
```

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

* React dashboard runs on: `http://localhost:3000/`
* Make sure backend is running first.

### 3️⃣ Telemetry Example

```javascript
fetch("http://127.0.0.1:8000/api/telemetry", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    objects: [
      { id: "SAT-1", type: "SATELLITE", r: {x:7000,y:0,z:0}, v:{x:0,y:7.5,z:0} },
      { id: "DEB-1", type: "DEBRIS", r: {x:7002,y:0,z:0}, v:{x:0,y:7.5,z:0} }
    ]
  })
}).then(res => res.json()).then(console.log)
```

### 4️⃣ Docker Setup

```bash
docker build -t orbital-insight .
docker run -p 8000:8000 orbital-insight
```

* Exposes backend on port 8000.
* Frontend can be served via `npm run build` and any static server.

## 📜 APIs

| Endpoint                      | Method | Description                                    |
| ----------------------------- | ------ | ---------------------------------------------- |
| `/`                           | GET    | Health check                                   |
| `/api/telemetry`              | POST   | Send satellite/debris positions and velocities |
| `/api/simulate/step`          | POST   | Run simulation step & maneuvers                |
| `/api/visualization/snapshot` | GET    | Get current positions for dashboard            |

## ⚙️ Physics Models

* Central gravity acceleration
* Maneuver computation with fuel tracking
* Collision detection between objects

## 🛠 Hackathon Notes

* All simulations run locally, no external services
* Ground station data in `data/ground_stations.csv`
* Ensure CORS enabled for frontend-backend communication

Made with ❤️ by Tanya Garg 
