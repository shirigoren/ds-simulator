from Problem.EightTilePuzzle import Eight_Tile_Puzzle
from datetime import datetime
from Algorithms.Node import Node


class Breadth_First_Search(object):

    # ---------------------------------------------Constructor and Init Methods--------------------------------------###

    def __init__(self, problem):

        # --- Problem Parameters --- #

        self.nodes_index = 0
        self.problem = problem
        self.initial_state = problem.initial_state
        self.goal_state = problem.goal_state
        self.open_list = []
        self.create_initial_que(problem=problem)
        self.closed_list = []

        # --- Statistical Parameters --- #

        self.NCLO = 0
        self.closed_list_len = 0
        self.open_list_len = 0
        self.number_of_nodes_opened = 0
        self.final_NCLO = 0

        # --- Print Debug Parameters --- #

        self.print_debug = False

    def create_initial_que(self, problem):

        initial_state = problem.initial_state
        operators = problem.update_node_operators(current_state=initial_state)
        initial_node = Node(node_id=self.nodes_index, father_id=None, current_state=initial_state, operators=operators)
        self.nodes_index = self.nodes_index + 1
        self.open_list.append(initial_node)

    # ---------------------------------------------Run Method--------------------------------------------------------###

    def run_algorithm(self):

        while len(self.open_list) > 0:

            current_node = self.open_list.pop(0)

            arrived_at_goal, NCLO = self.problem.check_for_goal_state(current_node.current_state)

            self.NCLO = self.NCLO + NCLO

            if self.NCLO % 1000 == 0 and self.print_debug is True:

                print(f"NCLO: ({self.NCLO}), Node Number: ({current_node.node_id}) Current State: {current_node.current_state}, Size of Open List:{len(self.open_list)}, Size of Closed list = {len(self.closed_list)}")

            if arrived_at_goal is True:

                print("Arrived at goal")

                path = self.find_the_path_new(current_node=current_node)

                self.closed_list_len = len(self.closed_list)
                self.open_list_len = len(self.open_list)
                self.number_of_nodes_opened = self.nodes_index
                self.final_NCLO = self.NCLO
                return self.final_NCLO, self.number_of_nodes_opened, self.closed_list_len, self.open_list_len, path

            else:

                self.expand(current_node=current_node)

            if len(self.open_list) == 0:

                print("No Solutions Was Found")

    # ---------------------------------------------Algorithm Support Methods-----------------------------------------###

    def check_if_in_closed_list(self, node_for_check):

        node_to_check_state = node_for_check.current_state

        for node in self.closed_list:

            closed_list_node_state = node.current_state

            result, NCLO = self.problem.check_for_similar(current_state=node_to_check_state, state_for_check=closed_list_node_state)

            self.NCLO = self.NCLO + NCLO

            if result is True:

                if self.print_debug:

                    print(f"NCLO: ({self.NCLO}), Node Number: ({node_for_check.node_id}) With current State {node_for_check.current_state} was allready checked.")

                return True

        return False

    def check_if_in_open_list(self, node_for_check):

        node_to_check_state = node_for_check.current_state

        for node in self.open_list:

            open_list_node_state = node.current_state

            result, NCLO = self.problem.check_for_similar(current_state=node_to_check_state, state_for_check=open_list_node_state)

            self.NCLO = self.NCLO + NCLO

            if result is True:

                if self.print_debug:

                    print(f"NCLO: ({self.NCLO}), Node Number: ({node_for_check.node_id}) With current State {node_for_check.current_state} was allready checked.")

                return True

        return False

    def find_the_path_new(self, current_node):

        path = {}
        path.update({current_node.node_id: current_node})
        node_to_look = current_node.father_id

        while node_to_look is not None:

            for node in self.closed_list:

                if node.node_id == node_to_look:

                    path.update({node.node_id: node})
                    node_to_look = node.father_id
                    break

        for node_id in path:

            node = path.get(node_id)
            print(node.current_state)

        return path

    def find_the_path(self, current_node):

        j = 1

        path = {}

        path.update({j:current_node})

        j = j + 1

        node_id_to_look = current_node.father_id

        if len(self.closed_list) > 1:

            while node_id_to_look != 0:

                for node in self.closed_list:

                    if node.node_id == node_id_to_look:

                        path.update({j: node})

                        j = j + 1

                        node_id_to_look = node.father_id

        path.update({j: self.closed_list[0]})

        for item in path:

            node = path.get(item)
            node_id = node.node_id
            node_state = node.current_state
            print(f"Node:{node_id} - State {node_state}")

        return path

    def expand(self, current_node):

        current_operators = current_node.operators

        for operator in current_operators:

            operator_status = current_operators.get(operator)

            if operator_status is True:

                if operator == "up":

                    new_state = self.problem.swap_up(current_state=current_node.current_state)
                    last_opertor = "down"

                elif operator == "down":

                    new_state = self.problem.swap_down(current_state=current_node.current_state)
                    last_opertor = "up"

                elif operator == "right":

                    new_state = self.problem.swap_right(current_state=current_node.current_state)
                    last_opertor = "left"

                elif operator == "left":

                    new_state = self.problem.swap_left(current_state=current_node.current_state)
                    last_opertor = "right"

                operators = self.problem.update_node_operators(current_state=new_state)
                new_node = Node(node_id=self.nodes_index, father_id=current_node.node_id, current_state=new_state,operators=operators)
                new_node.last_operator = last_opertor

                if self.check_if_in_closed_list(node_for_check=new_node) is False:

                    if self.check_if_in_open_list(node_for_check=new_node) is False:

                        self.nodes_index = self.nodes_index + 1
                        self.open_list.append(new_node)

        # self.closed_list.append(current_node)
        self.closed_list.insert(0, current_node)

