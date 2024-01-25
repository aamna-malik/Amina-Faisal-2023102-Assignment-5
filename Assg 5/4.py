class InheritanceRuleMeta(type):
    def __new__(cls, name, bases, dct):
        # Check if all base classes have a specific attribute
        required_attribute = dct.get('__required_attribute__')

        for base in bases:
            if not hasattr(base, required_attribute):
                raise TypeError(f"{base.__name__} must have attribute '{required_attribute}'.")

        # Create the class using the standard method
        new_class = super().__new__(cls, name, bases, dct)

        return new_class

# Applying the InheritanceRuleMeta to a class
class ParentA:
    required_value = 42

class ParentB:
    required_value = 99

class ChildClass(ParentA, ParentB, metaclass=InheritanceRuleMeta):
    __required_attribute__ = 'required_value'

# This will raise an error since ParentC is missing the required_value attribute
try:
    class ParentC:
        pass

    class InvalidChildClass(ChildClass, ParentC):
        pass
except TypeError as e:
    print(f"Error: {e}")
