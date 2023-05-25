from Domains.Domain import Domain
from Model.Action import Action
from Model.Predicate import Predicate


class LinkRepeatDomain(Domain):
    def __init__(self, size):
        # Initialize the Link-repeat Domain
        self.name = "Link-repeat Domain"  # Set the name of the domain
        self.size = size  # Set the size of the domain
        self.actions = []  # Initialize an empty list of actions
        self.define_actions()  # Define the actions for the domain

    def get_size(self):
        # Get the size of the domain
        return self.size

    def define_objects(self):
        # Define the objects of the domain
        pass  # Placeholder, as there are no objects defined in this domain

    def define_actions(self):
        # Define the actions for the domain

        # Create the A* action
        g_star = Predicate("g", ["*"])  # Create a predicate "g(*)"
        a_star = Action("A*", [], [], [g_star], [])  # Create an action "A*"
        self.actions.append(a_star)  # Add the A* action to the list of actions

        predicates = []  # Initialize an empty list of predicates
        for i in range(self.size + 1):
            g_i = Predicate("g", [str(i)])  # Create a predicate "g(i)"
            predicates.append(g_i)  # Add the predicate to the list of predicates

        # Create the A1, A2, ..., An actions
        for i in range(1, self.size + 1):
            a_i = Action(
                "A" + str(i), [g_star, predicates[i - 1]], [], [predicates[i]], [g_star]
            )  # Create an action "Ai" with preconditions and effects
            self.actions.append(a_i)  # Add the action to the list of actions
