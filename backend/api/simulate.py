from fastapi import APIRouter
from storage import space_objects
from physics.propagation import update_position
from physics.collision import check_collision

router = APIRouter()

@router.post("/api/simulate/step")
def simulate(step: dict):
    collisions = 0

    for obj in space_objects:
        update_position(obj, dt=1)

    for i in range(len(space_objects)):
        for j in range(i+1, len(space_objects)):
            if check_collision(space_objects[i], space_objects[j]):
                collisions += 1

    return {
        "status": "STEP_COMPLETE",
        "collisions_detected": collisions
    }