from simulator.DiaryEvent import *
from simulator.DisasterSite import *
from Problem.SmallProblem import *
from simulator.allocation import Allocation
from simulator.Status import Status


class simulation(object):

    def __init__(self, simulation_number, time_start, time_end, medical_units, disaster_sites, casualties):

        self.simulation_number = simulation_number
        self.time_start = time_start #8
        self.time_end = time_end   # 240
        self.simulation_events = []
        self.disaster_sites = disaster_sites
        self.medical_units = medical_units
        self.casualties = casualties
        self.print_debug = True
        self.current_event = None

        self.create_disaster_sites_arrival_event()


    def run_simulation(self):
        while self.time_start <= self.time_end:
            self.simulation_events = sorted(self.simulation_events, key=lambda event: event.time_now, reverse=False)
            if self.print_debug:
                if len(self.simulation_events) == 0:
                    print("No events in the diary, simulation will crush.")
                    break
            self.current_event = self.simulation_events.pop(0)

            if self.current_event.event_type == DiaryEventType.NEW_DISASTER_SITE:

                allocations = self.new_ds()
                print(f"Time {self.time_now}. function that was handeled is: new_ds()")
                self.update_simulation_event(allocations=allocations)

            elif self.current_event.event_type == DiaryEventType.ARRIVAL_TO_DISASTER_SITE:
                self.medical_unit_arrived_to_ds()
                print(f"Time {self.time_now}. function that was handeled is: medical_unit_arrived_to_ds()")

            elif self.current_event.event_type == DiaryEventType.FINISH_AT_DS_DRIVING_TO_HOSPITAL:
                self.medical_unit_finished_ds_driving_to_hospital()
                print(f"Time {self.time_now}. function that was handeled is: medical_unit_finished_ds_driving_to_hospital()")

            elif self.current_event.event_type == DiaryEventType.FINISH_AT_DS_DRIVING_TO_ANOTHER_DS:
                self.medical_unit_finished_ds_driving_to_another_ds()
                print(f"Time {self.time_now}. function that was handeled is: medical_unit_finished_ds_driving_to_another_ds()")


            elif self.current_event.event_type == DiaryEventType.FINISH_AT_DS_DRIVING_TO_DISPATCH:
                self.medical_unit_finished_ds_driving_to_dispatch()
                print(f"Time {self.time_now}. function that was handeled is: medical_unit_finished_ds_driving_to_dispatch()")

            elif self.current_event.event_type == DiaryEventType.ARRIVAL_TO_DISPATCH:
                self.medical_unit_arrived_to_dispatch()
                print(f"Time {self.time_now}. function that was handeled is: medical_unit_finished_ds_driving_to_dispatch()")

            elif self.current_event.event_type == DiaryEventType.ARRIVAL_TO_HOSPITAL:
                self.medical_unit_arrived_hosspital()
                print(f"Time {self.time_now}. function that was handeled is: medical_unit_arrived_hosspital()")

            elif self.current_event.event_type == DiaryEventType.FINISH_AT_HOSPITAL:
                self.finished_at_hospital()
                print(f"Time {self.time_now}. function that was handeled is: finished_at_hospital()")

            elif self.current_event.event_type == DiaryEventType.SIMULATION_END:
                print(f"Time {self.time_now}. Simulation end.")
                break

            #else:
            #    print("An unknown event was identified.")

    def update_simulation_event(self, allocations):

        for allocation in allocations:

            unit_id = allocation.medical_unit_id
            disaster_site_id = allocation.disaster_site_id
            medical_unit = self.get_medical_unit_as_obj(medical_unit_id_to_look=unit_id)
            disaster_site = self.get_disaster_site_as_obj(disaster_site_id_to_look=disaster_site_id)

            # Case 1 - Unit is idle:

            if medical_unit.status == Status.IDLE:

                arrival_time = medical_unit.travel_time(current_location=medical_unit.current_location, future_destination=disaster_site.coordinate)
                new_arrival_to_disaster_site = ArrivalToDisasterSite(arrival_time=arrival_time, medical_unit=medical_unit, disaster_site=disaster_site)
                self.simulation_events.append(new_arrival_to_disaster_site)

            # Case 2 - Unit in driving.

            # Case 3 - Unit is working at disaster site.

    def get_medical_unit_as_obj(self, medical_unit_id_to_look):

        for medical_unit in self.medical_units:

            if medical_unit.medical_unit_id == medical_unit_id_to_look:

                return medical_unit

    def get_disaster_site_as_obj(self, disaster_site_id_to_look):

        for disaster_site in self.disaster_sites:

            if disaster_site.ds_id == disaster_site_id_to_look:

                return disaster_site





    def new_ds(self):

        self.time_now = self.current_event.time_now
        self.disaster_sites.append(self.current_event.disaster_site)
        allocations = self.allocation_solver()
        # id - 1, ds - 2, start - 5, end - 8.
        return allocations

    def medical_unit_arrived_to_ds(self):

        self.current_event.medical_unit.arrived_to_disaster_site(self.current_event.disaster_site, self.current_event.time_now)
        self.current_event.disaster_site.medical_unit_arrived(self.current_event.medical_unit, self.current_event.time_now)


    def medical_unit_finished_ds_driving_to_hospital(self):
        self.current_event.medical_unit.finished_at_ds_driving_to_hospital(self.current_event.hospital, self.current_event.time_now)
        self.current_event.disaster_site.medical_unit_finished(self.current_event.medical_unit, self.current_event.time_now)


    def medical_unit_finished_ds_driving_to_another_ds(self):
        self.current_event.medical_unit.finished_at_ds_driving_to_another_ds(self.current_event.disaster_site, self.current_event.time_now)
        self.current_event.disaster_site.medical_unit_finished(self.current_event.medical_unit, self.current_event.time_now)

    def medical_unit_finished_ds_driving_to_dispatch(self):
        self.current_event.medical_unit.finished_at_ds_driving_to_dispatch(self.current_event.time_now)
        self.current_event.disaster_site.medical_unit_finished(self.current_event.medical_unit, self.current_event.time_now)

    def medical_unit_arrived_to_dispatch(self):
        self.current_event.medical_unit.arrived_to_dispatch(self.current_event.time_now)

    def medical_unit_arrived_hosspital(self):
        self.current_event.medical_unit.arrived_to_hospital(self.current_event.hospital, self.current_event.time_now)
        self.current_event.hospital.medical_unit_arrived_to_hospital(self.current_event.medical_unit, self.current_event.time_now)

    def finished_at_hospital(self):
        self.current_event.medical_unit.finished_at_hospital(self.current_event.hospital, self.current_event.time_now)


    def allocation_solver(self):
        allocations_list =[]
        new_allocation = Allocation(medical_unit_id=1, disaster_site_id=1, working_start_time=9, working_end_time=12)
        allocations_list.append(new_allocation)
        return allocations_list

    def create_disaster_sites_arrival_event(self):

        for disaster_site in self.disaster_sites:

            new_disaster_site_event = NewDisasterSite(time_now=9, disaster_site=disaster_site)
            self.simulation_events.append(new_disaster_site_event)


medical_units, disaster_sites, casualties = create_small_problem()
new_simulation = simulation(simulation_number=1, time_start=8, time_end=24, medical_units=medical_units, disaster_sites=disaster_sites, casualties=casualties)
new_simulation.run_simulation()