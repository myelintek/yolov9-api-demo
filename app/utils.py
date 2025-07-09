def get_status():
    return {
        "state": "ready",
        "msg": ""
    }


def get_cvat_info():
    return {
        "name": "Lpr detector Malaysia",
        "description": "detect Plate/Car/Motobike",
        "type": "detector",
        "spec": [
            {"id": 0, "name": "Plate"},
            {"id": 1, "name": "Car"},
            {"id": 2, "name": "Motobike"}
        ]
    }

