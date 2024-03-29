from simulator.Medical_Unit import MedicalUnit
from simulator.Casualty import Casualty
from simulator.PointLocation import PointLocation
"""Developed by Shiri_G - 31102022"""

class DisasterSite:

    def __init__(self, disaster_site_id, number_of_casualties, location_lat, location_long):
        self.ds_id = disaster_site_id
        self.number_of_casualties = number_of_casualties
        self.coordinate = PointLocation(location_lat,location_long)
        self.casualties = []
        self.units_on_site = []
        self.print_debug = True
        self.create_casualties(number_of_casualties)

# ---------------------------------------------casualties----------------------------------------------#

    def create_casualties(self, number_of_casualties):
        for i in range(1, number_of_casualties+1):
            new_casualty = Casualty(self.ds_id,i)
            self.casualties.append(new_casualty)
            if self.print_debug:
                print(f"Casualty {i} was added to disaster site {self.ds_id}.")

# ---------------------------------------------medical unit----------------------------------------------#

    def medical_unit_arrived(self, medical_unit, time_now):
        self.units_on_site.append(medical_unit)
        # if self.print_debug:
        #     print(f"\n{time_now}: Disaster site {self.ds_id} in geographic coordinate: {self.coordinate}"
        #         f" medical team {medical_unit.medical_unit_id} has arrived.")

    def medical_unit_finished(self, medical_unit, time_now):
        self.units_on_site.remove(medical_unit)
        # if self.print_debug:
        #     print(f"{time_now}: Disaster site {self.ds_id} in geographic coordinate {self.coordinate} -"
        #           f" medical team {medical_unit.medical_unit_id} finished work.")

    def add_casualty(self, casualty):
        self.casualties.append(casualty)
    #

    def attach_casualty_to_medical_unit(self, casualtyInTreatment, medical_unit):
        medical_unit.attach_casualty(casualtyInTreatment)
        # In "medical unit" class there will be a function called "attach_casualty"
        for c in self.casualties:
            if c.casualty_id == casualtyInTreatment.casualty_id:
                self.casualties.remove(casualtyInTreatment)
                break


# ---------------------------------------------Eq and Str----------------------------------------------#

    def __eq__(self, other):
        if type(self) is type(other):
            return self.ds_id == other.ds_id and self.coordinate == other.coordinate
        return False

    def __str__(self):
        return f"disaster site id: {self.ds_id}"

# ---------------------------------------------Main------------------------------------------------------------------###



