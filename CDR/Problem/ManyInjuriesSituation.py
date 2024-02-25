from CDR.Casualties.Casualty import Casualty
from CDR.Casualties.Casualty import CasualtyType
from CDR.Medical_Units.Medical_Unit import MedicalUnit
from CDR.Medical_Units.ALSAmbulance import ALSAmbulance
from CDR.Medical_Units.BLSAmbulance import BLSAmbulance
from CDR.MCIProblems.AbstractProblem import problem


class ARAN(object):
    def __init__(self, problem):

        self.medical_units = self.generate_sorted_medical_units_list(problem=problem)

        self.casualties = self.generate_sorted_casualty_list(problem=problem)

        self.MCI_matrix = self.initial_matrix()

        self.initial_state = self.generate_initial_state()

        self.goal_state = self.generate_goal_state()

        self.operators = self.generate_initial_operators()

        self.print_debug = False

    def generate_sorted_medical_units_list(self, problem):

        medical_units = problem.medical_units

        medical_units.sort(key=lambda medical_unit: medical_unit.medical_unit_id, reverse=False)

        return medical_units

    def generate_sorted_casualty_list(self, problem):

        disaster_site = problem.ds.pop(0)

        casualties = disaster_site.get_casualties()

        casualties.sort(key=lambda casualty: casualty.casualty_id, reverse=False)

        return casualties

    def generate_initial_operators(self):

        operators_dict = {}

        for casualty in self.casualties:
            operators_dict.update({casualty.casualty_id: casualty.get_casualty_status()})

        return operators_dict

    def initial_matrix(self):

        matrix_rows = len(self.medical_units)
        matrix_cols = len(self.casualties)
        MCI_matrix = [[-1] * matrix_cols for i in range(matrix_rows)]
        return MCI_matrix

    def generate_initial_state(self):

        initial_state = {}

        for casualty_type in CasualtyType:
            initial_state.update({casualty_type: 0})

        return initial_state

    def generate_goal_state(self):

        goal_state = {}

        for casualty_type in CasualtyType:
            goal_state.update({casualty_type: 0})

        return goal_state

    def prev(self):
        urgent_capacity, medium_capacity, non_urgent_capacity = self.create_medical_units_capacity()
        urgent_casualties, medium_casualties, non_urgent_casualties = self.create_casualty_counter()
        if urgent_capacity > urgent_casualties:  # More medical units than casualties
            if medium_capacity > medium_casualties:
                if non_urgent_capacity > non_urgent_casualties:
                    return "case_1"
                    # Case 1 - More medical units than casualties
                    # prob BFS

        elif urgent_capacity == urgent_casualties:

            if medium_capacity == medium_casualties:

                if non_urgent_capacity == non_urgent_casualties:
                    return "case_2"
                    # the same capacity of medical units than casualties
                    # prob BFS

        else:

            return "case_3"
            # more casualties than medical units
            # FML it's AStar

    def create_medical_units_capacity(self):

        urgent = 0
        medium = 0
        non_urgent = 0

        for medical_unit in self.medical_units:

            passenger_capacity = medical_unit.passenger_capacity

            for type_of_casualty in passenger_capacity:

                capacity = passenger_capacity.get(type_of_casualty)

                if type_of_casualty == CasualtyType.URGENT:

                    urgent = urgent + capacity

                elif type_of_casualty == CasualtyType.MEDIUM:

                    medium = medium + capacity

                elif type_of_casualty == CasualtyType.NON_URGENT:

                    non_urgent = non_urgent + capacity

                else:

                    raise Exception("Bug - Did not found the casualty type.")

        return urgent, medium, non_urgent

    def create_casualty_counter(self):

        urgent = 0
        medium = 0
        non_urgent = 0

        for casualty in self.casualties:

            type_of_casualty = casualty.get_casualty_type()

            if type_of_casualty == CasualtyType.URGENT:

                urgent = urgent + 1

            elif type_of_casualty == CasualtyType.MEDIUM:

                medium = medium + 1

            elif type_of_casualty == CasualtyType.NON_URGENT:

                non_urgent = non_urgent + 1

        return urgent, medium, non_urgent

    def generate_goal_state_pre(self, case_type, list_of_medical_units, list_of_casualties):

        # urgent_capacity, medium_capacity, non_urgent_capacity = \
        #     self.create_medical_units_capacity(list_of_medical_units)

        # assuming that list of casualties is sorted by RPM
        urgent_casualties, medium_casualties, non_urgent_casualties = self.create_casualty_counter(list_of_casualties)

        if case_type == "case_1" or "case_2" or "case_3":

            for med_unit in list_of_medical_units:

                if len(list_of_casualties) != 0:

                    if med_unit.capacity_urgent > 0:

                        if urgent_casualties > 0:
                            med_unit.add_casualty_to_medical_unit(list_of_casualties[0])

                            del list_of_casualties[0]

                            urgent_casualties -= 1

                if len(list_of_casualties) != 0:

                    if med_unit.capacity_medium > 0:

                        if medium_casualties > 0:
                            med_unit.add_casualty_to_medical_unit(list_of_casualties[0])

                            del list_of_casualties[0]

                            medium_casualties -= 1

                if len(list_of_casualties) != 0:

                    if med_unit.capacity_non_urgent > 0:

                        if non_urgent_casualties > 0:
                            med_unit.add_casualty_to_medical_unit(list_of_casualties[0])

                            del list_of_casualties[0]

                            non_urgent_casualties -= 1

                # assign casualties to medical_unit.

                # goal_state

            goal_state = {}
            for i in list_of_medical_units:
                goal_state.update({"i": i.casualty_passengers})

            return goal_state, list_of_casualties

    def can_treat(self, med_unit, casualty):
        if casualty.current_RPM in med_unit.skills:
            return True
        return False

    def create_index_matrix(self, list_of_medical_units, list_of_casualties):
        matrix = []
        for med_unit in range(0, len(list_of_medical_units)):
            k = []
            for casualty in range(0, len(list_of_casualties)):
                if self.can_treat(med_unit, casualty):
                    k.append(0)
                else:
                    k.append(-1)
            matrix.append(k)
        return matrix

    def create_prob_matrix(self, list_of_medical_units, list_of_casualties):
        matrix = []
        for med_unit in range(0, len(list_of_medical_units)):
            k = []
            for casualty in range(0, len(list_of_casualties)):
                CasualtyData.get_probability_upon_arrival_time(self, ) # need to write this function
            matrix.append(k)
        return matrix


# ----------------------------------------------------main--------------------------------------#


new_problem = problem(num_of_ds=1, num_of_urgent=5, num_of_medium=3, num_of_non_urgent=2, num_of_ALS=1, num_of_BLS=1)

new_ARAN = ARAN(problem=new_problem)

print("Stop")
