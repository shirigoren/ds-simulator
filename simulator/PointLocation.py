class PointLocation(object):
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self.geo_coordinate = (self.lat, self.long)
        self.print_debug = True

    # ##------------------------------Equality and str methods -------------------------------------##

    def __eq__(self, other):
        if type(other) is PointLocation:
            return self.lat == other.lat and self.long == other.long
        return False

    def __str__(self):
        return f"({self.lat}, {self.long})"


# # TESTS
# p = PointLocation(5, 2)
# print(p)
#
# t = PointLocation(2, 5)
# print(t)
#
# g = PointLocation(2, 5)
# print(t)
#
# print(p == t)
# print(g == t)
