from simulator.Allocation_ds import *
from simulator.Allocation_hospital import *

def allocation_solver_ds(self):
    allocations_list = []

    new_allocation = Allocation_ds(medical_unit_id=1, disaster_site_id=1, working_start_time=9, working_end_time=12)
    allocations_list.append(new_allocation)
    return allocations_list


def allocation_solver_hospital(self, medical_unit, hospitals):
    hospital = hospitals[0]
    return Allocation_hospital(medical_unit, hospital, working_start_time=10, working_end_time=11)