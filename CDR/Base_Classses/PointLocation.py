import math


class PointLocation(object):
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self.geo_coordinate = (self.lat, self.long)
        self.print_debug = False

    # Equality method
    def __eq__(self, other):
        if not isinstance(other, PointLocation):
            return NotImplemented
        return self.geo_coordinate == other.geo_coordinate

    # str & repr method
    def __str__(self):
        return f"-- Point Location is -- \n   Latitude:{self.lat} \n   Longitude:{self.long} \n"

    def __repr__(self):
        return str(self)

    # distance from an other PointLocation
    def distance(self, other):
        dx = self.lat - other.lat
        dy = self.long - other.long
        return round(math.sqrt(dx ** 2 + dy ** 2), 2)


# # TESTS
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
#
# print(p.distance(t))

