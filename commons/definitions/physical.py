

class Dimensions:
    def __init__(self, l: int | float | None = None, w: int | float | None = None, h: int | float | None = None):
        self._dimensions = {
            "length": l,
            "width": w,
            "height": h
        }

    def set_length(self, length: int | float):
        self._dimensions["length"] = length

    def set_width(self, width: int | float):
        self._dimensions["width"] = width

    def set_height(self, height: int | float):
        self._dimensions["height"] = height


from commons.definitions.materials import *

class PhysicalProperties:
    def __init__(self):
        self._shape = {
            "dimensions": Dimensions()
        }
        self._materials = []
