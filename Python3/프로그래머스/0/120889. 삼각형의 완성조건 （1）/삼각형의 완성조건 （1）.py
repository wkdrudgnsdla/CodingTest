def solution(sides):
    answer = 0
    big_sides = 0
    for i in sides:
        if big_sides < i:
            big_sides = i
    sides.remove(big_sides)
    return 1 if sides[0] + sides[1] > big_sides else 2