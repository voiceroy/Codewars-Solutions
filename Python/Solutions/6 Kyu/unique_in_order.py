from itertools import groupby
from typing import Iterable


def unique_in_order(iterable: Iterable) -> list:
    return [list(grp)[0] for _, grp in groupby(iterable)]
