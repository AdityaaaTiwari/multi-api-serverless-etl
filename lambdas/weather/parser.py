from shared.validators import validate_keys


def parse_weather(weather):
    current = weather["current"]

    validate_keys(
        current,
        [
            "time",
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m",
            "weather_code",
        ],
    )

    return {
        "timestamp": current["time"],
        "temperature": str(current["temperature_2m"]),
        "humidity": str(current["relative_humidity_2m"]),
        "wind_speed": str(current["wind_speed_10m"]),
        "weather_code": str(current["weather_code"]),
    }