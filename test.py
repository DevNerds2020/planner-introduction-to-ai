from Domains.LinkRepeatDomain import LinkRepeatDomain
from Problems.LinkRepeatProblem import LinkRepeatProblem
from Planners.BackwardPlanner import BackwardPlanner

# Create a BackwardPlanner object with a LinkRepeatProblem instantiated with a LinkRepeatDomain of size 1000
back = BackwardPlanner(LinkRepeatProblem(LinkRepeatDomain(1000)))

# Perform a search using the backward planner on the LinkRepeatProblem
print(back.search())
