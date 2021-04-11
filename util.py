from models import Node
import data

def is_valid_route(route):
  for node in route[:-1:-1]:
    if (node.parent.station is not node.next.station):
      return False
  return True

def formatted(route):
  final = []
  for node in route:
    final.append((node.name, node.arrival_time, node.chosen_departure, node.cumulative))
  return final

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

def end_card(station, arrive, elapsed):
  print('  |')
  print('+-\'-----------------+')
  print(f'| {station} - end         |')
  if(arrive < 10): print(f'| arrival: 0{arrive}00     |')
  else: print(f'| arrival: {arrive}00     |')
  if(elapsed < 10): print(f'| elapsed: {elapsed}h       |')
  else: print(f'| elapsed: {elapsed}h      |')
  print('+-------------------+')

def display_route(route):
  print()
  for st in route:
    print(st)
  print()
  start_card(route[0][0], route[0][1], route[0][2], route[0][3])
  for station in route[1:-1]:
    mid_card(station[0], station[1], station[2], station[3])
  end_card(route[-1][0], route[-1][1], route[-1][3])

def menu():
  print()
  print('->> WELCOME TO ROUTE FINDER <<-')
  print('-------------------------------')
  print(data.map)

  print()
  depart = int(input('Depart from (index no): '))
  arrive = int(input('Arrive at (index no): '))
  start = int(input('Start journey at time (0 - 23 hours): '))

  print(f'Travelling from {data.cities[depart]} to {data.cities[arrive]}')
  print('Calculating Route...')
  print()

  return (depart, arrive, start)
