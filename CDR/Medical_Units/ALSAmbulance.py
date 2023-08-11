from CDR.Medical_Units.Medical_Unit import MedicalUnit
from CDR.Casualties.Casualty import CasualtyType
from CDR.Medical_Units.Medical_Unit import Tasks


class ALSAmbulance(MedicalUnit):

    def __init__(self, medical_unit_id, location_lat, location_long, speed, creation_time):

        MedicalUnit.__init__(self, medical_unit_id, location_lat, location_long, speed, creation_time)
        self.number_of_urgent = 1
        self.number_of_medium = 0
        self.number_of_non_urgent = 2
        self.passenger_capacity = self.set_casualties_evacuation_capacity()  # Give them a method to define themselves
        self.skills = self.set_medical_unit_skills()  # key - [Treating - 1, Uploading - 2, evacuating - 3]

    def set_casualties_evacuation_capacity(self):

        passenger_capacity = {}

        for type_of_casualty in CasualtyType:
            passenger_capacity.update({type_of_casualty: 0})

        for type_of_casualty in passenger_capacity:

            if type_of_casualty == CasualtyType.URGENT:
                passenger_capacity.update({type_of_casualty: self.number_of_urgent})

            if type_of_casualty == CasualtyType.MEDIUM:
                passenger_capacity.update({type_of_casualty: self.number_of_medium})

            if type_of_casualty == CasualtyType.NON_URGENT:
                passenger_capacity.update({type_of_casualty: self.number_of_non_urgent})

        return passenger_capacity

    def set_medical_unit_skills(self):

        skills = {}
        list_of_tasks = []

        for type_of_task in Tasks:
            list_of_tasks.append(type_of_task)

        for type_of_casualty in self.passenger_capacity:

            number_of_passengers = self.passenger_capacity.get(type_of_casualty)

            if number_of_passengers > 0:
                skills.update({type_of_casualty: list_of_tasks})

        return skills

    def medical_unit_at_waiting_location(self, time_now):
        pass

    def medical_unit_on_way_to_waiting_location(self, time_now):
        pass


new_amb = ALSAmbulance(medical_unit_id=1, location_lat=2, location_long=5, speed=50, creation_time=0)