# ---------------------------------------------Statistical Methods---------------------------------------------------###


def summarize_results(stat_dict):

    final_parameters = ["NCLO", "Number of Nodes", "Size of Closed List", "Size of Open List"]

    for i in range(0, len(final_parameters)):

        sum_of_param = 0

        for item in stat_dict:
            stat_list = stat_dict.get(item)

            sum_of_param = sum_of_param + stat_list[i]

        avg = round(sum_of_param / len(stat_dict), 2)

        print(f"For {final_parameters[i]} the average is={avg}")

# ---------------------------------------------Print Debug Methods---------------------------------------------------###


def return_time():

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


# ---------------------------------------------Generate Problems Methods---------------------------------------------###

def generate_test_problems():

    eight_tile_problems = {}
    dictionary_problems = {}
    dictionary_problems.update({1: [[1,2,3],[4,5,6],[7,0,8]]})
    dictionary_problems.update({2: [[1,2,3],[4,0,6],[7,5,8]]})
    dictionary_problems.update({3: [[1,0,3],[4,2,6],[7,5,8]]})
    dictionary_problems.update({4: [[0,1,3],[4,2,6],[7,5,8]]})
    dictionary_problems.update({5: [[0,1,3],[7,2,4],[6,5,8]]})
    dictionary_problems.update({6: [[3,1,2],[4,5,6],[7,8,0]]})
    dictionary_problems.update({7: [[3,1,2],[4,5,0],[7,8,6]]})

    for i in range(1, 8):

        name = "Eight_Tile_Puzzle"
        initial_state = dictionary_problems.get(i)
        problem = Eight_Tile_Puzzle(initial_state)
        eight_tile_problems.update({i:problem})

    return eight_tile_problems


# ---------------------------------------------Main------------------------------------------------------------------###


eight_tile_puzzle_problems = generate_test_problems()

print(f"Simulation start at time: {return_time()}")

stat_dict = {}

for i in range(1, 8):

     # if i == 1:

        print(f"Problem {i} is Initiated at time: {return_time()}")

        eight_title_puzzle_problem = eight_tile_puzzle_problems.get(i)

        problem_initial_state = eight_title_puzzle_problem.initial_state

        print(f"Problem {i} initial state: {eight_title_puzzle_problem.initial_state}")

        algorithm = Breadth_First_Search(problem=eight_title_puzzle_problem)

        final_NCLO, number_of_nodes_opened, closed_list_len, open_list_len, path = algorithm.run_algorithm()

        data_list = [final_NCLO, number_of_nodes_opened, closed_list_len, open_list_len]

        stat_dict.update({i: data_list})

        print(f"Problem {i} was solved at time: {return_time()}")

print(f"Simulation ended at time: {return_time()}")

summarize_results(stat_dict=stat_dict)

