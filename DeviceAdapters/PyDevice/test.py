import numpy as np
from typing import Any
    
class RandomGenerator:
    """Demo device, used to test building device graphs. It generates random numbers for use in the Camera"""
    def __init__(self, min=0, max=1000):
        self._min = min
        self._max = max

    def generate_into(self, buffer):
        buffer[:,:] = np.random.randint(self._min, self._max, buffer.shape, dtype=np.uint16)
    
    @property
    def min(self) -> int:
        return self._min
    
    @min.setter
    def min(self, value):
        self._min = value
 
    @property
    def max(self) -> int:
        return self._max
    
    @max.setter
    def max(self, value):
        self._max = value
 
class Camera:
    """Demo camera implementation that returns noise images. To test building device graphs, the random number generator is implemented as a separate object with its own properties."""
    def __init__(self, left = 0, top = 0, width = 100, height = 100, measurement_time = 100, random_generator = None):
        if random_generator is None:
            random_generator = RandomGenerator() 

        self._resized = True
        self._image = None
        self._left = left
        self._top = top
        self._width = width
        self._height = height
        self._measurement_time = measurement_time
        self._random_generator = random_generator


    def trigger(self):
        if self._resized:
            self._image = np.zeros(self.data_shape, dtype=np.uint16)
            self._resized = False
        self.random_generator.generate_into(self._image)

    def read(self):
        return self._image

    @property
    def data_shape(self):
        return (self._height, self._width)

    @property
    def left(self) -> int:
        return self._top

    @left.setter
    def left(self, value: int):
        self._top = value

    @property
    def top(self) -> int:
        return self._top
    
    @top.setter
    def top(self, value: int):
        self._top = value
    
    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value
        self._resized = True
    
    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value
        self._resized = True

    @property
    def measurement_time(self) -> float:
        return self._measurement_time

    @measurement_time.setter
    def measurement_time(self, value):
        self._measurement_time = value

    @property
    def Binning(self) -> float:
        return 1
        
    @property
    def random_generator(self):
        return self._random_generator 
        

r = RandomGenerator()
devices = {'cam': Camera(random_generator = r), 'rng': r}
