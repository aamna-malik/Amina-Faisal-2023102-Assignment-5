class AttributeValidationMeta(type):
    def __new__(cls, name, bases, dct):
        # Extract the validation range from the metaclass attributes
        validation_range = dct.get('__validation_range__')

        # Iterate over class attributes and validate their values
        for attr_name, attr_value in dct.items():
            if isinstance(attr_value, (int, float)) and validation_range[0] <= attr_value <= validation_range[1]:
                print(f"Attribute '{attr_name}' validated successfully.")
            else:
                raise ValueError(f"Attribute '{attr_name}' must be within the range {validation_range}.")

        # Create the class using the standard method
        new_class = super().__new__(cls, name, bases, dct)

        return new_class

# Applying the AttributeValidationMeta to a class
class MyClass(metaclass=AttributeValidationMeta):
    __validation_range__ = (0, 100)

    def __init__(self, value):
        self.value = value

# Creating an instance of MyClass with a valid attribute value
obj1 = MyClass(42)

# This will raise an error since the value attribute is outside the specified range
try:
    obj2 = MyClass(150)
except ValueError as e:
    print(f"Error: {e}")
