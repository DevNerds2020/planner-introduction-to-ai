# BackwardPlanner Implementation

## Class Attributes
- `problem`: an object of the `Problem` class that represents the planning problem instance.

## Constructor
The constructor initializes the `problem` attribute using the input problem instance.

## Public Methods
### `search()`
This method runs the backward search algorithm to find a sequence of actions that leads from the initial state to the goal state. It returns a list of action names in the order they need to be executed.

#### Method Variables:
- `total_state_index`: an integer variable that represents the unique identifier of each state generated during the search process.
- `result`: a list that stores the sequence of actions needed to reach the goal state, in case the planner finds a solution.
- `frontier`: a queue data structure that stores the indices of states that need to be expanded. It follows the First-In-First-Out (FIFO) rule, meaning that the first state that was added to the queue will be the first one to be explored.
- `visited`: a set that stores all the states that have already been visited during the search process. If a state has already been visited, it will not be added to either the frontier or `all_states` again. This helps to prevent the algorithm from revisiting the same states multiple times and getting stuck in a loop.
- `all_states`: a list that stores all the states that have been generated during the search process, including both the initial state and any successor states that were created. The index of each state in this list represents its unique identifier.

#### Method Steps
1. Check if the goal state is already reached. If so, return an empty result list.
2. Add the goal state to the frontier and visited set.
3. While the frontier is not empty, do the following:
    1. Remove the first state from the frontier.
    2. Generate its successor states using the `successor()` method.
    3. For each successor state, check if it is the goal state. If so, build the solution using the `build_solution()` method and return it.
    4. If the successor state has not been visited, add it to the `all_states` list, increment the `total_state_index`, and add its index to the frontier and visited set.

### `successor(state, current_state_index)`
This method generates the successor states of a given state by applying all applicable actions from the domain. It returns a list of successor states.

#### Method Parameters
- `state`: an object of the `State` class that represents the current state.
- `current_state_index`: an integer variable that represents the index of the current state in the `all_states` list.

#### Method Steps
1. Initialize an empty list called `result`.
2. For each action in the domain, do the following:
    1. Check if the action is relevant to the given state.
    2. If so, calculate the new state by applying the action's effects in reverse (i.e., regressing the state with the action).
    3. Set the parent index of the new state to the index of the current state.
    4. Append the new state to the result list.
3. Return the result list.

### `goal_test(state)`
This method checks if a given state is the goal state. It returns `True` if the state is the goal state and `False` otherwise.

#### Method Parameters
- `state`: an object of the `State` class that represents the state to be tested.

#### Method Steps
1. Get the initial state using the `get_initial_state()` method from the problem instance.
2. Check if all positive literals in the given state are present in the initial state and negative literals are not present.
3. Return `True` if the condition is met, and `False` otherwise.

### `build_solution(state, all_states)`
This method constructs the solution by tracing back parent states from the goal state. It returns a list of action names in the order they need to be executed.

#### Method Parameters
- `state`: an object of the `State` class that represents the goal state.
- `all_states`: a list that stores all the states that have been generated during the search process, including both the initial state and any successor states that were created. The index of each state in this list represents its unique identifier.

#### Method Steps
1. Initialize an empty list called `result`.
2. While the parent index of the given state is not -1, do the following:
    1. Get the action that led from the parent state to the current state using the `get_action()` method from the problem instance.
    2. Insert the action name at position 0 in the `result` list.
   