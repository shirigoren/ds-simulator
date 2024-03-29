import random
from enum import Enum
from CDR.Casualties.CasualtyData import *

"""Developed by Shiri_G - 20102022"""


class CasualtyStatus(Enum):
    UNTREATED = 1
    TRIAGE = 2
    TREATMENT = 3
    EVACUATED = 4


class CasualtyType(Enum):
    NON_URGENT = 1
    MEDIUM = 2
    URGENT = 3


def in_treatment_area():
    return random.choice([False, True])


class Casualty(object):

    def __init__(self, disaster_site_id, casualty_id, casualty_RPM):

        self.casualty_id = casualty_id
        self.disaster_site_id = disaster_site_id

        # ----Medical Variables---- #
        self.casualty_data = CasualtyData()
        self.__status = CasualtyStatus.UNTREATED
        self.__initial_RPM = casualty_RPM
        self.__current_RPM = self.__initial_RPM
        self.__survival_prob = self.casualty_data.get_updated_survival_probability(updated_RPM=self.__initial_RPM)
        self.__care_time = self.casualty_data.get_updated_care_time(initial_RPM=self.__initial_RPM, time_passed=0)
        self.__casualty_type = self.set_casualty_triage_type(casualty_RPM=casualty_RPM)

        # ----States Variables---- #

        self.__departure_time = None
        self.__arrived_to_hospital_time = None

    # ---------------------------------------------Casualty Med Condition--------------------------------------------###

    def create_casualty_data(self):
        initial_RPM = random.randint(0, 12)
        self.__care_time = CasualtyData().care_time_table.get(initial_RPM)
        self.__survival_prob = round(CasualtyData().survival_table.get(initial_RPM), 2)
        return initial_RPM

    def update_casualty_med_condition(self, time_now):
        self.__current_RPM, self.__survival_prob, self.__care_time = CasualtyData().update_RPM_survival_care_time(
            initial_RPM=self.__initial_RPM, time_passed=time_now)

    # ---------------------------------------------Change Status Methods---------------------------------------------###

    def change_to_triage(self):
        self.__status = CasualtyStatus.TRIAGE

    def change_to_treated(self):
        self.__status = CasualtyStatus.TREATMENT

    def change_to_evacuated(self):
        self.__status = CasualtyStatus.EVACUATED

    def get_casualty_status(self):
        return self.__status

    def get_casualty_type(self):

        return self.__casualty_type

    # ---------------------------------------------Stats Methods-----------------------------------------------------###

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

    # ---------------------------------------------Set Methods-------------------------------------------------###

    def set_casualty_triage_type(self, casualty_RPM):

        if 0 <= casualty_RPM <= 4:

            return CasualtyType.URGENT

        elif 5 <= casualty_RPM <= 7:

            return CasualtyType.MEDIUM

        elif 8 <= casualty_RPM <= 12:

            return CasualtyType.NON_URGENT

        else:

            raise Exception(f"Casualty RPM {casualty_RPM} that was entered is out of range of 0-12.")

    # ---------------------------------------------Previous Methods--------------------------------------------------###

    def set_first_triage(self):
        triage_type = ['u', 'm', 'nu']
        casualty_triage_type = triage_type[random.randint(0, 2)]
        return casualty_triage_type

    def in_evacuation_area(self):
        if self.__status == 3:
            return False
        return random.choice([False, True])

# ---------------------------------------------Main------------------------------------------------------------------###
