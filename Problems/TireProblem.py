from Model.Predicate import Predicate
from Model.State import State
from Problems.Problem import Problem

class TireProblem(Problem):
    def __init__(self, domain):
        # Initialize a TireProblem object with a specified domain
        super().__init__(domain)

        # Define the predicates for the problem
        at_flat_axle = Predicate(
            "At",
            ["Flat", "Axle"],
        )
        at_spare_trunk = Predicate(
            "At",
            ["Spare", "Trunk"],
        )
        at_spare_axle = Predicate(
            "At",
            ["Spare", "Axle"],
        )
        at_flat_trunk = Predicate(
            "At",
            ["Flat", "Trunk"],
        )

        # Create the initial and goal states using the defined predicates
        temp_initial_state = State("", [at_flat_axle, at_spare_trunk], [])
        temp_goal_state = State("", [at_spare_axle, at_flat_trunk], [])

        # Set parent indices for the initial and goal states
        temp_initial_state.set_parent_index(-1)
        temp_goal_state.set_parent_index(-1)

        # Set the initial and goal states for the problem
        self.initial_state = temp_initial_state
        self.goal_state = temp_goal_state
