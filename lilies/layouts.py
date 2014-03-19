from __future__ import print_function
from .lilystring import grow, wilt


def columnify(iter, cols=0, width=80, justify='left', spacing=3):
    iter = map(grow, iter)
    if cols == 0:
        cols = width // (max(map(len, iter)) + spacing)
    if cols == 0:
        cols = 1
    colsize = width // cols
    resized = map(lambda s: s.resize(colsize - spacing, justify, add_elipsis=True, fillchar=' '), iter)
    num_per_column = len(iter) // cols + 1
    groups = []
    for i in range(num_per_column):
        groups.append(resized[i::num_per_column])
    for group in groups:
        s = group[0]
        for q in group[1:]:
            s += grow(' ' * spacing)
            s += q
        print(s)