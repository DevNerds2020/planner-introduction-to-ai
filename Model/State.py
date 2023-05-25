from Model.Predicate import Predicate

class State:
    def __init__(self, action_name: str, positive_literals: list[Predicate], negative_literals: list[Predicate]):
        # Initialize a State object
        self.action_name = action_name  # Set the name of the action
        self.positive_literals = set(positive_literals)  # Convert positive_literals to a set
        self.negative_literals = set(negative_literals)  # Convert negative_literals to a set

    def set_parent_index(self, parent_index: int):
        # Set the index of the parent state in the search tree
        self.parent_index = parent_index

    def get_parent_index(self) -> int:
        # Get the index of the parent state in the search tree
        return self.parent_index

    def get_action_name(self) -> str:
        # Get the name of the action associated with the state
        return self.action_name

    def get_positive_literals(self) -> set[Predicate]:
        # Get the set of positive literals in the state
        return self.positive_literals

    def get_negative_literals(self) -> set[Predicate]:
        # Get the set of negative literals in the state
        return self.negative_literals

    def __eq__(self, other) -> bool:
        # Check if two State objects are equal
        return (self.positive_literals == other.get_positive_literals() and
                self.negative_literals == other.get_negative_literals())

    def __hash__(self) -> int:
        # Compute the hash value of the State object
        result = 0
        PRIME = 1073741789  # A prime number for hashing

        # Hash each positive literal in the set of positive literals
        for positive_literal in self.positive_literals:
            result = (result + (positive_literal.__hash__() % PRIME)) % PRIME

        # Hash each negative literal in the set of negative literals
        for negative_literal in self.negative_literals:
            result = (result + (negative_literal.__hash__() % PRIME)) % PRIME

        return result
