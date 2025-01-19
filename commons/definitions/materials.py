from abc import ABC


class BaseMaterial(ABC):
    def __int__(self, name, density):
        self.name = name
        self.density = density

class ConductiveMaterial(BaseMaterial):
    def __init__(self, name, density):
        super().__init__(name, density)

def create_material() -> BaseMaterial:
    """
    Create a **material** object.
    :return: an *object instance* with a subclass of *BaseMaterial*.
    """
    raise NotImplementedError(f"Dummy Factory Function 'create_material()'")