from predictor import CarPricePredictor

def main():
    predictor = CarPricePredictor()

    print("Welcome to Car Price Predictor!")
    print("-" * 30)

    try:
        # Get user input
        year = int(input("Enter car year (1990-2024): "))
        mileage = float(input("Enter mileage (km): "))
        brand = input("Enter brand (Toyota/Honda/Ford/BMW/Mercedes): ")
        model = input("Enter model: ")

        # Predict price
        predicted_price = predictor.predict_price(year, mileage, brand, model)

        # Display result
        print("\nPrediction Result:")
        print("-" * 30)
        print(f"Car: {year} {brand} {model}")
        print(f"Mileage: {mileage:,.0f} km")
        print(f"Estimated Price: ${predicted_price:,.2f}")

    except ValueError as e:
        print(f"\nError: {str(e)}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()