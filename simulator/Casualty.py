from random import *
from random import seed
from enum import Enum
from simulator.CasualtyData import *

"""Developed by Shiri_G - 20102022"""


class CasualtyStatus(Enum):
    UNTREATED = 1
    TRIAGE = 2
    TREATMENT = 3
    EVACUATED = 4


class Casualty(object):

    def __init__(self, disaster_site_id, casualty_id):

        self.casualty_id = casualty_id
        self.disaster_site_id = disaster_site_id

        # ----Medical Variables---- #

        self.__status = CasualtyStatus.UNTREATED
        self.__initial_RPM = randint(0,12)
        self.__current_RPM = self.__initial_RPM
        self.__survival_prob = round(CasualtyData().survival_table.get(self.__initial_RPM),2)
        self.__care_time = CasualtyData().care_time_table.get(self.__initial_RPM)
        self.__first_triage = self.set_first_triage()
        self.__current_triage = self.update_current_triage()

        # ----States Variables---- #

        self.__departure_time = None
        self.__arrived_to_hospital_time = None


# ---------------------------------------------Casualty Med Condition-------------------------------------------------###

    def update_casualty_med_condition(self, time_now):
        self.__current_RPM, self.__survival_prob, self.__care_time = CasualtyData().get_RPM_survival_care_time(initial_RPM=self.__initial_RPM, time_passed=time_now)

    def set_first_triage(self):
        if self.__initial_RPM >= 8:
            casualty_triage_type = "nu" # non urgent
        elif self.__initial_RPM <= 4:
            casualty_triage_type = "u" # urgent
        else:
            casualty_triage_type = "m" # medium
        return casualty_triage_type

    def update_current_triage(self):
        if self.__current_RPM >= 8:
            casualty_triage_type = "nu" # non urgent
        elif self.__current_RPM <= 4:
            casualty_triage_type = "u" # urgent
        else:
            casualty_triage_type = "m" # medium
        return casualty_triage_type

# ---------------------------------------------Change Status Methods-------------------------------------------------###

    def change_to_triage(self):
        self.__status = CasualtyStatus.TRIAGE

    def change_to_treated(self):
        self.__status = CasualtyStatus.TREATMENT

    def change_to_evacuated(self):
        self.__status = CasualtyStatus.EVACUATED

    def get_casualty_status(self):
        return self.__status

# ---------------------------------------------Stats Methods---------------------------------------------------------###

    def save_evacuation_time(self, time_now):
        self.__departure_time = time_now

    def save_arrive_to_hospital_time(self, time_now):
        self.__arrived_to_hospital_time = time_now

    # ---------------------------------------------Eq and Str--------------------------------------------------------###

    def __eq__(self, other):
        if type(self) is type(other):
            return self.casualty_id == other.casualty_id and self.disaster_site_id == self.disaster_site_id
        return False

    def __str__(self):
        return f"casualty {self.casualty_id} was injured at disaster site {self.disaster_site_id}"


# ---------------------------------------------Previous Methods------------------------------------------------------###

    def in_treatment_area(self):
        return random.choice([False, True])

    def in_evacuation_area(self):
        if self.in_treatment == False:
            return False
        return random.choice([False, True])


# ---------------------------------------------Main------------------------------------------------------------------###



