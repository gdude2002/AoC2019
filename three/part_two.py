from dataclasses import dataclass
from typing import List, Set


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


def distance(left: Point, right: Point):
    return abs(left.x - right.x) + abs(left.y - right.y)


all_wires: List[List[str]]
root_point = Point(0, 0)


with open("data.txt") as fh:
    all_wires = [x.split(",") for x in fh.readlines() if x.strip()]


def find_points(wires: List[List[str]]):
    points: List[List[Point]] = []
    intersections: List[Point] = []

    for wire in wires:
        print(f"Instructions in wire: {len(wire)}")
        point_list = [root_point]

        for instruction in wire:
            direction, amount = instruction[0], int(instruction[1:])

            for _ in range(amount):
                last_point = point_list[-1]

                if direction == "R":
                    point = Point(last_point.x + 1, last_point.y)
                elif direction == "L":
                    point = Point(last_point.x - 1, last_point.y)
                elif direction == "U":
                    point = Point(last_point.x, last_point.y + 1)
                elif direction == "D":
                    point = Point(last_point.x, last_point.y - 1)
                else:
                    print(f"Unknown instruction: {direction} {amount}")
                    continue

                point_list.append(point)
        points.append(point_list)

    return points


all_points = find_points(all_wires)
point_sets: List[Set[Point]] = []

for point_set in all_points:
    print(f"Points in wire: {len(point_set)}")

    point_sets += [set(point_set)]

intersections = set()

for point_set in point_sets:
    if len(intersections) == 0:
        intersections = point_set
        continue

    intersections = intersections & point_set


def steps(point, *wires):
    total = 0

    for wire in wires:
        for wire_point in wire:
            if point != wire_point:
                total += 1
            else:
                break

    return total


cur_distance = None
cur_point = None

for point in intersections:
    if point == root_point:
        continue

    if cur_distance is None:
        cur_distance = steps(point, *all_points)
        cur_point = point
        continue

    dist = steps(point, *all_points)

    if dist < cur_distance:
        cur_distance = dist
        cur_point = point


print(f"Point: {cur_point}, steps: {cur_distance}")
