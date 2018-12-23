import os

robots = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
    	line_splitted = line.replace("\n","").split(",")
    	pos_x = line_splitted[0].replace("pos=<","")
    	pos_y = line_splitted[1]
    	pos_z = line_splitted[2].replace(">","")
    	radius = line_splitted[3].replace(" r=","")
    	robots.append([(int(pos_x), int(pos_y), int(pos_z)), int(radius)])
    	
max_radius = max([robot[1] for robot in robots])
strongest_robot = [robot for robot in robots if robot[1] == max_radius]
strongest_robot = strongest_robot[0]

in_range = 0
for robot in robots:
	taxcab = abs(robot[0][0] - strongest_robot[0][0]) + abs(robot[0][1] - strongest_robot[0][1]) + abs(robot[0][2] - strongest_robot[0][2])
	if taxcab <= strongest_robot[1]:
		in_range += 1
		
print(in_range)