from shared.validators import validate_keys


def parse_transit(transit):

    validate_keys(
        transit,
        [
            "stop_id",
            "name",
            "municipality",
            "latitude",
            "longitude",
        ],
    )

    return {
        "stop_id": str(transit["stop_id"]),
        "name": transit["name"],
        "municipality": transit["municipality"],
        "latitude": str(transit["latitude"]),
        "longitude": str(transit["longitude"]),
    }