from CDR.Medical_Units.ALSAmbulance import ALSAmbulance
from CDR.Medical_Units.BLSAmbulance import BLSAmbulance
from CDR.Base_Classses.PointLocation import PointLocation
from CDR.Casualties.Casualty import Casualty

"""Developed by Shiri_G - 31102022"""


class DisasterSite:

    def __init__(self, disaster_site_id, number_of_casualties, location_lat, location_long):

        self.__ds_id = disaster_site_id
        self.__number_of_casualties = number_of_casualties
        self.__coordinate = PointLocation(location_lat, location_long)
        self.__casualties = []
        self.__units_on_site = []
        self.print_debug = True
        self.create_casualties(number_of_casualties)

    # ---------------------------------------------casualties----------------------------------------------#

    def create_casualties(self, number_of_casualties):
        for i in range(1, number_of_casualties + 1):
            new_casualty = Casualty(self.ds_id, i)
            self.casualties.add(new_casualty)
            if self.print_debug:
                print(f"Casualty {i} was added to disaster site {self.ds_id}.")

    # ---------------------------------------------medical unit----------------------------------------------#

    def medical_unit_arrived(self, medical_unit, time_now):
        self.units_on_site.add(medical_unit)
        if self.print_debug:
            print(f"{time_now}: Disaster site {self.ds_id} in geographic coordinate {self.coordinate} -"
                  f" medical team {medical_unit.id} was arrived.")

    def attach_casualty_to_medical_unit(self, casualtyInTreatment, medical_unit):
        medical_unit.attach_casualty(casualtyInTreatment)
        # In "medical unit" class there will be a function called "attach_casualty"
        for c in self.casualties:
            if c.casualty_id == casualtyInTreatment.casualty_id:
                self.casualties.remove(casualtyInTreatment)
                break

    def medical_unit_left(self, medical_unit, time_now):
        self.units_on_site.remove(medical_unit)
        if self.print_debug:
            print(f"{time_now}: Disaster site {self.ds_id} - medical team {medical_unit.id} left.")

    # ---------------------------------------------Getters-------------------------------------------------#

    def get_ds_id(self):

        return self.__ds_id

    def get_casualties(self):

        return self.__casualties

    def get_number_of_casualties(self):

        return len(self.__number_of_casualties)

    def get_site_location(self):

        return self.__coordinate

    def get_units_on_site(self):

        return self.__units_on_site

    # ---------------------------------------------Eq and Str----------------------------------------------#

    def __eq__(self, other):
        if type(self) is type(other):
            return self.ds_id == other.ds_id and self.coordinate == other.coordinate
        return False

    def __str__(self):
        return f"disaster site id: {self.ds_id}"
