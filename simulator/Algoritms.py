from simulator.Allocation_ds import *
from simulator.Allocation_hospital import *
import math

def allocation_solver_ds(disaster_site, medicalUnits, time_now):
    allocations_list = []
    num_of_nonUrgent_casualties = 0
    num_of_medium_urgent_casualties = 0
    for casualty in disaster_site.casualties:
        if casualty.first_triage == "nu":
            num_of_nonUrgent_casualties+=1
        else:
            num_of_medium_urgent_casualties+=1
    print(f"------------------------------\n"
          f"INFORMATION ABOUT DISASTER {disaster_site.ds_id}"
          f"\n------------------------------")
    print(f"In disaster site {disaster_site.ds_id} there are {disaster_site.number_of_casualties} casualties: "
          f"\n- {num_of_nonUrgent_casualties} non-urgent"
          f"\n- {num_of_medium_urgent_casualties} medium and urgent\n")
    num_of_available_BLS = 0
    num_of_available_ALS = 0
    for mu in medicalUnits:
        if mu.type == "BLS":
            num_of_available_BLS+=1
        else:
            num_of_available_ALS+=1
    print(f"There are {len(medicalUnits)} available medical units:"
          f"\n- {num_of_available_ALS} ALS (can treat 1 medium/urgent casualty and 2 non-urgent)"
          f"\n- {num_of_available_BLS} BLS (can treat 3 non-urgent casualties)\n")

    num_of_ALS_needed = num_of_medium_urgent_casualties
    num_of_allocation = 0
    BLS_list = []

    # First, I will allocate ALS medical units to treat medium & urgent casualties:
    print("---------------------------------------------"
          f" \nALLOCATE *ALS* AMBULACES TO DISASTER SITE {disaster_site.ds_id}: "
          "\n---------------------------------------------")
    for mu in medicalUnits:
        if num_of_ALS_needed == 0:
            print(f"\nAll the ALS medical units that should have been allocate to disaster site {disaster_site.ds_id} have been allocated.")
            break
        if mu.type == "ALS":
            num_of_allocation += 1
            new_allocation = Allocation_ds(mu.medical_unit_id, disaster_site.ds_id, time_now, time_now + 30)
            print(f"Allocation number {num_of_allocation}: {mu.type} medical unit {mu.medical_unit_id} in coordinate {mu.current_location} was allocated to disaster site {disaster_site.ds_id}")
            allocations_list.append(new_allocation)
            num_of_ALS_needed -= 1
        else:
            BLS_list.append(mu)
    if num_of_ALS_needed != 0: # There were not enough ALS ambulances to allocate to all the medium & urgent casualties
        print(f"\nThere were not enough ALS medical units to allocate to all the medium & urgent "
              f"casualties in disaster site {disaster_site.ds_id}.")

    # Now I want to figure out how many non-urgent casualties the ALS ambulace that i allocated can treat.
    num_of_ALS_I_allocated = num_of_medium_urgent_casualties - num_of_ALS_needed
    num_of_nu_ALS_can_trerat = num_of_ALS_I_allocated*2
    print(f"\n{num_of_ALS_I_allocated} ALS medical units were allocated to disaster site {disaster_site.ds_id}.")
    if num_of_nonUrgent_casualties < num_of_nu_ALS_can_trerat:
          print(f"They will treat {num_of_ALS_I_allocated} medium and urgent casualties and {num_of_nonUrgent_casualties} non-urgent casualties.")
    else:
          print(f"They will treat {num_of_ALS_I_allocated} medium and urgent casualties and {num_of_nu_ALS_can_trerat} non-urgent casualties.")
    print(f"{num_of_ALS_needed} medium and urgent casualties will not receive treatment.\n")

    print("---------------------------------------------"
          f" \nALLOCATE *BLS* AMBULACES TO DISASTER SITE {disaster_site.ds_id}: "
          "\n---------------------------------------------")

    # calculate how many BLS ambulances I need to send to treat the remaining non-urgent casualties in the site
    num_of_nonUrgent_left = num_of_nonUrgent_casualties-(num_of_ALS_I_allocated*2)
    if num_of_nonUrgent_left > 0:
        num_of_BLS_needed = math.ceil((num_of_nonUrgent_left)/3)

        # Now I will allocate BLS medical units to treat the remaining non-urgent casualties:
        for mu in BLS_list:
            if num_of_BLS_needed == 0:
                print(f"\nAll the BLS medical units that should have been allocate to disaster site {disaster_site.ds_id} have been allocated.")
                break
            num_of_allocation += 1
            new_allocation = Allocation_ds(mu.medical_unit_id, disaster_site.ds_id, time_now, time_now + 20)
            print(f"Allocation number {num_of_allocation}: {mu.type} medical unit {mu.medical_unit_id} in coordinate {mu.current_location} was allocated to disaster site {disaster_site.ds_id}")
            allocations_list.append(new_allocation)
            num_of_BLS_needed -= 1
            num_of_nonUrgent_left -= 3
        if num_of_BLS_needed > 0: # There were not enough BLS ambulances to allocate to all the remaining non-urgent casualties
            print(f"\nThere were not enough BLS medical units to allocate to all the non-urgent "
                  f"casualties in disaster site {disaster_site.ds_id}. "
                  f"\n{num_of_nonUrgent_left} non-urgent casualties will not receive treatment ")
        # if num_of_nonUrgent_left < 0:
        #     num_of_nonUrgent_left += 3
        print(f"\n{num_of_allocation-num_of_ALS_I_allocated} BLS medical units were allocated to disaster site {disaster_site.ds_id}. "
              f"\nThey will treat {num_of_nonUrgent_left+3*(num_of_allocation-num_of_ALS_I_allocated)} non-urgent casualties\n")

    else:
        print(f"No BLS ambulance needed\n")

    print("--------------------------------------------"
          f" \nEND OF DISASTER SITES ALLOCATION ALGORITHM! "
          "\n--------------------------------------------\n")
    return allocations_list



def allocation_solver_hospital(self, medical_unit, hospitals):
    hospital = hospitals[0]
    return Allocation_hospital(medical_unit, hospital)