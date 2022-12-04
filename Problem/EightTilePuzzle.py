import numpy as np
import copy


class Eight_Tile_Puzzle(object): # This is the class

    def __init__(self, initial_state): # This is the constructor

        self.size_of_problem = 3

        self.goal_state = [[1,2,3],[4,5,6],[7,8,0]]

        self.initial_state = initial_state

        self.current_state = initial_state

        self.operators = self.generate_operators()

        self.print_debug = False

# ---------------------------------------------Init Problem----------------------------------------------------------###

    def generate_initial_and_goal_state(self):

        conversions_test = False

        while conversions_test is False:

            initial_state_list = [1,2,3,4,5,6,7,8,0]

            np.random.shuffle(initial_state_list)

            initial_state = [[0 for i in range(self.size_of_problem)] for j in range(self.size_of_problem)]

            initial_state[0][0] = initial_state_list[0]
            initial_state[0][1] = initial_state_list[1]
            initial_state[0][2] = initial_state_list[2]
            initial_state[1][0] = initial_state_list[3]
            initial_state[1][1] = initial_state_list[4]
            initial_state[1][2] = initial_state_list[5]
            initial_state[2][0] = initial_state_list[6]
            initial_state[2][1] = initial_state_list[7]
            initial_state[2][2] = initial_state_list[8]

            goal_state = [[0 for i in range(self.size_of_problem)] for j in range(self.size_of_problem)]

            goal_state[0][0] = 1
            goal_state[0][1] = 2
            goal_state[0][2] = 3
            goal_state[1][0] = 4
            goal_state[1][1] = 5
            goal_state[1][2] = 6
            goal_state[2][0] = 7
            goal_state[2][1] = 8
            goal_state[2][2] = 0

            conversions_test = self.check_for_inversions(initial_state=initial_state)

        return initial_state, goal_state

    def generate_operators(self):

        operators = {"up": False, "down": False, "left": False, "right": False}

        return operators

    def check_for_inversions(self, initial_state):

        inversions_count = 0

        list_for_inversion_check = []

        for i in range(self.size_of_problem):

            for j in range(self.size_of_problem):

                list_for_inversion_check.append(initial_state[i][j])

        for i in range(0, len(list_for_inversion_check)):

            for j in range(i+1, len(list_for_inversion_check)):

                if list_for_inversion_check[i] != 0 and list_for_inversion_check[j] != 0:

                    if list_for_inversion_check[i] > list_for_inversion_check[j]:

                        inversions_count = inversions_count + 1

        if inversions_count % 2 == 0:

            return True

        else:

            return False

