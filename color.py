import math

memory = {}


def train(values, labels):
    for i in range(0, len(values)):
        memory[values[i]] = labels[i]
    print("memory is " + str(memory))


def find_nearest_neighbor(rgb_tuple):
    distances = {}
    for i in memory:
        distances[i] = distance(i, rgb_tuple)
    print("distances is " + str(distances))
    sorted_distances = sorted(distances.items(), key=lambda b: b[1])
    print("sorted_distances is " + str(sorted_distances))
    return memory[sorted_distances[0][0]]


def distance(t1, t2):
    x_diff = t1[0] - t2[0]
    y_diff = t1[1] - t2[1]
    z_diff = t1[2] - t2[2]
    return math.sqrt(x_diff ** 2 + y_diff ** 2 + z_diff ** 2)


values = [(0, 0, 0), (255, 0, 0), (255, 127, 80), (220, 20, 60), (0, 255, 255), (169, 169, 169), (255, 140, 0), (255, 140, 0), (255, 140, 0), (255,99,71), (64,224,208), (0,255,127), (255,255,255)]

labels = ["black", "red", "coral", "crimson", "cyan", "dark grey", "dark orange", "deep pink", "fuchsia", "tomato", "Turquoise", "spring green", "white"]

train(values, labels)

print(find_nearest_neighbor((255, 102, 102)))



# print memory