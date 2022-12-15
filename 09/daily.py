"""
    'It's your choice.  We can go to the donut shop or you can take a break.'
    --Ada
"""

from math import ceil
from collections import namedtuple


class Point:
    """simple cartesian coordinate class"""

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"{self.x}, {self.y}"
        # return "{}, {}".format(self.x, self.y)

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return self + -point

    def __lt__(self, other):
        return ((self.x < other.x) and (self.y < other.y))

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y and __o.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


Move = namedtuple("Move", ["direction", "magnitude"])


def main():
    """pass"""
    # test = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
    tail_moves = set()
    head = Point(0, 0)
    tail = Point(0, 0)
    with open("input.txt", "r", encoding="UTF-8") as file:
        file = [x.strip("\n") for x in file]
        # file = test
        for line in file:
            tmp = line.split()
            # movelist.append(Move(tmp[0], int(tmp[1])))
            movement = Move(tmp[0], int(tmp[1]))
            # move
            head, tail, tail_trail = travel(head, tail, movement)
            tail_moves |= tail_trail
    print(len(tail_moves))
    return len(tail_moves)


def travel(head, tail, movement):
    """move head, then tail, and log tail location - return end for head, tail, and list of coords

    Args:
        head (Point): cartesian coordinate
        tail (Point): cartesian coordinate
        movement (Move): int vector - (direction, distance)
    """
    tail_trail = set()
    vector = {"U": Point(0, 1), "D": Point(0, -1), "L": Point(-1, 0), "R": Point(1, 0)}[
        movement.direction
    ]
    print(vector, movement)
    for _ in range(1, movement.magnitude + 1):
        head += vector
        tail = check_tail(head, tail)
        print(f"{head=}, {tail=}")
        tail_trail.add(tail)
    return head, tail, tail_trail


def check_tail(head, tail):
    """
    Check positioning of tail after head move and update tail accordingly.
    """
    scalar = (a_dx := abs((diff_x := head.x - tail.x))), (a_dy := abs((diff_y := head.y - tail.y)))
    # no move
    if max(scalar) <= 1:
        return tail

    if diff_x >= 0:
        dx_mod = 1
    else:
        dx_mod = -1
    if diff_y >= 0:
        dy_mod = 1
    else:
        dy_mod = -1
    tail += Point(ceil(a_dx / 2)*dx_mod, ceil(a_dy / 2)*dy_mod)
    return tail


def borrowed():
    SEGMENT_COUNT = 9
    visited_points_list = list()
    head_moves = list()

    def is_adjacent(hx: int, hy: int, tx: int, ty: int) -> bool:
        if abs(hx - tx) <= 1 and abs(hy-ty) <=1:
            return True
        else:
            return False

    def move_tail(hx: int, hy: int, tx: int, ty: int) -> tuple():
        x_delta, y_delta = 0, 0

        if hx > tx:
            x_delta += 1
        elif hx < tx:
            x_delta -= 1

        if hy > ty:
            y_delta += 1
        elif hy < ty:
            y_delta -= 1

        return (x_delta, y_delta)


    with open('input.txt') as f:
        for line in [l.strip() for l in f]:
            dir, distance = line.split(' ')
            if dir == 'U':
                for _ in range(int(distance)):
                    head_moves.append((0, 1))
            elif dir == 'D':
                for _ in range(int(distance)):
                    head_moves.append((0, -1))
            elif dir == 'R':
                for _ in range(int(distance)):
                    head_moves.append((1, 0))
            elif dir == 'L':
                for _ in range(int(distance)):
                    head_moves.append((-1, 0))

    moves = head_moves
    for _ in range(SEGMENT_COUNT):
        visited_points = set()
        new_moves = list()
        visited_points.add((0,0))
        head_loc_x, head_loc_y, tail_loc_x, tail_loc_y = 0, 0, 0, 0
        for dx, dy in moves:
            head_loc_x += dx
            head_loc_y += dy
            if not is_adjacent(head_loc_x, head_loc_y, tail_loc_x, tail_loc_y):
                tail_delta = move_tail(head_loc_x, head_loc_y, tail_loc_x, tail_loc_y)
                tail_loc_x += tail_delta[0]
                tail_loc_y += tail_delta[1]
                new_moves.append(tail_delta)
                visited_points.add((tail_loc_x, tail_loc_y))
        visited_points_list.append(visited_points)
        moves = new_moves

    print(len(visited_points_list[-1]))




if __name__ == "__main__":
    # main()
    borrowed()
