class Ticket:
  def __init__(self, source, destination):
    self.source = source
    self.destination = destination

def reconstruct_trip(tickets, length):
  routes = {}
  for ticket in tickets:
    routes[ticket.source] = ticket.destination
  route = []
  location = 'NONE'
  while True:
    location = routes[location]
    route.append(location)
    if location == 'NONE':
      break
  return route
