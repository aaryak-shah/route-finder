from lib import data

class Node:
  def __init__(self, station, destination):
    self.station = station
    self.destination = destination
    self.name = data.cities[station]
    self.departures = data.departures[station]
    self.next_stop_costs = data.costs[station]
    self.heuristic = data.heuristics[station][destination]

  def successors(self):
    return []

def generate_route(final):
  return []

def best(exploring):
  return Node(0, 0)

def find_route(depart, arrive, start):
  final = [Node(depart, arrive)]
  explored = []
  exploring = [Node(depart, arrive)]
  while exploring:
    best_node = best(exploring)
    if(best_node.station == arrive):
      final.append(best_node)
      break
    else:
      

  return generate_route(final)

#   route = [
#     > (station, arrival-time, departure-time, elapsed-time)
#     > sample route for banglore to gwalior:
#     ('BLR', -1, 14,  0),
#     ('MUM', 10, 10, 20),
#     ('GWL',  2, -1, 36)
#   ]