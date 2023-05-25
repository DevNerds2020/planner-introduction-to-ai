from Domains.TireDomain import TireDomain
from Problems.TireProblem import TireProblem
from Planners.BackwardPlanner import BackwardPlanner

back = BackwardPlanner(TireProblem(TireDomain()))
print(back.search())
