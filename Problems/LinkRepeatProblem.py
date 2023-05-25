from Domains.Domain import Domain
from Model.Predicate import Predicate
from Model.State import State
from Problems.Problem import Problem

class LinkRepeatProblem(Problem):
    def __init__(self, domain: Domain):
        # Initialize a LinkRepeatProblem object
        super().__init__(domain)  # Call the constructor of the parent class (Problem)

        size = domain.get_size()  # Get the size from the domain
        g_0 = Predicate("g", [str(0)])  # Create a predicate for g(0)
        g_n = Predicate("g", [str(size)])  # Create a predicate for g(size)
        g_star = Predicate("g", [str("*")])  # Create a predicate for g("*")

        temp_initial_state = State("", [g_star, g_0], [])  # Create a temporary initial state with g("*") and g(0) as positive literals
        temp_goal_state = State("", [g_star, g_n], [])  # Create a temporary goal state with g("*") and g(size) as positive literals

        temp_initial_state.set_parent_index(-1)  # Set the parent index of the initial state to -1 (indicating no parent)
        temp_goal_state.set_parent_index(-1)  # Set the parent index of the goal state to -1 (indicating no parent)

        self.initial_state = temp_initial_state  # Set the initial state of the problem to the temporary initial state
        self.goal_state = temp_goal_state  # Set the goal state of the problem to the temporary goal state
