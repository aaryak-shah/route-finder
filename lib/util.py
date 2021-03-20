from lib import data

def start_card(station, depart, elapsed):
  print('+-------------------+')
  print(f'| {station} - start       |')
  if(depart < 10): print(f'| departure: 0{depart}00   |')
  else: print(f'| departure: {depart}00   |')
  print('| elapsed: 0h       |')
  print('+-,-----------------+')
  print('  |')

def mid_card(station, arrive, depart, elapsed):
  print('  |')
  print('+-\'-----------------+')
  print(f'| {station}               |')
  if(arrive < 10): print(f'| arrival: 0{arrive}00     |')
  else: print(f'| arrival: {arrive}00     |')
  if(depart < 10): print(f'| departure: 0{depart}00   |')
  else: print(f'| departure: {depart}00   |')
  if(elapsed < 10): print(f'| elapsed: {elapsed}h       |')
  else: print(f'| elapsed: {elapsed}h      |')
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
  start_card(route[0][0], route[0][2], route[0][3])
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
  start = int(input('Start journey at (0 - 23) hours: '))

  print(f'Travelling from {data.cities[depart]} to {data.cities[arrive]}')
  print('Calculating Route...')
  print()

  return (depart, arrive, start)
