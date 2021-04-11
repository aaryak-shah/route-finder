from models import Node
import util

#   > (station, arrival-time, departure-time, elapsed-time)
#   > sample route for banglore to gwalior:
#   route = [
#     ('BLR', -1, 14,  0),
#     ('MUM', 10, 10, 20),
#     ('GWL',  2, -1, 36)
#   ]

# route generation function definition
def generate_route(final_node):
  route = []
  current = final_node
  while (current is not None):
    print((current.name, current.arrival_time, current.chosen_departure, current.cumulative))
    route.append(current)
    current = current.parent_node
  print()
  # for station in util.formatted(route[::-1]):
  #   print(station)
  if (util.is_valid_route(route)):
    return util.formatted(route[::-1])
  else:
    return []

'''
1.GENERATE A LIST of all possible next steps
  towards goal from current position

  current.successors

2.STORE CHILDREN in priority queue
  based on distance to goal, closest first

  aight this might be a lil' tough

3.SELECT CLOSEST child and REPEAT until goal reached or no more children
'''

def find_route(depart, arrive, start):
  current = Node(depart, arrive)
  current.arrival_time = start
  exploring = [current]

  while (exploring):
    print(f'\ncurrently at {current.name}/{current.evaluated_value} and exploring...')
    for node in exploring:
      print(f'  {node.name}/{node.evaluated_value}', end="")
    print()

    successors = current.successors()
    exploring.remove(current)

    for successor in successors:
      # print(f'for successor {successor.name}:')
      # available_departures = current.departures[successor.station]
      # print(f'  available departures = {available_departures}')
      # wait_times = []
      # for departure_time in available_departures:
      #   if(departure_time < current.arrival_time):
      #     wait_times.append((24 - current.arrival_time) + departure_time)
      #   else:
      #     wait_times.append(departure_time - current.arrival_time)
      # successor.wait_time = min(wait_times)
      # print(f'  wait times = {wait_times}, smallest of which is {successor.wait_time}')
      # min_index = wait_times.index(successor.wait_time)
      # current.chosen_departure = available_departures[min_index]
      # print(f'  chosen departure time from current = {current.chosen_departure}')
      # successor.parent_node = current
      # successor.arrival_time = (current.chosen_departure + current.next_stop_costs[successor.station]) % 24
      # print(f'  arrival time = {successor.arrival_time}')
      # successor.cumulative = current.cumulative + current.next_stop_costs[successor.station] + successor.wait_time
      # successor.evaluated_value = successor.cumulative + successor.heuristic
      exploring.append(successor)

    current = exploring[0]
    for node in exploring:
      if (node.evaluated_value < current.evaluated_value):
        current = node
        print(f'switching current to {current.name}/{current.evaluated_value} wtih at {current.arrival_time} and dt {current.chosen_departure}')
    
    if (current.station is arrive):
      return generate_route(current)