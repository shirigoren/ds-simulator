class PointLocation(object):
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self.geo_coordinate = (self.lat, self.long)
        self.print_debug = False

    # ##------------------------------Equality and str methods -------------------------------------##

    def __eq__(self, other):
        if type(other) is PointLocation:
            return self.lat == other.lat and self.long == other.long
        print("type ERROR")
        return False

    def __str__(self):
        return f"-- Point Location is -- \n   Latitude:{self.lat} \n   Longitude:{self.long} \n"


# TESTS
# p = PointLocation(5, 2)
# print(p)

t = PointLocation(2, 5)
print(t)
#
# g = PointLocation(3, 5)
g = [3, 5]
print(g)
#
# print(p == t)
print(t < g)
