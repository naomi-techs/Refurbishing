#Defining a class to represent a product with its attributes and methods
class Product:
    #Constructor method to initialize the product attributes

    def __init__(self, brand, model, processor, ram, storage, condition):
        #Private attributes to store the product details
        self.__brand = brand
        self.__model = model
        self.__processor = processor
        self.__ram = ram
        self.__storage = storage
        self.__condition = condition

    def get_full_name(self):
        #Method to return the full name of the product
        return f"{self.__brand} {self.__model}"

    def get_specs(self):
        #Method to return the specifications of the product
        return f"Processor: {self.__processor}, RAM: {self.__ram}, Storage: {self.__storage}"

    def get_condition(self):
        #Method to return the condition of the product
        return self.__condition