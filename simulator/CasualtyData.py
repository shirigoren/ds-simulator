import math as math

"""Developed by Shiri_G - 19102022"""

class CasualtyData(object):

    def __init__(self):
        self.RPM_table = self.initialize_RPM_table()
        self.survival_table = self.initialize_survival_table()
        self.care_time_table = self.initialize_care_time_table()
        self.survival_delta = []

    # ##------------------------------Methods for Initialize the Casualty Parameters----------------------------------##

    def initialize_RPM_table(self):
        RPM_table = {0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     1: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     2: [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     3: [3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     4: [4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     5: [5, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     6: [6, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                     7: [7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0],
                     8: [8, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0],
                     9: [9, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0],
                     10: [10, 10, 9, 9, 8, 8, 7, 6, 6, 5, 5, 4, 4],
                     11: [11, 11, 11, 10, 10, 9, 8, 8, 7, 7, 6, 6, 5],
                     12: [12, 12, 12, 11, 11, 10, 10, 10, 10, 9, 9, 8, 8]}
        return RPM_table

    def initialize_survival_table(self):
        survival_table = {0: 0.052, 1: 0.089, 2: 0.15, 3: 0.23, 4: 0.35, 5: 0.49, 6: 0.63, 7: 0.75, 8: 0.84, 9: 0.9,
                          10: 0.94, 11: 0.97, 12: 0.98}
        return survival_table

    def initialize_care_time_table(self):
        care_time_table = {0: 180, 1: 170, 2: 160, 3: 150, 4: 140, 5: 130, 6: 120, 7: 110, 8: 90, 9: 60, 10: 50, 11: 40,
                           12: 30}
        for val in care_time_table.values():
            val = val/60
        return care_time_table

    # ##------------------------------Methods for Update Parameters---------------------------------------------------##

    def get_updated_rpm(self, initial_RPM, time_interval):
        # col = self.calculate_how_many_time_intervals_in_hours(time=time_interval)
        col = time_interval
        if col > 12:
            col = 12
        RPM_row = self.RPM_table.get(initial_RPM)
        updated_RPM = RPM_row[col]
        return updated_RPM

    def get_updated_survival_probability(self, updated_RPM):
        updated_survival_probability = self.survival_table.get(updated_RPM)
        return round(updated_survival_probability,2)

    def get_updated_care_time(self, initial_RPM, time_passed):
        time_interval = self.calculate_how_many_time_intervals_in_hours(time=time_passed)
        updated_RPM = self.get_updated_rpm(initial_RPM=initial_RPM, time_interval=time_interval)
        updated_care_time = self.care_time_table.get(updated_RPM)
        #print(f"\nMETHOD get_updated_care_time \ninitial RPM: {initial_RPM} \nupdated RPM: {updated_RPM}")
        return updated_care_time

    def update_RPM_survival_care_time(self, initial_RPM, time_passed):
        time_interval = self.calculate_how_many_time_intervals_in_hours(time=time_passed)
        current_RPM = self.get_updated_rpm(initial_RPM=initial_RPM, time_interval=time_interval)
        current_survival_probability = self.get_updated_survival_probability(updated_RPM=current_RPM)
        current_care_time = self.care_time_table.get(current_RPM)
        return current_RPM, current_survival_probability, current_care_time

    # ##------------------------------Methods for Calculations--------------------------------------------------------##

    def calculate_how_many_time_intervals_in_hours(self, time):
        time_in_minutes = time * 60
        reminder = time_in_minutes % 30
        time_in_minutes = time_in_minutes - reminder
        time_interval = math.floor(time_in_minutes / 30)
        return time_interval

    def calculate_time_until_RPM_zero(self, initial_RPM, time_passed):
        RPM_row = self.RPM_table.get(initial_RPM)
        time_intervals_passed = self.calculate_how_many_time_intervals_in_hours(time=time_passed)
        time_interval_until_zero = 0
        for col in RPM_row:
            if col != 0:
                time_interval_until_zero += 1
        time_until_zero_in_hours = (time_interval_until_zero - time_intervals_passed) * 0.5
        return time_until_zero_in_hours

    def get_minimal_probability(self, initial_RPM):
        RPM_row = self.RPM_table.get(initial_RPM)
        minimal_RPM = min(RPM_row)
        minimal_probability = self.survival_table.get(minimal_RPM)
        return minimal_probability

    def get_probability_upon_arrival_time(self, initial_RPM, time_passed):
        time_intervals = self.calculate_how_many_time_intervals_in_hours(time=time_passed)
        future_RPM = self.get_updated_rpm(initial_RPM=initial_RPM, time_interval=time_intervals)
        future_survival_probability = self.get_updated_survival_probability(updated_RPM=future_RPM)
        return future_survival_probability

    def get_max_probability_according_to_time_now(self, initial_RPM, time_passed):
        time_intervals = self.calculate_how_many_time_intervals_in_hours(time=time_passed)
        current_RPM = self.get_updated_rpm(initial_RPM=initial_RPM, time_interval=time_intervals)
        current_survival_probability = self.get_updated_survival_probability(updated_RPM=current_RPM)
        RPM_row = self.RPM_table.get(initial_RPM)
        minimal_RPM = min(RPM_row)
        minimal_probability = self.survival_table.get(minimal_RPM)
        probability_to_gain = current_survival_probability - minimal_probability
        return probability_to_gain



# cd = CasualtyData()
# current_RPM, current_survival_probability, current_care_time = cd.update_RPM_survival_care_time(initial_RPM=10, time_passed=7)
# print("Stop")

