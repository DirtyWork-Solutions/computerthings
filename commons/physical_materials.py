from abc import ABC, abstractmethod

from sympy.physics.units import Unit, Quantity, mm, cm, m, km


class BasePhysicalMaterial(ABC):

    @abstractmethod
    def __init__(self):

        super().__init__()

class PhysicalMaterial(BasePhysicalMaterial):

    def __init__(self):
        super().__init__()


class Material(PhysicalMaterial):

    def __init__(self):
        super().__init__()
