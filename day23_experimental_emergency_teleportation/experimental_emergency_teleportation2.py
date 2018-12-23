import os
import z3

robots = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
    	line_splitted = line.replace("\n","").split(",")
    	pos_x = line_splitted[0].replace("pos=<","")
    	pos_y = line_splitted[1]
    	pos_z = line_splitted[2].replace(">","")
    	radius = line_splitted[3].replace(" r=","")
    	robots.append((int(radius), int(pos_x), int(pos_y), int(pos_z)))
    	
def manhattan(ax, ay, az, bx, by, bz):
    diff_x = ax - bx
    diff_y = ay - by
    diff_z = az - bz
    dist = z3.If(diff_x >= 0, diff_x, -diff_x) + z3.If(diff_y >= 0, diff_y, -diff_y) + z3.If(diff_z >= 0, diff_z, -diff_z)
    return dist

solver = z3.Optimize()

best_x = z3.Int('best_x')
best_y = z3.Int('best_y')
best_z = z3.Int('best_z')
distance = z3.Int('distance')

z3_robots = []
for i, r in enumerate(robots):
    rr, rx, ry, rz = r
    robot = z3.Int('r{:4d}'.format(i))
    in_range = z3.If(manhattan(best_x, best_y, best_z, rx, ry, rz) <= rr, 1, 0)
    solver.add(robot == in_range)
    z3_robots.append(robot)

solver.add(distance == manhattan(best_x, best_y, best_z, 0, 0, 0))

solver.maximize(z3.Sum(*z3_robots))
solver.minimize(distance)
solver.check()

m = solver.model()
min_distance = m.eval(distance)
print(min_distance)