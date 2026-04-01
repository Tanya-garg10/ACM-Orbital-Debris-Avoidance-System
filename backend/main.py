from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

# -----------------------------
# ✅ CORS (important for React)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# GLOBAL STORAGE
# -----------------------------
space_objects = []

# -----------------------------
# Space Object Class
# -----------------------------
class SpaceObject:
    def __init__(self, id, r, v, type):
        self.id = id
        self.r = np.array(r, dtype=float)
        self.v = np.array(v, dtype=float)
        self.type = type
        self.fuel = 50.0

# -----------------------------
# Physics
# -----------------------------
mu = 398600.4418

def acceleration(r):
    return -mu * r / np.linalg.norm(r)**3

def update_position(obj, dt=1):
    a = acceleration(obj.r)
    obj.v += a * dt
    obj.r += obj.v * dt

# -----------------------------
# APIs
# -----------------------------

@app.get("/")
def home():
    return {"status": "ACM running 🚀"}

# -----------------------------
# Telemetry API
# -----------------------------
@app.post("/api/telemetry")
def telemetry(data: dict):
    global space_objects
    space_objects = []   # reset data

    for obj in data["objects"]:
        r = [obj["r"]["x"], obj["r"]["y"], obj["r"]["z"]]
        v = [obj["v"]["x"], obj["v"]["y"], obj["v"]["z"]]

        space_objects.append(
            SpaceObject(obj["id"], r, v, obj["type"])
        )

    return {
        "status": "ACK",
        "processed_count": len(space_objects)
    }

# -----------------------------
# Simulation Step API
# -----------------------------
@app.post("/api/simulate/step")
def simulate(step: dict):
    for obj in space_objects:
        update_position(obj, dt=1)

    return {
        "status": "STEP_COMPLETE",
        "objects": len(space_objects)
    }

# -----------------------------
# Visualization API
# -----------------------------
@app.get("/api/visualization/snapshot")
def snapshot():
    satellites = []
    debris = []

    for obj in space_objects:
        lat = float(obj.r[0] % 90)
        lon = float(obj.r[1] % 180)

        if obj.type == "SATELLITE":
            satellites.append({
                "id": obj.id,
                "lat": lat,
                "lon": lon,
                "fuel_kg": obj.fuel,
                "status": "NOMINAL"
            })
        else:
            debris.append([
                obj.id,
                lat,
                lon,
                float(obj.r[2])
            ])

    return {
        "timestamp": "2026-03-12T08:00:00Z",
        "satellites": satellites,
        "debris_cloud": debris
    }