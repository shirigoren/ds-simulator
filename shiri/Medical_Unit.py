import math
import enum
from Departments.Casualty import #
from PointLocation import PointLocation
from Status import Status


## Raanan.y 13/11 ##


## let crate an enum of abilitise
class Tasks(enum.Enum):
    TREATMENT = 1
    UPLOADING = 2
    EVACUATING = 3


class MedicalUnit(object):
    """ An Abstract class that represents a Medical Unit """

    def __init__(self, medical_unit_id, location_lat, location_long, speed, creation_time):

        # ##------------------------Parameters for creation of an agent-------------------------##
        self.medical_unit_id = medical_unit_id
        self.current_location = PointLocation(lat=location_lat, long=location_long)
        self.speed = speed
        self.creation_time = creation_time
        self.base_location = self.current_location
        self.passenger_capacity = None   # לתת להם שיטה להגדיר בעצמם
        self.skills = {} #key - casualty type [Treatment - 1, Uploading - 1, evaci - 1]

        # ##-----------------------------Parameters that updates during simulation-----------------------------##
        self.status = Status.IDLE
        self.schedule = []
        #  יובל מחזיר לי לוח זמנים ומחזיר גם את הטיפולים רשימה של רשימות
        self.future_arrival_time = None
        self.casualty_passengers = [] # הפנייה לאובייקטים
        self.time_to_finish_hospitalization = None
        self.going_to_hospital = None

        # ##-----------------------------Debug Parameters-----------------------------##
        self.medical_unit_debug = False

    # ##------------------------------Methods for change of status---------------------------------##
# לייצר שיטה שמאתחלת את היכולות ותצעק עליהם אם הם לא עושים את זה בהתאם למשימות עם סוג המטופל

    def medical_unit_change_status_to_idle(self):
        self.status = Status.IDLE

    def medical_unit_arrived_to_disaster_site(self, disaster_site, time_now):
        self.current_location = disaster_site.location_point

    def medical_unit_at_waiting_location(self, time_now):
        raise NotImplementedError("Please Implement this method")

    def medical_unit_is_on_the_way_to_disaster_site(self, disaster_site, time_now):
        raise NotImplementedError("Please Implement this method")

    def medical_unit_on_the_way_to_hospital(self, time_now):
        raise NotImplementedError("Please Implement this method")

    def medical_unit_handling_a_casualty(self, casualty, time_now):
        raise NotImplementedError("Please Implement this method")

    def medical_unit_at_a_hospital(self, time_now):
        raise NotImplementedError("Please Implement this method")

    def medical_unit_on_way_to_waiting_location(self, time_now):
        raise NotImplementedError("Please Implement this method")

    # ##------------------------------Methods for schedule sorting ---------------------------------##

    def sort_my_schedule(self):
        self.schedule = sorted(self.schedule, key=lambda allocation: allocation.allocation_id, reverse=False)

    def update_my_schedule(self):
        self.schedule.pop(0)

    # ##------------------------------Methods for patient uploading / downloading ------------------##

    def add_patient_to_medical_unit(self, patient):  # אם מנסים להעלות יותר מידי אנשים להעיף את הסימולציה- להקריס אותה
        self.patient_passengers.append(patient)
        self.passenger_capacity = self.passenger_capacity - 1
        # if self.passenger_capacity < 0:
        if self.medical_unit_debug is True:
            print(f'Agent ({self.medical_unit_id} uploaded patient ({patient.patient_id}).\n')

    def remove_patient_from_agent(self, patient):
        for passenger in self.patient_passengers:
            if passenger.patient_id == patient.patient_id:
                self.patient_passengers.remove(patient)
                self.passenger_capacity = self.passenger_capacity + 1
                if self.medical_unit_debug is True:
                    print(f'Agent ({self.medical_unit_id}) dropped patient ({patient.patient_id}) at the hospital.\n')

    # ##------------------------------Methods for agent travel -------------------------------------##

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

    def set_destination(self, future_destination):
        self.future_destination = future_destination
        self.future_arrival_time = self.travel_time(self.current_location, self.future_destination)

    def update_medical_unit_location(self, time_now):
        going_right = False
        going_down = False
        if self.current_location.lat - self.future_destination.lat > 0:
            going_right = True
        if self.current_location.long - self.future_destination.long > 0:
            going_down = True
        lat_delta = abs(self.future_destination.lat - self.current_location.lat)
        long_delta = abs(self.future_destination.long - self.current_location.long)
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
        self.future_arrival_time = self.travel_time(self.current_location, self.future_destination)

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