# ---------------------------------------------Operator--------------------------------------------------------------###

    def update_operators(self):

        for operator in self.operators:

            self.operators.update({operator: False})

    def update_node_operators(self, current_state):

        operators = {"up": False, "down": False, "left": False, "right": False} # Init to the operators - False.

        zero_position_i,  zero_position_j = self.find_zero_location(current_state) # Return i - row, j - col

        if zero_position_i == 0: # If in the first row.

            operators.update({"down": True})

        elif 0 < zero_position_i < self.size_of_problem - 1: # if in the middle.

            operators.update({"up": True})
            operators.update({"down": True})

        elif zero_position_i == self.size_of_problem - 1: # if in the last row.

            operators.update({"up": True})

        if zero_position_j == 0: # The first col.

            operators.update({"right": True})

        elif 0 < zero_position_j < self.size_of_problem - 1: # The second col.

            operators.update({"right": True})
            operators.update({"left": True})

        elif zero_position_j == self.size_of_problem - 1: # The third col.

            operators.update({"left": True})

        return operators

    def find_zero_location(self, current_state):

        for i in range(self.size_of_problem):

            for j in range(self.size_of_problem):

                if current_state[i][j] == 0:

                    return i,j

        zero_position = current_state.index(0)

        return zero_position

    # ---------------------------------------------Check For Goal State----------------------------------------------###

    def check_for_goal_state(self, current_state):

        NCLO = 0

        # for i in range(self.size_of_problem**2):
        #
        #     if current_state[i//self.size_of_problem][i%self.size_of_problem] !=\
        #     self.goal_state[i//self.size_of_problem][i%self.size_of_problem]:
        #
        #         NCLO = NCLO + 1
        #
        #         return False, NCLO
        #
        #     else:
        #
        #         NCLO = NCLO + 1
        #
        # return True, NCLO
        for i in range(self.size_of_problem):

            for j in range(self.size_of_problem):

                if current_state[i][j] != self.goal_state[i][j]:

                    NCLO = NCLO + 1

                    return False, NCLO

                else:

                    NCLO = NCLO + 1

        return True, NCLO

    def check_for_similar(self, current_state, state_for_check):

        NCLO = 0

        for i in range(self.size_of_problem):

            for j in range(self.size_of_problem):

                NCLO = NCLO + 1

                if current_state[i][j] != state_for_check[i][j]:

                    return False, NCLO

        return True, NCLO

    # ---------------------------------------------Swaps-------------------------------------------------------------###

    def swap_right(self, current_state):

        new_state = copy.deepcopy(current_state)
        zero_location_i, zero_location_j = self.find_zero_location(current_state=current_state)
        new_state[zero_location_i][zero_location_j], new_state[zero_location_i][zero_location_j + 1] \
            = new_state[zero_location_i][zero_location_j + 1], new_state[zero_location_i][zero_location_j]
        # left_value = new_state[zero_location_i][zero_location_j]
        # right_value = new_state[zero_location_i][zero_location_j+1]
        # new_state[zero_location_i][zero_location_j] = right_value
        # new_state[zero_location_i][zero_location_j+1] = left_value

        return new_state

    def swap_left(self, current_state):

        new_state = copy.deepcopy(current_state)
        zero_location_i, zero_location_j = self.find_zero_location(current_state=current_state)
        new_state[zero_location_i][zero_location_j - 1], new_state[zero_location_i][zero_location_j]\
            = new_state[zero_location_i][zero_location_j], new_state[zero_location_i][zero_location_j-1]
        # left_value = new_state[zero_location_i][zero_location_j-1]
        # right_value = new_state[zero_location_i][zero_location_j]
        # new_state[zero_location_i][zero_location_j-1] = right_value
        # new_state[zero_location_i][zero_location_j] = left_value

        return new_state

    def swap_up(self, current_state):

        new_state = copy.deepcopy(current_state)
        zero_location_i, zero_location_j = self.find_zero_location(current_state=current_state)
        new_state[zero_location_i - 1][zero_location_j], new_state[zero_location_i][zero_location_j]\
        = new_state[zero_location_i][zero_location_j], new_state[zero_location_i - 1][zero_location_j]
        # up_value = new_state[zero_location_i-1][zero_location_j]
        # down_value = new_state[zero_location_i][zero_location_j]
        # new_state[zero_location_i][zero_location_j] = up_value
        # new_state[zero_location_i-1][zero_location_j] = down_value

        return new_state

    def swap_down(self, current_state):

        new_state = copy.deepcopy(current_state)
        zero_location_i, zero_location_j = self.find_zero_location(current_state=current_state)
        new_state[zero_location_i][zero_location_j], new_state[zero_location_i+1][zero_location_j]\
        = new_state[zero_location_i+1][zero_location_j], new_state[zero_location_i][zero_location_j]
        # up_value = new_state[zero_location_i][zero_location_j]
        # down_value = new_state[zero_location_i+1][zero_location_j]
        # new_state[zero_location_i+1][zero_location_j] = up_value
        # new_state[zero_location_i][zero_location_j] = down_value

        return new_state

    # ---------------------------------------------Test Problems-----------------------------------------------------###

    # def update_initial_state(self, location_at_dictionary):
    #
    #     self.initial_state = self.dictionary_problems.get(location_at_dictionary)
    #
    #     return self.initial_state

    def check_results(self, path, initial_state):

        first_key = list(path.keys())[0]
        last_node = path.get(first_key)
        final_state = last_node.current_state
        counter = 1

        for key in path:

            node = path.get(key)
            last_operator = node.last_operator
            counter = counter + 1

            if last_operator == "up":

                final_state = self.swap_up(current_state=final_state)

            elif last_operator == "down":

                final_state = self.swap_down(current_state=final_state)

            elif last_operator == "right":

                final_state = self.swap_right(current_state=final_state)

            elif last_operator == "left":

                final_state = self.swap_left(current_state=final_state)

            arrived = self.check_for_initial_state(final_state=final_state, initial_state=initial_state)

            if arrived is True:

                if counter == len(path):

                    print("Arrived at goal - This is correct")
                    break

    def check_for_initial_state(self, final_state, initial_state):

        for i in range(self.size_of_problem):

            for j in range(self.size_of_problem):

                if final_state[i][j] != initial_state[i][j]:

                    return False

        return True