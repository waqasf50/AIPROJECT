from models.car_model import Car
from utils.validators import validate_year, validate_mileage, validate_brand
from utils.price_calculator import (
    calculate_base_price,
    calculate_mileage_adjustment,
    calculate_brand_multiplier
)

class CarPricePredictor:
    def __init__(self):
        self.valid_brands = ['toyota', 'honda', 'ford', 'bmw', 'mercedes']

    def predict_price(self, year, mileage, brand, model):
        # Validate inputs
        validate_year(year)
        validate_mileage(mileage)
        validate_brand(brand.lower(), self.valid_brands)

        # Create car instance
        car = Car(year, mileage, brand, model)

        # Calculate price components
        base_price = calculate_base_price(car)
        mileage_adjustment = calculate_mileage_adjustment(car)
        brand_multiplier = calculate_brand_multiplier(car)

        # Calculate final price
        final_price = (base_price + mileage_adjustment) * brand_multiplier

        return max(0, round(final_price))