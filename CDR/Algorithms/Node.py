
class Node(object):

    def __init__(self, node_id, father_id, current_state, operators):

        self.node_id = node_id
        self.father_id = father_id
        self.current_state = current_state
        self.operators = operators
        self.last_operator = None


class A_star_node(Node):

    def __init__(self, node_id, father_id, current_state, operators, g_cost, h_cost):

        Node.__init__(self, node_id, father_id, current_state, operators)
        self.g_cost = g_cost
        self.h_cost = h_cost
        if self.g_cost is not None and self.h_cost is not None:

            self.f_cost = g_cost + h_cost

        else:

            self.f_cost = None
