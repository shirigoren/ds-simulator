import math
import random


class PointLocation(object):
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

        # debug value
        self.print_debug = False

    # Equality method
    def __eq__(self, other):
        if not isinstance(other, PointLocation):
            return NotImplemented
        return self.lat == other.lat and self.long == other.long

    # str & repr method
    def __str__(self):
        return f"-- Point Location is ({self.lat},{self.long})-- " \
               f"\n   Latitude:{self.lat} " \
               f"\n   Longitude:{self.long} \n"

    def __repr__(self):
        return str(self)


# distance from an other PointLocation
def geo_distance(point: PointLocation, other: PointLocation):
    dx = point.lat - other.lat
    dy = point.long - other.long
    return round(math.sqrt(dx ** 2 + dy ** 2), 2)


def spawn_in_range(lat: int = 1, long: int = 1):
    x = random.randint(0, lat)
    y = random.randint(0, long)
    return PointLocation(x, y)


# # TESTS
#
# a = spawn_in_range()
# print(a)
#
# p = PointLocation(5, 2)
# print(p)
#
# t = PointLocation(2, 5)
# print(t)
#
# g = PointLocation(3, 5)
# print(g)
#
# print(p == t)
# print(p == p)
# print(geo_distance(p, t))
