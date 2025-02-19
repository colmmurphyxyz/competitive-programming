from random import random
from math import sqrt

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self._radius = radius
        self._diameter = 2 * self._radius
        self._radius_squared = self._radius ** 2
        self._x_center = x_center
        self._y_center = y_center

    def _random_coord(self) -> float:
        return (random() * self._diameter) - self._radius
    
    def _distance_to_origin(self, x: float, y: float) -> float:
        return sqrt((x ** 2) + (y ** 2))
    
    def _distance_to_origin_squared(self, x: float, y: float) -> float:
        return (x ** 2) + (y ** 2)

    def randPoint(self) -> list[float]:
        while True:
            x_cand: float = self._random_coord()
            y_cand: float = self._random_coord()
            if self._distance_to_origin_squared(x_cand, y_cand) <= self._radius_squared:
                return [x_cand + self._x_center, y_cand + self._y_center]
            
if __name__ == "__main__":
    s = Solution(1.0, 1.0, 1.0)
    print(s.randPoint())
    print(s.randPoint())
    print(s.randPoint())