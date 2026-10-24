from ai_listing import AIListing
from price_estimate import PriceEstimator
from product import Product


def main():
    product_specs = {
        "brand": "Dell",
        "model": "XPS 13",
        "processor": "Intel i7",
        "ram": "16GB",
        "storage": "512GB SSD",
        "condition": "Refurbished",
    }
    laptop = Product(
        product_specs["brand"],
        product_specs["model"],
        product_specs["processor"],
        product_specs["ram"],
        product_specs["storage"],
        product_specs["condition"],
    )

    comparables = [600, 900, 400, 800, 700]
    estimator = PriceEstimator()
    estimator.estimate(comparables)
    estimated_price = estimator.get_estimated_price()

    print("Product Name:", laptop.get_full_name(), flush=True)
    print("Specifications:", laptop.get_specs(), flush=True)
    print("Condition:", laptop.get_condition(), flush=True)
    print("Estimated Price:", estimated_price, flush=True)
    print("Generating listing with the AI service...", flush=True)

    ai_listing = AIListing()
    listing = ai_listing.generate_listing(
        product_specs=product_specs,
        estimated_price_=estimated_price,
        comparables=estimator.get_comparables(),
    )
    print("Generated Listing:\n", listing, flush=True)


if __name__ == "__main__":
    main()
