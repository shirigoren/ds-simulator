from simulator.Medical_Unit import MedicalUnit
from simulator.DisasterSite import DisasterSite
from simulator.Casualty import Casualty
from simulator.Hospital import Hospital

def generate_medical_units(number_of_medical_units):
    medical_units = []
    type = 'BLS'
    for i in range(0, number_of_medical_units):
        if i%2==0:
            type = 'ALS'
        new_medical_unit = MedicalUnit(medical_unit_id=i+1, location_lat=0, location_long=0, speed=50, creation_time=8,type=type)
        medical_units.append(new_medical_unit)
    return medical_units

def generate_disaster_site(number_of_disaster_sites):
    disaster_sites = []
    for i in range(0, number_of_disaster_sites):
        new_ds = DisasterSite(disaster_site_id=i+1, number_of_casualties=0, location_lat=0, location_long=0)
        disaster_sites.append(new_ds)
    return disaster_sites

def generate_casualties(number_of_casualties):
    casualties = []
    for i in range(0, number_of_casualties):
        new_casualty = Casualty(disaster_site_id=i+1, casualty_id=i+1)
        casualties.append(new_casualty)
    return casualties

def create_small_problem():
    medical_units = generate_medical_units(number_of_medical_units=3)
    disaster_sites = generate_disaster_site(number_of_disaster_sites=1)
    hospitals = generate_hospitals()
    casualties = generate_casualties(number_of_casualties=8)
    for casualty in casualties:
        disaster_sites[0].add_casualty(casualty)
    return medical_units, disaster_sites, hospitals, casualties

def generate_hospitals():
    hospitals = []
    hospitals.append(Hospital(1,10,30))
    hospitals.append(Hospital(2, 20, 40))
    hospitals.append(Hospital(3, 30, 80))
    hospitals.append(Hospital(4, 40, 55))
    return hospitals

medical_units, disaster_sites, hospitals, casualties = create_small_problem()



print("Stop")


