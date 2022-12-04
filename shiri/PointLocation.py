class PointLocation(object):

    def __init__(self, lat, long):

        self.lat = lat
        self.long = long
        self.geo_coordinate = (lat, long)
        self.print_debug = False


    # ##------------------------------Equality and str methods -------------------------------------##

    def __eq__(self, other):

        if type(other) is type(MedicalUnit):
            return self.license_plate == other.agent_id
        return False

    def __str__(self):
        return f"Agent id is {self.license_plate}.\n"
