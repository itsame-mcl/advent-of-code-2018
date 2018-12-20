import os
import sre_yield
regex = ""

# with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
#    for line in f:
#        regex = line.replace("\n","").replace("^","").replace("$","")

regex = "ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))"
routes = sre_yield.AllMatches(regex)

rooms = set()
doors = set()
rooms.add((0,0))
for route in routes:
    walker = (0,0)
    for char in route:
        if char == "N":
            go_to = (walker[0], walker[1] + 1)
            doors.add((walker, go_to))
            walker = go_to
        elif char == "S":
            go_to = (walker[0], walker[1] - 1)
            doors.add((go_to, walker))
            walker = go_to
        elif char == "E":
            go_to = (walker[0] + 1, walker[1])
            doors.add((walker, go_to))
            walker = go_to
        elif char == "W":
            go_to = (walker[0] - 1, walker[1])
            doors.add((go_to, walker))
            walker = go_to
        rooms.add(walker)