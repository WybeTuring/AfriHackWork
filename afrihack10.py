def points(games):
    points = 0
    for x in games:
        if x[0] > x[2]:
            points = points + 3
        elif x[0] == x[2]:
            points = points +1
    return points