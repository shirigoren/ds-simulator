from PointLocation import PointLocation
from Medical_Unit import MedicalUnit

class Hospital:

    def __init__(self, hospital_id, location_lat, location_long):
        self.hospital_id = hospital_id
        self.coordinate = PointLocation(location_lat,location_long)
        self.casualties = set()
        self.capacity = None
        self.print_debug = True

    def medical_unit_arrived_to_hospital(self, medicalUnit, time_now):
        for casualty in medicalUnit.casualty_passengers:
            if self.capacity == 0:
                print("There is no room for more casualties the hospital")
                break
            self.casualties.add(casualty)
            self.capacity -= 1
            medicalUnit.remove_patient_from_agent(casualty)
            if self.print_debug:
                print(f"{time_now}:  medical unit {medicalUnit} "
                      f"arrived to hospital {self.hospital_id}")

    def __eq__(self, other):
        if type(self) is type(other):
            return self.hospital_id == other.hospital_id and self.coordinate == other.coordinate
        return False

    def __str__(self):
        return f"Hospital ID: {self.hospital_id}"


