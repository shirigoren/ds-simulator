class Allocation_ds():

    def __init__(self, medical_unit_id, disaster_site_id, working_start_time, working_end_time):
        self.medical_unit_id = medical_unit_id
        self.disaster_site_id = disaster_site_id
        self.working_start_time = working_start_time
        self.working_end_time = working_end_time

    def get_medical_unit_id(self):
        return self.medical_unit_id

    def get_disaster_site_id(self):
        return self.disaster_site_id

    def get_working_start_time(self):
        return self.working_start_time

    def working_end_time(self):
        return self.working_end_time

    def overall_working_time(self):
        return self.working_end_time - self.working_start_time


