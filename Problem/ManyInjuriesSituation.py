class ARAN(object):

    def __init__(self, medical_units_dict, casualty_dict):
        self.number_of_medical_units = len(medical_units_dict)

        self.number_of_casualties_IDs = len(casualty_dict)

        self.initial_state = self.generate_initial_state(medical_units_dict, casualty_dict)

        # self.goal_state = self.generate_goal_state()

        self.current_state = self.initial_state

        # self.operators = self.generate_operators()

        self.print_debug = False

    def generate_initial_state(self, list_of_medical_units, list_of_casualties):

        urgent_capacity, medium_capacity, non_urgent_capacity = self.create_medical_units_capacity(
            list_of_medical_units)

        urgent_casualties, medium_casualties, non_urgent_casualties = self.create_casualty_counter(list_of_casualties)

        if urgent_capacity > urgent_casualties:

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

    def create_medical_units_capacity(self, list_of_med_units):

        urgent = 0
        medium = 0
        non_urgent = 0

        for med_unit in list_of_med_units:

            if med_unit.capacity_urgent > 0:
                urgent = urgent + med_unit.capacity_urgent

            if med_unit.capacity_medium > 0:
                medium = medium + med_unit.capacity_medium

            if med_unit.capacity_non_urgent > 0:
                non_urgent = non_urgent + med_unit.capacity_non_urgent

        return urgent, medium, non_urgent

    def create_casualty_counter(self, list_of_casualties):

        urgent = 0
        medium = 0
        non_urgent = 0

        for Casualty in list_of_casualties:

            if Casualty.__current_RPM in [0, 1, 2, 3, 4, 5, 6, 7]:
                urgent += 1

            if Casualty.__current_RPM in [8, 9]:
                medium += 1

            if Casualty.__current_RPM in [10, 11, 12]:
                non_urgent += 1

        return urgent, medium, non_urgent

    def generate_goal_state(self, case_type, list_of_medical_units, list_of_casualties):

        # urgent_capacity, medium_capacity, non_urgent_capacity = \
        #     self.create_medical_units_capacity(list_of_medical_units)

        # assuming that list of casualties is sorted by RPM
        urgent_casualties, medium_casualties, non_urgent_casualties = self.create_casualty_counter(list_of_casualties)

        if case_type == "case_1" or "case_2" or "case_3":

            for med_unit in list_of_medical_units:

                if len(list_of_casualties) != 0:

                    if med_unit.capacity_urgent > 0:

                        if urgent_casualties > 0:

                            med_unit.add_patient_to_medical_unit(list_of_casualties[0])

                            del list_of_casualties[0]

                            urgent_casualties -= 1

                if len(list_of_casualties) != 0:

                    if med_unit.capacity_medium > 0:

                        if medium_casualties > 0:

                            med_unit.add_patient_to_medical_unit(list_of_casualties[0])

                            del list_of_casualties[0]

                            medium_casualties -= 1

                if len(list_of_casualties) != 0:

                    if med_unit.capacity_non_urgent > 0:

                        if non_urgent_casualties > 0:

                            med_unit.add_patient_to_medical_unit(list_of_casualties[0])

                            del list_of_casualties[0]

                            non_urgent_casualties -= 1

                # assign casualties to medical_unit.

                # goal_state

            goal_state = {}
            for i in list_of_medical_units:
                goal_state.update({"i": i.casualty_passengers})

            return goal_state, list_of_casualties

# ----------------------------------------------------main--------------------------------------#
