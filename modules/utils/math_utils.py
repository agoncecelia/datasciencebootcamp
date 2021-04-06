from operator import attrgetter

def max_average(l):
    return max(l, key=attrgetter("average"))