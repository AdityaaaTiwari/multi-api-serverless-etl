from shared.validators import validate_keys


def parse_earthquake(data):
    feature = data["features"][0]
    properties = feature["properties"]

    validate_keys(
        properties,
        [
            "mag",
            "place",
            "time",
            "status",
            "type",
        ],
    )

    return {
        "timestamp": str(properties["time"]),
        "magnitude": str(properties["mag"]),
        "place": properties["place"],
        "status": properties["status"],
        "type": properties["type"],
    }