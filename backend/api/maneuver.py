from fastapi import APIRouter
from storage import space_objects
from physics.maneuver_calc import calculate_evasion_delta_v, fuel_used

router = APIRouter()

@router.post("/api/maneuver/auto")
def auto_maneuver():
    maneuvers = []

    for obj in space_objects:
        if obj.type != "SATELLITE":
            continue

        for threat in space_objects:
            if threat.type != "DEBRIS":
                continue

            dist = ((obj.r - threat.r)**2).sum()**0.5

            if dist < 5:   # warning zone
                dv = calculate_evasion_delta_v(obj, threat)

                obj.v += dv   # apply maneuver

                fuel = fuel_used(550, dv)

                maneuvers.append({
                    "satellite": obj.id,
                    "delta_v": dv.tolist(),
                    "fuel_used": float(fuel)
                })

    return {
        "status": "MANEUVERS_EXECUTED",
        "count": len(maneuvers),
        "details": maneuvers
    }