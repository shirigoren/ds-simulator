class ManyInjuriesSituation(object):

    def __init__(self, medical_units_dict, casualty_dict):
        # self.initial_state =

        # self.goal_state =

        # self.current_state = self.initial_state

        self.operators = self.generate_operators()

        self.number_of_medical_units = len(medical_units_dict)

        self.number_of_casualties_IDs = len(casualty_dict)

        self.print_debug = False

    def generate_initial_and_goal_state(self):
        pass

    def generate_operators(self):
        operators = {"up": False, "down": False}

        return operators

