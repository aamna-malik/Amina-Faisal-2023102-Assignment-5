class LoggingMeta(type):
    def __new__(cls, name, bases, dct):
        # Create the class using the standard method
        new_class = super().__new__(cls, name, bases, dct)
        
        # Log the creation of the class
        print(f"Creating class: {name}")
        
        return new_class

    def __call__(cls, *args, **kwargs):
        # Initialize an instance of the class using the standard method
        instance = super().__call__(*args, **kwargs)
        
        # Log the initialization of the instance
        print(f"Initializing instance of class: {cls.__name__}")
        
        return instance

# Applying the metaclass to a class
class MyClass(metaclass=LoggingMeta):
    def __init__(self, value):
        self.value = value

# Creating an instance of the class
obj = MyClass(42)
