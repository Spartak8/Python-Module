def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]
    valid = any(ing in ingredients.lower() for ing in allowed)
    keyword = "VALID" if valid else "INVALID"
    return f"{ingredients} - {keyword}"
