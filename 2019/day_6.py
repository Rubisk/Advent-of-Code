class Planet(object):

    def __init__(self, tag):
        self._tag = tag
        self.children = []
        self._orbits = -1
        self.parent = None

    def update_orbits(self, orbits):
        self._orbits = orbits
        for c in self.children:
            c.update_orbits(orbits + 1)

    def get_orbits(self):
        assert self._orbits != -1
        return self._orbits

    def __repr__(self):
        return "<" + self._tag + ">"


planets = {}


def find_planet(tag):
    if tag not in planets.keys():
        planets[tag] = Planet(tag)
    return planets[tag]


for line in open("input_6.txt").readlines():
    parent, child = line[:-1].split(")")
    parent_planet = find_planet(parent)
    child_planet = find_planet(child)
    child_planet.parent = parent_planet
    parent_planet.children.append(child_planet)


planets["COM"].update_orbits(0)

total_orbits = 0
for planet in planets.values():
    total_orbits += planet.get_orbits()


def find_path(start, end):
    path = [start]
    while path[-1] != end:
        path.append(path[-1].parent)
    return path


san_path = find_path(planets["SAN"], planets["COM"])
you_path = find_path(planets["YOU"], planets["COM"])

i = 0
while you_path[i] not in san_path:
    i += 1
    if you_path[i] in san_path:
        print(san_path.index(you_path[i]) + i - 2)
