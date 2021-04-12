# imports
from models import Node
import data

# utility function that ensures route is continuous and valid
def is_valid_route(route):
  for node in route[:-1:-1]:
    if (node.parent.station is not node.next.station):
      return False
  return True

# utility function which generates route list from final node
def generate_route(final_node):
  route = []
  current = final_node
  while (current is not None):
    route.append(current)
    current = current.parent_node
  if (is_valid_route(route)):
    return formatted(route[::-1])
  else:
    return []

# utility function to format route list for display purposes
def formatted(route):
  #   > FORMAT
  #   > [(station, arrival-time, departure-time, elapsed-time)]
  #   > sample route for banglore to gwalior:
  #   route = [
  #     ('BLR', -1, 14,  0),
  #     ('MUM', 10, 10, 20),
  #     ('GWL',  2, -1, 36)
  #   ]
  final = []
  path_length = len(route)
  for i in range(path_length):
    route.append(Node(0, 0))
    node = route[i]
    next_node = route[i+1]
    final.append((node.name, node.arrival_time, next_node.chosen_departure, node.cumulative))
  return final

# display utility for origin station
def start_card(station, arrive, depart, elapsed):
  print('+-------------------+')
  print(f'| {station} - start       |')
  if(arrive < 10): print(f'| arrival: 0{arrive}00     |')
  else: print(f'| arrival: {arrive}00     |')
  print('| elapsed: 0h       |')
  if(depart < 10): print(f'| departure: 0{depart}00   |')
  else: print(f'| departure: {depart}00   |')
  print('+-,-----------------+')
  print('  |')

# display utility for intermediate stops
def mid_card(station, arrive, depart, elapsed):
  print('  |')
  print('+-\'-----------------+')
  print(f'| {station}               |')
  if(arrive < 10): print(f'| arrival: 0{arrive}00     |')
  else: print(f'| arrival: {arrive}00     |')
  if(elapsed < 10): print(f'| elapsed: {elapsed}h       |')
  else: print(f'| elapsed: {elapsed}h      |')
  if(depart < 10): print(f'| departure: 0{depart}00   |')
  else: print(f'| departure: {depart}00   |')
  print('+-,-----------------+')
  print('  |')

# display utility for destination
def end_card(station, arrive, elapsed):
  print('  |')
  print('+-\'-----------------+')
  print(f'| {station} - end         |')
  if(arrive < 10): print(f'| arrival: 0{arrive}00     |')
  else: print(f'| arrival: {arrive}00     |')
  if(elapsed < 10): print(f'| elapsed: {elapsed}h       |')
  else: print(f'| elapsed: {elapsed}h      |')
  print('+-------------------+')

# utility function that takes a formatted route and displays it
def display_route(route):
  start_card(route[0][0], route[0][1], route[0][2], route[0][3])
  for station in route[1:-1]:
    mid_card(station[0], station[1], station[2], station[3])
  end_card(route[-1][0], route[-1][1], route[-1][3])

# utility function for the program menu
def menu():
  print()
  print('->> WELCOME TO ROUTE FINDER <<-')
  print('-------------------------------')
  print()
  print(data.map)
  print()
  depart = int(input('Depart from (index no): '))
  arrive = int(input('Arrive at (index no): '))
  start = int(input('Start journey at time (0 - 23 hours): '))
  print(f'Travelling from {data.cities[depart]} to {data.cities[arrive]}')
  print('Calculating Route...')
  print()
  return (depart, arrive, start)
