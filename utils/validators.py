def validate_year(year):
    current_year = 2024
    if not isinstance(year, int):
        raise ValueError("Year must be an integer")
    if year < 1900 or year > current_year:
        raise ValueError(f"Year must be between 1900 and {current_year}")
    return True

def validate_mileage(mileage):
    if not isinstance(mileage, (int, float)):
        raise ValueError("Mileage must be a number")
    if mileage < 0:
        raise ValueError("Mileage cannot be negative")
    return True

def validate_brand(brand, valid_brands):
    if brand.lower() not in valid_brands:
        raise ValueError(f"Brand must be one of: {', '.join(valid_brands)}")
    return True