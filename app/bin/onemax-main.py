# -*- coding: utf-8 -*-
from onemax import OneMax

one_max = OneMax(
    gene_size=10,
    item_size=10,
    selection_rate=0.5,
    mutation_rate=0.5,
)

for i in range(0, 100):
    one_max.cycle()
