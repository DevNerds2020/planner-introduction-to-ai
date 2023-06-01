from queue import Queue
from Planners.Planner import Planner

"""
result is a list that stores the sequence of actions needed to reach the goal state, in case the planner finds a solution.

frontier is a queue data structure that stores the indices of states that need to be expanded. It follows the First-In-First-Out (FIFO) rule, meaning that the first state that was added to the queue will be the first one to be explored.

all_states is a list that stores all the states that have been generated during the search process, including both the initial state and any successor states that were created. The index of each state in this list represents its unique identifier.

visited is a set that stores all the states that have already been visited during the search process. If a state has already been visited, it will not be added to either the frontier or all_states again. This helps to prevent the algorithm from revisiting the same states multiple times and getting stuck in a loop

"""
class BackwardPlanner(Planner):
    def __init__(self, problem):
        super().__init__(problem)

    def search(self):
        total_state_index = 0
        result = []
        frontier = Queue()
        visited = set()
        all_states = []

        # Check if goal state is already reached
        if self.goal_test(self.problem.get_goal_state()):
            return result

        # Add goal state to frontier and visited set
        frontier.put(total_state_index)
        visited.add(self.problem.get_goal_state())
        all_states.append(self.problem.get_goal_state())

        while not frontier.empty():
            current_state_index = frontier.get()
            current_state = all_states[current_state_index]

            # Generate successor states
            successor_states = self.successor(current_state, current_state_index)

            for successor_state in successor_states:
                # If goal state is found, build solution and return
                if self.goal_test(successor_state):
                    result = self.build_solution(successor_state, all_states)
                    return result
                
                # Add successor state to frontier and visited set
                if successor_state not in visited:
                    total_state_index += 1
                    frontier.put(total_state_index)
                    visited.add(successor_state)
                    all_states.append(successor_state)

        return result

    def successor(self, state, current_state_index):
        result = []
        return result

    def goal_test(self, state):
        initial_state = self.problem.get_initial_state()

        # Check if all positive literals in state are present in initial state and negative literals are not present
        return state.get_positive_literals().issubset(initial_state.get_positive_literals()) and \
               state.get_negative_literals().isdisjoint(initial_state.get_positive_literals())

    def build_solution(self, state, all_states):
        result = []

        # Build solution by tracing back parent states from goal state
        while state.get_parent_index() != -1:
            result.append(state.get_action_name())
            state = all_states[state.get_parent_index()]

        return result