from shared.validators import validate_keys


def parse_product(product):

    validate_keys(
        product,
        [
            "id",
            "title",
            "price",
            "category",
            "brand",
        ],
    )

    return {
        "id": str(product["id"]),
        "title": product["title"],
        "price": str(product["price"]),
        "category": product["category"],
        "brand": product["brand"],
    }