# imports
from models import Node
import util
import data

# modified a* to find route
def find_route(depart, arrive, start):
  current = Node(depart, arrive)
  current.arrival_time = start
  exploring = [current]
  while (exploring):
    if (data.log):
      print(f'\ncurrently at {current.name}/{current.evaluated_value} and exploring...')
      for node in exploring:
        print(f'  {node.name}/{node.evaluated_value}', end="")
      print()
    successors = current.successors()
    exploring.remove(current)
    for successor in successors:
      exploring.append(successor)
    current = exploring[0]
    for node in exploring:
      if (node.evaluated_value < current.evaluated_value):
        current = node
        if (data.log):
          print(f'  switching current to {current.name}/{current.evaluated_value} wtih at {current.arrival_time} and dt {current.chosen_departure}')
    if (current.station is arrive):
      return util.generate_route(current)