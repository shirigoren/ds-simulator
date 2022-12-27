from CDR.Casualties.Casualty import Casualty
from CDR.Disaster_Site.DisasterSite import DisasterSite
from CDR.Medical_Units.ALSAmbulance import ALSAmbulance
from CDR.Medical_Units.BLSAmbulance import BLSAmbulance


class problem(object):

    def __init__(self, num_of_ds, num_of_urgent, num_of_medium, num_of_non_urgent, num_of_ALS, num_of_BLS):

        self.ds = []
        self.medical_units = []

        for i in range(1, num_of_ds + 1):

            new_ds = DisasterSite(disaster_site_id=i, number_of_casualties=0, location_lat=20, location_long=30)

            for j in range(1, num_of_urgent + 1):
                new_casualty = Casualty(disaster_site_id=i, casualty_id=j, casualty_RPM=4)
                ds_casualties = new_ds.get_casualties()
                ds_casualties.append(new_casualty)

            for j in range(num_of_urgent + 1, num_of_urgent + num_of_medium + 1):
                new_casualty = Casualty(disaster_site_id=i, casualty_id=j, casualty_RPM=5)
                ds_casualties = new_ds.get_casualties()
                ds_casualties.append(new_casualty)

            for j in range(num_of_medium + num_of_urgent + 1, num_of_medium + num_of_urgent + num_of_non_urgent + 1):
                new_casualty = Casualty(disaster_site_id=i, casualty_id=j, casualty_RPM=5)
                ds_casualties = new_ds.get_casualties()
                ds_casualties.append(new_casualty)

        self.ds.append(new_ds)

        for i in range(1, num_of_ALS + 1):
            new_ALS = ALSAmbulance(medical_unit_id=1, location_lat=20, location_long=30, speed=50, creation_time=0)
            self.medical_units.append(new_ALS)

        for i in range(num_of_ALS + 1, num_of_ALS + num_of_BLS + 1):
            new_BLS = BLSAmbulance(medical_unit_id=1, location_lat=20, location_long=30, speed=50, creation_time=0)
            self.medical_units.append(new_BLS)


new_problem = problem(num_of_ds=1, num_of_urgent=5, num_of_medium=3, num_of_non_urgent=2, num_of_ALS=1, num_of_BLS=1)
print("Stop")
