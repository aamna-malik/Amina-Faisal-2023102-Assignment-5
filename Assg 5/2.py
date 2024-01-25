class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # If an instance doesn't exist, create one and store it
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        # Return the existing instance
        return cls._instances[cls]

# Applying the Singleton metaclass to a class
class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Creating instances of the SingletonClass
obj1 = SingletonClass(42)
obj2 = SingletonClass(99)

# Both obj1 and obj2 will refer to the same instance
print(obj1 is obj2)  # Output: True
