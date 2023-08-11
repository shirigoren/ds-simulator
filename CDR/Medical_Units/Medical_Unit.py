import math
import enum

from CDR.Base_Classses.PointLocation import PointLocation
from CDR.Medical_Units.MedicalUnitStatus import MedicalUnitStatus

"""Developed by Raanan_Y - 13112022"""


class Tasks(enum.Enum):  # let crate an enum of abilities

    TREATING = 1
    UPLOADING = 2
    EVACUATING = 3


""" An Abstract class that represents a Medical Unit """


class MedicalUnit(object):

    def __init__(self, medical_unit_id, location_lat, location_long, speed, creation_time):

        # ##------------------------Parameters for creation of a  medical unit -------------------------##

        self.medical_unit_id = medical_unit_id
        self.current_location = PointLocation(lat=location_lat, long=location_long)
        self.speed = speed
        self.creation_time = creation_time
        self.base_location = self.current_location
        self.passenger_capacity = None  # Give them a method to define themselves
        self.skills = {}  # key - [Treating - 1, Uploading - 2, evacuating - 3]

        # ##-----------------------------Parameters that updates during simulation-----------------------------##

        self.status = MedicalUnitStatus.IDLE
        self.schedule = []
        #  The algorithm returns a list of lists: list of schedules and list of treatments
        self.future_arrival_time = None
        self.casualty_passengers = []  # Refer to objects
        self.time_to_finish_hospitalization = None
        self.going_to_hospital = None

        # ##-----------------------------Debug Parameters-----------------------------##

        self.print_debug = False

    # ##------------------------------Methods to Complete the Class Initiation---------------------------------##

    def set_medical_unit_skills(self):

        raise NotImplementedError("Please Implement this method")

    def set_casualties_evacuation_capacity(self):

        raise NotImplementedError("Please Implement this method")

    # ##------------------------------Methods for change of status---------------------------------##

    def medical_unit_change_status_to_idle(self):

        self.status = MedicalUnitStatus.IDLE
        if self.print_debug:
            print(f"{time_now}: Medical Unit {self.medical_unit_id} is idle.")  # fix this function

    def medical_unit_arrived_to_disaster_site(self, disaster_site, time_now):

        self.current_location = disaster_site.location_point
        self.update_my_schedule()

    def medical_unit_at_waiting_location(self, time_now):

        # todo - Why we need this method?
        raise NotImplementedError("Please Implement this method")

    def medical_unit_is_on_the_way_to_disaster_site(self, disaster_site, time_now):

        self.status = MedicalUnitStatus.ON_THE_WAY_TO_A_SITE_LOCATION
        if self.print_debug:
            print(
                f"{time_now}: Medical Unit {self.medical_unit_id} is on the way to disaster site {disaster_site.disaster_site_id}.")

    def medical_unit_on_the_way_to_hospital(self, hospital, time_now):

        self.status = MedicalUnitStatus.EVACUATING_A_CASUALTY_TO_HOSPITAL
        if self.print_debug:
            print(f"{time_now}: Medical Unit {self.medical_unit_id} is on the way to hospital {hospital.hospital_id}.")

    def medical_unit_handling_a_casualty(self, casualty, time_now):

        self.status = MedicalUnitStatus.TREATING_A_CASUALTY
        if self.print_debug:
            print(f"{time_now}: Medical Unit {self.medical_unit_id} is treating casualty {casualty.casualty_id}.")

    def medical_unit_uploading_a_casualty(self, casualty, time_now):

        self.status = MedicalUnitStatus.UPLOADING_A_CASUALTY
        if self.print_debug:
            print(f"{time_now}: Medical Unit {self.medical_unit_id} is uploading casualty {casualty.casualty_id}.")

    def medical_unit_at_a_hospital(self, hospital, time_now):

        self.status = MedicalUnitStatus.HOSPITALIZATION_OF_PATIENTS
        if self.print_debug:
            print(f"{time_now}: Medical Unit {self.medical_unit_id} arrived at hospital {hospital.hospital_id}.")

    def medical_unit_on_way_to_waiting_location(self, time_now):

        # todo - Did you mean back to base?

        raise NotImplementedError("Please Implement this method")

    # ##------------------------------Methods for schedule sorting ---------------------------------##

    def sort_my_schedule(self):

        self.schedule = sorted(self.schedule, key=lambda allocation: allocation.allocation_id, reverse=False)

    def update_my_schedule(self):

        if len(self.schedule) == 0:

            raise Exception(
                f"Medical unit {self.medical_unit_id} tried to pop an event for the schedule while it is empty.")

        else:

            self.schedule.pop(0)

    # ##------------------------------Methods for patient uploading / downloading ------------------##

    # If you try to upload too many people to blow the simulation - crash it
    def add_patient_to_medical_unit(self, patient):
        self.casualty_passengers.append(patient)
        self.passenger_capacity = self.passenger_capacity - 1
        if self.passenger_capacity < 0:
            raise Exception("Bug - can't add more patients to this medical unit ")
        if self.print_debug is True:
            print(f'Agent ({self.medical_unit_id} uploaded patient ({patient.patient_id}).\n')

    def remove_patient_from_medical_unit(self, patient):

        for passenger in self.casualty_passengers:

            if passenger.patient_id == patient.patient_id:

                self.casualty_passengers.remove(patient)

                self.passenger_capacity = self.passenger_capacity + 1

                # todo - Remind me how to remove items from a list in one line code, else you will nead a break.

                if self.medical_unit_debug is True:
                    print(f'Agent ({self.medical_unit_id}) dropped patient ({patient.patient_id}) at the hospital.\n')

    # ##------------------------------Methods for medical unit travel -------------------------------------##

    # Calculates the travel time between two points (a and b) in hours
    def travel_time(self, current_location, future_destination):
        distance = self.haversine(lon1=current_location.long, lat1=current_location.lat, lon2=future_destination.long,
                                  lat2=future_destination.lat)
        return distance / self.speed

    def haversine(self, lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
        # haversine formula
        d_lon = lon2 - lon1
        d_lat = lat2 - lat1
        a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        # Radius of earth in kilometers is 6371
        km = 6371 * c
        return km

    def update_medical_unit_location(self, time_now):

        going_right = False
        going_down = False

        if self.current_location.lat - self.schedule[0].lat > 0:
            going_right = True

        if self.current_location.long - self.schedule[0].long > 0:
            going_down = True

        lat_delta = abs(self.schedule[0].lat - self.current_location.lat)
        long_delta = abs(self.schedule[0].long - self.current_location.long)
        time_passed = (time_now - self.future_arrival_time) / time_now

        if going_right is True:

            lat_location = self.current_location.lat
            lat_location = lat_location - lat_delta * time_passed

        else:

            lat_location = self.current_location.lat
            lat_location = lat_location + lat_delta * time_passed

        if going_down is True:

            long_location = self.current_location.long
            long_location = long_location - long_delta * time_passed

        else:

            long_location = self.current_location.long
            long_location = long_location + long_delta * time_passed

        self.current_location = PointLocation(lat_location, long_location)

        self.future_arrival_time = self.travel_time(self.current_location, self.schedule[0])

    # ##------------------------------Check Methods ------------------------------------------------##

    def does_medical_unit_has_allocations(self):

        if len(self.schedule) > 0:

            return True

        else:

            return False

    # ##------------------------------Equality and str methods -------------------------------------##

    def __eq__(self, other):

        if type(other) is type(MedicalUnit):
            return self.medical_unit_id == other.agent_id
        return False

    def __str__(self):
        return f"Agent id is {self.medical_unit_id}.\n"
