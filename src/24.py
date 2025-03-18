import networkx as nx
# import matplotlib.pyplot as plt

with open("./data/input_24.txt") as f:
    wires, connections = {}, []
    for line in map(str.strip, f):
        if ':' in line:
            w, val = line.split(':')
            wires[w] = int(val)
        elif ' -> ' in line:
            ins, to_wire = line.split(' -> ')
            connections.append((ins.split(), to_wire))

G = nx.Graph()
finished = False
while not finished:
    finished = True
    for (a, ins, b), to_wire in connections:
        if a not in wires or b not in wires:
            finished = False
        else:
            match ins:
                case('AND'):  wires[to_wire] = wires[a] & wires[b]
                case('OR'):   wires[to_wire] = wires[a] | wires[b]
                case('XOR'):  wires[to_wire] = wires[a] ^ wires[b]
            # ins_node = a + ins + b
            # G.add_node(a)
            # G.add_node(b)
            # G.add_node(to_wire)
            # G.add_node(ins_node)
            # G.add_edge(a, ins_node)
            # G.add_edge(b, ins_node)
            # G.add_edge(ins_node, to_wire)

z_keys = sorted((key for key in wires if key.startswith('z')), reverse=True)
part1 = ''.join(str(wires[key]) for key in z_keys)
print(int(part1, 2))


# for k in sorted(wires.keys()):
#     print(f"{k}: {wires[k]}")
#
# pos = nx.spiral_layout(G)
# plt.figure(figsize=(20, 20))
# nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold')
# plt.show()
