def calculate_base_price(car):
    """Calculate base price based on car year"""
    base_price = 20000
    year_factor = (car.year - 1990) * 500
    return max(0, base_price + year_factor)

def calculate_mileage_adjustment(car):
    """Calculate price adjustment based on mileage"""
    return -(car.mileage / 10000) * 1000

def calculate_brand_multiplier(car):
    """Get price multiplier based on brand"""
    brand_factors = {
        'toyota': 1.0,
        'honda': 1.0,
        'ford': 0.9,
        'bmw': 1.5,
        'mercedes': 1.6
    }
    return brand_factors.get(car.brand.lower(), 1.0)