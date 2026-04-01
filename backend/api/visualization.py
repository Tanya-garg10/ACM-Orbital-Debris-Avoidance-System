from fastapi import APIRouter
from storage import space_objects

router = APIRouter()

@router.get("/api/visualization/snapshot")
def snapshot():
    satellites = []
    debris = []

    for obj in space_objects:
        lat = obj.r[0] % 90
        lon = obj.r[1] % 180

        if obj.type == "SATELLITE":
            satellites.append({
                "id": obj.id,
                "lat": float(lat),
                "lon": float(lon),
                "fuel_kg": 50,
                "status": "NOMINAL"
            })
        else:
            debris.append([obj.id, float(lat), float(lon), float(obj.r[2])])

    return {
        "timestamp": "2026-03-12T08:00:00Z",
        "satellites": satellites,
        "debris_cloud": debris
    }