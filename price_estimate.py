from statistics import median

class PriceEstimator:
    def estimate(self, comparables):
        #Estimate a price from comparable prices using their median.
        self.__comparables = comparables
        #ML-generated code to filter out invalid prices (non-numeric, negative, or zero)
        valid_prices = [ price for price in comparables
                             if isinstance(price, (int, float))
                             and not isinstance(price, bool)
                             and price > 0 ]

        if not valid_prices:
            raise ValueError("At least one valid price must be provided.")

        self.estimated_price = round(median(valid_prices), 2)

    def get_estimated_price(self):
        #Return the median price calculated by estimate().
        return self.estimated_price

    def get_comparables(self):
        #Return the comparable prices supplied to estimate().
        return self.__comparables
    