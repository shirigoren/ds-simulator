from DiaryEvents.DiaryEvent import DiaryEventType
from DiaryEvents.DiaryEvent import *

class simulation(object):

    def __init__(self, simulation_number, time_start, time_end):

        self.simulation_number = simulation_number
        self.time_start = time_start #8
        self.time_end = time_end   # 240
        self.diary_event = []
        # 08:30 - New disaster site
        # 08:45 - Team Arrived to disaster site - Medical_Unit, Disaster Site



    def run_simulation(self):

        while self.time_start <= self.time_end:

            self.diary_event = sorted(self.diary_event, key=lambda event: event.arrival_time, reverse=False)
            if self.print_debug:
                if len(self.diary_event) == 0:
                    print("No events in the diary, simulation will crush.")
            self.next_event = self.diary_event.pop(0)

            if self.next_event == DiaryEventType.NEW_DISASTER_SITE:
                self.new_ds_arrival()
            elif self.next_event == "Arrival to disaster site"
            elif self.next_event == DiaryEventType.SIMULATION_END:
                break


            else:

                print("An unknown event was identified.")



    def new_ds_arrival(self):

        # allocations = call allocation_solver (allocation - id, medical unit - id, disaster site - id)
        # Create for each allocation an event in the diary event.
        event_type = DiaryEventType.ARRIVAL_TO_DISASTER_SITE
        medical_unit_id = 1
        disaster_site_id = 8
        new_event = ArrivalToDisasterSite(arrival_time=8.5, medical_unit=medical_unit_id, disaster_site=disaster_site_id)
        self.diary_event.append(new_event)
        pass

    def medical_unit_arrived_to_ds(self, event):

        medical_unit = event.medical_unit
        disaster_site = event.disaster_site

        pass