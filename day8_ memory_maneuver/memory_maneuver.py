import os
from operator import itemgetter

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        data = line.replace('\n',"").split(" ")
        
nodes = list()
def parse_nodes(stream):
    node = [0]
    childs = int(stream.pop(0))
    metas = int(stream.pop(0))
    for child in range(0, childs):
        child_node = parse_nodes(stream)
        nodes.append(child_node)
    metadata = 0
    for meta in range(0, metas):
        metadata += int(stream.pop(0))
    node[0] = metadata
    return(node)

id = 0
while data:
    nodes.append(parse_nodes(data))

print(sum(node[0] for node in nodes))
