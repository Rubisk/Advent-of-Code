import copy
import itertools as it


wire_1 = [(a[0], int(a[1:])) for a in file.readline().split(",")]
wire_2 = [(a[0], int(a[1:])) for a in file.readline().split(",")]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)


class Line:
    def __init__(self, start_point, direction, length, wire_length_before):
        self._start = start_point
        self._direction = direction
        self._length = length
        self.wire_before = wire_length_before

    def direction(self):
        return self._direction

    def start(self):
        return self._start

    def end(self):
        return self._start + self._direction * self._length

    def intersect(self, other):
        assert type(other) == Line
        if self.direction().x != 0 and other.direction().x != 0:
            return
        if self.direction().y != 0 and other.direction().y != 0:
            return
        if self.direction().x == 0:
            hline = other
            vline = self
        else:
            hline = self
            vline = other
        x_low = min(hline.start().x, hline.end().x)
        x_high = max(hline.start().x, hline.end().x)
        y_low = min(vline.start().y, vline.end().y)
        y_high = max(vline.start().y, vline.end().y)

        if y_low <= hline.start().y <= y_high and x_low <= vline.start().x <= x_high:
            length_hline = hline.wire_before + abs(hline.start().x - vline.start().x)
            length_vline = vline.wire_before + abs(vline.start().y - hline.start().y)
            return Point(vline.start().x, hline.start().y), length_hline + length_vline
        return None


directions = {"R": Point(1, 0), "L": Point(-1, 0), "U": Point(0, 1), "D": Point(0, -1)}


def generate_lines(wire):
    lines = []
    position = Point(0, 0)
    total_length = 0
    for instruction in wire:
        direction = directions[instruction[0]]
        length = instruction[1]
        line = Line(position, direction, length, total_length)
        lines.append(line)
        position = position + direction * length
        total_length += length
    return lines


lines_1 = generate_lines(wire_1)
lines_2 = generate_lines(wire_2)

best = -1
for line1 in lines_1:
    for line2 in lines_2:
        intersection = line1.intersect(line2)
        if intersection:
            print(intersection, line1, line2)
            distance = intersection[1]
            if distance < best or best == -1:
                best = distance

print(best)

