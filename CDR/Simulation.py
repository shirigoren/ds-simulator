from CDR.DiaryEvent import DiaryEventType


class simulation(object):

    def __init__(self, simulation_number, time_start, time_end):
        self.simulation_number = simulation_number
        self.time_start = time_start  # 8
        self.time_end = time_end  # 240
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
                self.new_ds()

            elif self.next_event == DiaryEventType.ARRIVAL_TO_DISASTER_SITE:
                self.medical_unit_arrived_to_ds()

            elif self.next_event == DiaryEventType.WORK_COMPLETED_AT_DISASTER_SITE:
                self.medical_unit_finished_ds()

            elif self.next_event == DiaryEventType.DRIVING_TO_NEW_DISASTER_SITE:
                self.driving_to_new_ds()

            elif self.next_event == DiaryEventType.DRIVING_TO_THE_MEDICAL_CENTER:
                self.driving_to_medical_canter()

            elif self.next_event == DiaryEventType.DRIVING_TO_HOSPITAL_WITH_CASUALTIES:
                self.driving_to_hospital()

            elif self.next_event == DiaryEventType.FINISH_WORK_AT_HOSPITAL:
                self.finished_at_hospital()

            elif self.next_event == DiaryEventType.SIMULATION_END:
                break

            else:
                print("An unknown event was identified.")

    def new_ds(self):
        pass

    def medical_unit_arrived_to_ds(self, event):
        medical_unit = event.medical_unit
        disaster_site = event.disaster_site
        pass

    def medical_unit_finished_ds(self):
        pass

    def driving_to_new_ds(self):
        pass

    def driving_to_medical_canter(self):
        pass

    def driving_to_hospital(self):
        pass

    def finished_at_hospital(self):
        pass

# names = ["shiri","alon","noam","yuval"]
# print("names list before using pop: ", names)
# shiri = names.pop(0)
# print("my name is ", shiri)
# print("names list after using pop: ", names)
