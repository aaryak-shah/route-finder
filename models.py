# imports
import data

# node model definition
class Node:
  # init method
  def __init__(self, station, destination):
    self.station = station # --------------------- <int> station index
    self.name = data.cities[station] # ----------- <string> station codename
    self.destination = destination # ------------- <int> goal station index
    self.departures = data.departures[station] # - <list<tuple<int>>> departure times for next stops
    self.next_stop_costs = data.costs[station] # - <list<int>> path costs till next stops
    self.parent_node = None # -------------------- <Node> parent state node of self
    self.arrival_time = -1 # --------------------- <int> arrival time of agent at self
    self.chosen_departure = -1 # ----------------- <int> departure time for parent chosen by agent

    self.heuristic = data.heuristics[station][destination] # - h(n)
    self.cumulative = 0 # ------------------------------------ g(n)
    self.wait_time = 0 # ------------------------------------- w(n)
    self.evaluated_value = self.heuristic # ------------------ f(n)

  # successors generator method
  def successors(self):
    result = []
    for i in range(len(self.next_stop_costs)):
      if(self.next_stop_costs[i] > 0):
        # initialisation of successor node
        node = Node(i, self.destination)
        node.parent_node = self
        available_departures = node.parent_node.departures[node.station]
        wait_times = []
        # calculate wait times to this node
        for departure_time in available_departures:
          if(departure_time < node.parent_node.arrival_time):
            wait_times.append((24 - node.parent_node.arrival_time) + departure_time) # arrived after departure time, must wait for next day
          else:
            wait_times.append(departure_time - node.parent_node.arrival_time) # arrived before departure time, only wait till departure time
        node.wait_time = min(wait_times)
        min_index = wait_times.index(node.wait_time)
        node.chosen_departure = available_departures[min_index]
        node.arrival_time = (node.chosen_departure + node.parent_node.next_stop_costs[node.station]) % 24 # % 24 because time cannot exceed 23 hours
        node.cumulative = node.parent_node.cumulative + node.parent_node.next_stop_costs[node.station] + node.wait_time # calculate g(n)
        node.evaluated_value = node.cumulative + node.heuristic # calculate f(n)
        result.append(node)
    return result
