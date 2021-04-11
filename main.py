# imports
from models import Node
import util
import ai
# from lib.models import Node

# driver code
(depart, arrive, start) = util.menu() # utility to run app menu
route = ai.find_route(depart, arrive, start) # model to generate best route
util.display_route(route) # utility to display routeclearr