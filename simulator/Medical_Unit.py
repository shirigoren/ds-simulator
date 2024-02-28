import math
import enum

from simulator.PointLocation import PointLocation
from simulator.Status import Status


class Tasks(enum.Enum):  # let crate an enum of abilities
    Treating = 1
    Uploading = 2
    evacuating = 3


class MedicalUnit(object):
    """ An Abstract class that represents a Medical Unit """

    def __init__(self, medical_unit_id, location_lat, location_long, speed, creation_time, type):

        # ##------------------------Parameters for creation of a  medical unit -------------------------##

        self.medical_unit_id = medical_unit_id
        self.current_location = PointLocation(lat=location_lat, long=location_long)
        self.speed = speed
        self.creation_time = creation_time
        self.type = type
        self.base_location = self.current_location
        self.passenger_capacity = 3
        self.skills = {}

        # ##-----------------------------Parameters that updates during simulation-----------------------------##

        self.status = Status.IDLE
        self.future_arrival_time = None
        self.casualty_passengers = []  # Refer to objects
        self.time_to_finish_hospitalization = None
        self.going_to_hospital = None

        # ##-----------------------------Debug Parameters-----------------------------##

        self.medical_unit_debug = True

    # ##------------------------------Methods for change of status---------------------------------##
    # Produce a method that initializes the capabilities according to the tasks with the type of patient

    def change_status_to_idle(self):
        self.status = Status.IDLE

    def arrived_to_disaster_site(self, disaster_site, time_now):
        self.current_location = disaster_site.coordinate
        self.status = Status.WORKING_ON_SITE
        #print(f"{time_now} : medical unit: " + str(self.medical_unit_id) + " arrived to disaster site " + str(disaster_site.ds_id))

    def finished_at_ds_driving_to_hospital(self):
        self.current_location = None
        self.status = Status.ON_THE_WAY_TO_HOSPITAL
        #print(f"{time_now} : medical unit: " + str(self.medical_unit_id) + " on the way to hospital number" + str(hospital_id))

    # def finished_at_ds_driving_to_another_ds(self,new_disaster_site,time_now):
    #     self.current_location = None
    #     self.status = Status.ON_THE_WAY_TO_A_SITE_LOCATION
    #     print(f"{time_now} : medical unit: " + str(self.medical_unit_id) + " on the way to disaster site " + str(new_disaster_site.ds_id))

    # def finished_at_ds_driving_to_dispatch(self,time_now):
    #     self.current_location = None
    #     self.status = Status.RETURN_TO_DISPATCH
    #     print(f"{time_now} : medical unit: " + str(self.medical_unit_id) + "on the way to dispatch")

    def arrived_to_dispatch(self,time_now):
        self.current_location = (0,0)
        #todo: What is the location of the dispatch? can it be (0,0)?
        self.status = Status.AT_DISPATCH
        #print(f"{time_now} : medical unit: " + str(self.medical_unit_id) + "arrived to dispatch")

    def arrived_to_hospital(self,hospital, time_now):
        self.current_location = hospital.coordinate
        self.status = Status.AT_HOSPITAL
        #print(f"{time_now} : medical unit: " + str(self.medical_unit_id) + " arrived to hospital " + str(hospital.hospital_id))

    def finished_at_hospital(self,hospital,time_now):
        self.current_location = None
        self.status = Status.RETURN_TO_DISPATCH #todo 6.9.23 - is that OK?
        #print(f"{time_now} : medical unit: " + str(self.medical_unit_id) + " finished at hospital " + str(hospital.hospital_id))


    # ##------------------------------Methods for schedule sorting ---------------------------------##


    # ##------------------------------Methods for patient uploading / downloading ------------------##

    def add_casualty_to_medical_unit(self, casualty):
        # If you try to upload too many people to blow the simulation - crash it
        self.casualty_passengers.append(casualty)
        if self.passenger_capacity > self.passenger_capacity :
            print("can't add more casualties to this medical unit ")
            exit()  # crash simulation

        if self.medical_unit_debug is True:
            print(f'Agent ({self.medical_unit_id} uploaded casualty ({casualty.casualty_id}).\n')

    def remove_casualty_from_medical_unit(self, casualty):
        for casualty in self.casualty_passengers:
            if casualty.casualty_id == casualty.casualty_id:
                self.casualty_passengers.remove(casualty)
                if self.medical_unit_debug is True:
                    print(f'Agent ({self.medical_unit_id}) dropped casualty ({casualty.casualty_id}) at the hospital.\n')

    # ##------------------------------Methods for medical unit travel -------------------------------------##

    # Calculates the travel time between two points (a and b) in hours
    def travel_time(self, current_location, future_destination):
        distance = self.haversine(lon1=current_location.long, lat1=current_location.lat, lon2=future_destination.long,
                                  lat2=future_destination.lat)
        return (distance / self.speed)*60

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

    # def update_medical_unit_location(self, time_now):
    #     going_right = False
    #     going_down = False
    #     if self.current_location.lat - self.schedule[0].lat > 0:
    #         going_right = True
    #     if self.current_location.long - self.schedule[0].long > 0:
    #         going_down = True
    #     lat_delta = abs(self.schedule[0].lat - self.current_location.lat)
    #     long_delta = abs(self.schedule[0].long - self.current_location.long)
    #     time_passed = (time_now - self.future_arrival_time) / time_now
    #     if going_right is True:
    #         lat_location = self.current_location.lat
    #         lat_location = lat_location - lat_delta * time_passed
    #     else:
    #         lat_location = self.current_location.lat
    #         lat_location = lat_location + lat_delta * time_passed
    #     if going_down is True:
    #         long_location = self.current_location.long
    #         long_location = long_location - long_delta * time_passed
    #     else:
    #         long_location = self.current_location.long
    #         long_location = long_location + long_delta * time_passed
    #     self.current_location = PointLocation(lat_location, long_location)
    #     self.future_arrival_time = self.travel_time(self.current_location, self.schedule[0])

    # ##------------------------------Check Methods ------------------------------------------------##

    # def does_medical_unit_has_allocations(self):
    #     return len(self.schedule) > 0


    # ##------------------------------Equality and str methods -------------------------------------##

    def __eq__(self, other):

        if type(other) is type(MedicalUnit):
            return self.medical_unit_id == other.agent_id
        return False

    def __str__(self):
        return f"Agent id is {self.medical_unit_id}.\n"



