import os
from operator import itemgetter

data = list()
with open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r", encoding="utf8") as f:
    for line in f:
        data = line.replace('\n',"").split(" ")
        
nodes = list()
def parse_node(stream):
    node = 0
    childs = int(stream.pop(0))
    metas = int(stream.pop(0))
    if childs > 0:
        childs_metas = list()
        for child in range(0, childs):
            child_node = parse_node(stream)
            childs_metas.append(child_node)
        for meta in range(0, metas):
            child_index = int(stream.pop(0)) - 1
            if child_index < len(childs_metas):
                node += childs_metas[child_index]
        return(node)
    else:
        for meta in range(0, metas):
            node += int(stream.pop(0))
        return(node)

print(parse_node(data))