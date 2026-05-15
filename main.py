class ElectronicDevice:
    def __init__(self, brand, model, description, price):
        self.brand = brand
        self.model = model
        self.description = description
        self.price = price

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        self._model = value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value

    # This method must be inside the class
    def make_electronic_device(self):
        return (
            f"Brand for device is {self.brand}, "
            f"with model is {self.model}, "
            f"with description of {self.description}, "
            f"and for the price of {self.price} €."
        )


# Child class
class Smartphone(ElectronicDevice):
    def __init__(
        self,
        brand,
        model,
        description,
        price,
        operating_system,
        screen_size,
        battery_capacity,
        camera_resolution,
        storage_capacity
    ):
        super().__init__(brand, model, description, price)

        self.operating_system = operating_system
        self.screen_size = screen_size
        self.battery_capacity = battery_capacity
        self.camera_resolution = camera_resolution
        self.storage_capacity = storage_capacity

    @property
    def operating_system(self):
        return self._operating_system
    
    @operating_system.setter
    def operating_system(self, value):
        self._operating_system = value

    @property
    def screen_size(self):
        return self._screen_size

    @screen_size.setter
    def screen_size(self, value):
        self._screen_size = value

    @property
    def battery_capacity(self):
        return self._battery_capacity
    
    @battery_capacity.setter
    def battery_capacity(self, value):
        self._battery_capacity = value

    @property
    def camera_resolution(self):
        return self._camera_resolution
    
    @camera_resolution.setter
    def camera_resolution(self, value):
        self._camera_resolution = value

    @property
    def storage_capacity(self):
        return self._storage_capacity
    
    @storage_capacity.setter
    def storage_capacity(self, value):
        self._storage_capacity = value

    # Overridden method
    def make_electronic_device(self):
        return (
            f"Brand for device is {self.brand}, "
            f"with model is {self.model}, "
            f"with description of {self.description}, "
            f"and for the price of {self.price} €. "
            f"It has operating system {self.operating_system}, "
            f"screen size of {self.screen_size} inches, "
            f"battery capacity of {self.battery_capacity} mAh, "
            f"camera resolution of {self.camera_resolution} MP, "
            f"and storage capacity of {self.storage_capacity} GB."
        )


# Create object
smartphone = Smartphone(
    "Apple",
    "iPhone 13",
    "The latest iPhone model with advanced features",
    999,
    "iOS",
    6.1,
    3095,
    12,
    128
)

# Print details
print(smartphone.make_electronic_device())

# Print description only
print(smartphone.description)

#Output: Brand for device is Apple, with model is iPhone 13, with description of The latest iPhone model with advanced features, and for the price of 999 €. It has operating system iOS, screen size of 6.1 inches, battery capacity of 3095 mAh, camera resolution of 12 MP, and storage capacity of 128 GB.