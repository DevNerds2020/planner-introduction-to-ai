from Domains.Domain import Domain
from Model.State import State

class Problem:
    def __init__(self, domain: Domain):
        # Initialize a Problem object with a specified domain
        self.domain = domain  # Store the domain for the problem

    def get_initial_state(self) -> State:
        # Get the initial state of the problem
        return self.initial_state

    def get_goal_state(self) -> State:
        # Get the goal state of the problem
        return self.goal_state

    def get_domain(self) -> Domain:
        # Get the domain associated with the problem
        return self.domain
