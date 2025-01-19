
class Dimensions:
    def __init__(self):
        self._dimensions = {}

class ClassicDimensions(Dimensions):
    def __init__(self):
        super().__init__()

    @property
    def length(self):
        return self._dimensions['height']

    @property
    def width(self):
        return self._dimensions['height']

    @property
    def height(self):
        return self._dimensions['height']