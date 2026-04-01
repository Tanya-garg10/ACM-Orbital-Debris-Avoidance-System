from fastapi import APIRouter
from models.space_object import SpaceObject
from storage import space_objects

router = APIRouter()

@router.post("/api/telemetry")
def telemetry(data: dict):
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