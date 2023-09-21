from statistics import mean as m
from statistics import pvariance as v


def mean(town: str, s: str) -> float:
    cities = {
        x.split(":")[0]: m(float(x.split()[1]) for x in x.split(":")[1].split(","))
        for x in (x for x in s.split("\n"))
    }

    if town in cities:
        return cities[town]

    return -1.0


def variance(town: str, s: str) -> float:
    cities = {
        x.split(":")[0]: v(float(x.split()[1]) for x in x.split(":")[1].split(","))
        for x in (x for x in s.split("\n"))
    }

    if town in cities:
        return cities[town]

    return -1.0
