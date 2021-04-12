# imports
from models import Node
import util
import data

# modified a* to find route
def find_route(depart, arrive, start):
  # initalise problem
  current = Node(depart, arrive)
  current.arrival_time = start
  exploring = [current] # open set
  while (exploring):
    successors = current.successors()
    exploring.remove(current)
    for successor in successors:
      exploring.append(successor)
    current = exploring[0]
    for node in exploring:
      if (node.evaluated_value < current.evaluated_value):
        current = node
    if (current.station is arrive):
      return util.generate_route(current)