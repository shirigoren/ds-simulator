from simulator.DiaryEvent import *
from simulator.DisasterSite import *
from Problem.SmallProblem import *
from simulator.Allocation_ds import *
from simulator.Status import Status
from Algoritms import *
from random import *

seed(1)

class simulation(object):

    def __init__(self, simulation_number, time_now, time_end, medical_units, disaster_sites,hospitals, casualties):

        self.simulation_number = simulation_number
        self.time_now = time_now #8
        self.time_end = time_end   # 240
        self.simulation_events = []
        self.disaster_sites = disaster_sites
        self.medical_units = medical_units
        self.hospitals = hospitals
        self.casualties = casualties
        self.print_debug = True
        self.current_event = None

        self.create_disaster_sites_event()


    def run_simulation(self):
        while self.time_now <= self.time_end:
            self.simulation_events = sorted(self.simulation_events, key=lambda event: event.time_now, reverse=False)
            if self.print_debug:
                if len(self.simulation_events) == 0:
                    print("No events in the diary, simulation is over.")
                    break
            self.current_event = self.simulation_events.pop(0)

            if self.current_event.event_type == DiaryEventType.NEW_DISASTER_SITE:
                self.new_ds()
                print(f"Time {self.time_now}. function that was handeled is: new_ds()")

            elif self.current_event.event_type == DiaryEventType.ARRIVAL_TO_DISASTER_SITE:
                self.medical_unit_arrived_to_ds()
                print(f"Time {self.time_now}. function that was handeled is: medical_unit_arrived_to_ds()")

            elif self.current_event.event_type == DiaryEventType.FINISH_AT_DS:
                self.medical_unit_finished_ds_driving_to_hospital()
                print(f"Time {self.time_now}. function that was handeled is: medical_unit_finished_ds_driving_to_hospital()")

            # elif self.current_event.event_type == DiaryEventType.FINISH_AT_DS_DRIVING_TO_ANOTHER_DS:
            #     self.medical_unit_finished_ds_driving_to_another_ds()
            #     print(f"Time {self.time_now}. function that was handeled is: medical_unit_finished_ds_driving_to_another_ds()")
            #
            # elif self.current_event.event_type == DiaryEventType.FINISH_AT_DS_DRIVING_TO_DISPATCH:
            #     self.medical_unit_finished_ds_driving_to_dispatch()
            #     print(f"Time {self.time_now}. function that was handeled is: medical_unit_finished_ds_driving_to_dispatch()")
            #
            # elif self.current_event.event_type == DiaryEventType.ARRIVAL_TO_DISPATCH:
            #     self.medical_unit_arrived_to_dispatch()
            #     print(f"Time {self.time_now}. function that was handeled is: medical_unit_finished_ds_driving_to_dispatch()")

            elif self.current_event.event_type == DiaryEventType.ARRIVAL_TO_HOSPITAL:
                self.medical_unit_arrived_hospital()
                print(f"Time {self.time_now}. function that was handeled is: medical_unit_arrived_hosspital()")

            # elif self.current_event.event_type == DiaryEventType.FINISH_AT_HOSPITAL:
            #     self.finished_at_hospital()
            #     print(f"Time {self.time_now}. function that was handeled is: finished_at_hospital()")

            elif self.current_event.event_type == DiaryEventType.SIMULATION_END:
                print(f"Time {self.time_now}. Simulation end.")
                break

            #else:
            #    print("An unknown event was identified.")


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
        allocations = allocation_solver_ds(self)
        for allocation in allocations:
            unit_id = allocation.medical_unit_id
            disaster_site_id = allocation.disaster_site_id
            medical_unit = self.get_medical_unit_as_obj(medical_unit_id_to_look=unit_id)
            disaster_site = self.get_disaster_site_as_obj(disaster_site_id_to_look=disaster_site_id)
            travel_time = medical_unit.travel_time(current_location=medical_unit.current_location, future_destination=disaster_site.coordinate)
            new_arrival_to_disaster_site = ArrivalToDisasterSite(arrival_time=self.time_now + travel_time, medical_unit=medical_unit, disaster_site=disaster_site)
            self.simulation_events.append(new_arrival_to_disaster_site)
            medical_unit.status = Status.ON_THE_WAY_TO_A_SITE_LOCATION


    def medical_unit_arrived_to_ds(self):
        self.current_event.medical_unit.arrived_to_disaster_site(self.current_event.disaster_site, self.current_event.time_now)
        self.current_event.disaster_site.medical_unit_arrived(self.current_event.medical_unit, self.current_event.time_now)
        finish_at_ds = FinishWorkDisasterSite(self.time_now,self.current_event.medical_unit , self.current_event.disaster_site)
        self.simulation_events.append(finish_at_ds)

    def medical_unit_finished_ds_driving_to_hospital(self):
        medical_unit = self.current_event.medical_unit
        disaster_site = self.current_event.disaster_site
        allocation = allocation_solver_hospital(self,medical_unit,self.hospitals)
        medical_unit.finished_at_ds_driving_to_hospital(allocation.hospital.hospital_id, self.current_event.time_now)
        disaster_site.medical_unit_finished(medical_unit, self.current_event.time_now)
        travel_time = medical_unit.travel_time(disaster_site.coordinate, allocation.hospital.coordinate)
        arrival_to_hospital = ArrivalToHospital(self.time_now+travel_time, medical_unit, allocation.hospital)
        self.simulation_events.append(arrival_to_hospital)

    # def medical_unit_finished_ds_driving_to_another_ds(self):
    #     self.current_event.medical_unit.finished_at_ds_driving_to_another_ds(self.current_event.disaster_site, self.current_event.time_now)
    #     self.current_event.disaster_site.medical_unit_finished(self.current_event.medical_unit, self.current_event.time_now)

    # def medical_unit_finished_ds_driving_to_dispatch(self):
    #     self.current_event.medical_unit.finished_at_ds_driving_to_dispatch(self.current_event.time_now)
    #     self.current_event.disaster_site.medical_unit_finished(self.current_event.medical_unit, self.current_event.time_now)

    # def medical_unit_arrived_to_dispatch(self):
    #     self.current_event.medical_unit.arrived_to_dispatch(self.current_event.time_now)

    def medical_unit_arrived_hospital(self):
        self.current_event.medical_unit.arrived_to_hospital(self.current_event.hospital, self.current_event.time_now)
        self.current_event.hospital.medical_unit_arrived_to_hospital(self.current_event.medical_unit, self.current_event.time_now)

    # def finished_at_hospital(self):
    #     self.current_event.medical_unit.finished_at_hospital(self.current_event.hospital, self.current_event.time_now)




    def create_disaster_sites_event(self):
        for disaster_site in self.disaster_sites:
            new_disaster_site_event = NewDisasterSite(time_now=9, disaster_site=disaster_site)
            self.simulation_events.append(new_disaster_site_event)


medical_units, disaster_sites, hospitals, casualties = create_small_problem()
new_simulation = simulation(simulation_number=1, time_now=8, time_end=24, medical_units=medical_units, disaster_sites=disaster_sites, hospitals=hospitals, casualties=casualties)
new_simulation.run_simulation()