from Model.State import State
from Model.Predicate import Predicate


class Action:
    def __init__(
        self,
        action_name: str,
        positive_preconditions: list[Predicate] | set[Predicate],
        negative_preconditions: list[Predicate] | set[Predicate],
        add_list: list[Predicate] | set[Predicate],
        delete_list: list[Predicate] | set[Predicate],
    ):
        """
        Initializes an Action object.

        Parameters:
        - action_name (str): the name of the action.
        - positive_preconditions (list[Predicate]|set[Predicate]): the positive preconditions for the action.
        - negative_preconditions (list[Predicate]|set[Predicate]): the negative preconditions for the action.
        - add_list (list[Predicate]|set[Predicate]): the list of positive literals added by the action.
        - delete_list (list[Predicate]|set[Predicate]): the list of negative literals deleted by the action.
        """
        self.action_name = action_name
        self.positive_preconditions = set(positive_preconditions)
        self.negative_preconditions = set(negative_preconditions)
        self.add_list = set(add_list)
        self.delete_list = set(delete_list)

    def get_action_name(self) -> str:
        """
        Returns the name of the action.
        """
        return self.action_name

    def is_unified(self, state: State) -> bool:
        """
        Checks if the action is unified with the given state.

        Parameters:
        - state (State): the state to check.

        Returns:
        - True if the action is unified with the state, False otherwise.
        """
        return (
            not self.add_list.isdisjoint(state.get_positive_literals())
        ) or (not self.delete_list.isdisjoint(state.get_negative_literals()))

    def is_conflicting(self, state: State) -> bool:
        """
        Checks if the action is conflicting with the given state.

        Parameters:
        - state (State): the state to check.

        Returns:
        - True if the action is conflicting with the state, False otherwise.
        """
        return (
            not self.add_list.isdisjoint(state.get_negative_literals())
        ) or (not self.delete_list.isdisjoint(state.get_positive_literals()))

    def is_relevant(self, state: State) -> bool:
        """
        Checks if the action is relevant to the given state.

        Parameters:
        - state (State): the state to check.

        Returns:
        - True if the action is relevant to the state, False otherwise.
        """
        return self.is_unified(state) and not self.is_conflicting(state)

    def regress(self, state: State) -> State:
        """
        Regresses the given state with the action effects.

        Parameters:
        - state (State): the state to regress.

        Returns:
        - The new state after regressing with the action effects.
        """
        result_positive_literals = (
            state.get_positive_literals() - self.add_list
        ).union(self.positive_preconditions)

        result_negative_literals = (
            state.get_negative_literals() - self.delete_list
        ).union(self.negative_preconditions)

        result = State(
            self.action_name, result_positive_literals, result_negative_literals
        )
        return result

    def progress(self, state: State) -> State:
        """
        Progresses the given state with the action effects.

        Parameters:
        - state (State): the state to progress.

        Returns:
        - The new state after progressing with the action effects.
        """
        result_positive_literals = state.get_positive_literals().union(self.add_list)
        result_negative_literals = state.get_negative_literals() - self.delete_list

        result = State(
            self.action_name, result_positive_literals, result_negative_literals
        )
        return result
