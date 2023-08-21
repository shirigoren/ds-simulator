from DiaryEvents.DiaryEvent import DiaryEventType
from DiaryEvents.DiaryEvent import *

class simulation(object):

    def __init__(self, simulation_number, time_start, time_end):
        self.simulation_number = simulation_number
        self.time_start = time_start #8
        self.time_end = time_end   # 240
        self.simulation_event = []
        # 08:30 - New disaster site
        # 08:45 - Team Arrived to disaster site - Medical_Unit, Disaster Site


    def run_simulation(self):
        while self.time_start <= self.time_end:
            self.simulation_event = sorted(self.simulation_event, key=lambda event: event.arrival_time, reverse=False)
            # todo: What is print_debug?
            if self.print_debug:
                if len(self.simulation_event) == 0:
                    print("No events in the diary, simulation will crush.")

            self.current_event = self.simulation_event.pop(0)

            if self.current_event.event_type == DiaryEventType.NEW_DISASTER_SITE:
                self.new_ds(self.current_event)

            elif self.current_event.event_type == DiaryEventType.ARRIVAL_TO_DISASTER_SITE:
                self.medical_unit_arrived_to_ds(self.current_event)

            elif self.current_event.event_type == DiaryEventType.WORK_COMPLITED_AT_DISASTER_SITE:
                self.medical_unit_finished_ds(self.current_event)

            elif self.current_event.event_type == DiaryEventType.DRIVING_TO_NEW_DISASTER_SITE:
                self.driving_to_new_ds()

            elif self.current_event.event_type == DiaryEventType.DRIVING_TO_THE_MEDICAL_CENTER:
                self.driving_to_medical_canter()

            elif self.current_event.event_type == DiaryEventType.DRIVING_TO_HOSPITAL_WITH_CASUALTIES:
                self.driving_to_hospital()

            elif self.current_event.event_type == DiaryEventType.FINISH_WORK_AT_HOSPITAL:
                self.finished_at_hospital()

            elif self.current_event.event_type == DiaryEventType.SIMULATION_END:
                break

            else:
                print("An unknown event was identified.")


    def new_ds(self, event):
        self.time_now = event.time_now
        self.disaster_site = event.disaster_site

        #todo: Why are the lines marked in gray?

    def medical_unit_arrived_to_ds(self, event):
        self.time_now = event.arrival_time
        self.medical_unit = event.medical_unit
        self.disaster_site = event.disaster_site
        self.medical_unit.current_location = disaster_site.coordinate
        self.disaster_site.units_on_site.add(medical_unit)

        #todo: What's wrong at the last line?

    def medical_unit_finished_ds(self,event):
        self.time_now = event.time_now
        self.medical_unit = event.medical_unit
        self.disaster_site = event.disaster_site
        self.disaster_site.units_on_site.remove(medical_unit)


    def driving_to_new_ds(self):
        pass

    def driving_to_medical_canter(self):
        pass

    def driving_to_hospital(self):
        pass

    def finished_at_hospital(self):
        pass


