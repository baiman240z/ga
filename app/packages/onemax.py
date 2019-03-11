# -*- coding: utf-8 -*-
import random
import copy


class OneMax:
    def __init__(self, gene_size, item_size, selection_rate, mutation_rate):
        self.generation = 0
        self.gene_size = gene_size
        self.item_size = item_size
        self.selection_rate = selection_rate
        self.mutation_rate = mutation_rate
        self.items = []
        for i in range(item_size):
            item = []
            for j in range(gene_size):
                item.append(self.gene())
            self.items.append(item)

    @classmethod
    def gene(cls):
        return random.randint(0, 1)

    @classmethod
    def evaluate(cls, item):
        return sum(item)

    def cross(self):
        item1 = self.items[random.randint(0, len(self.items) - 1)]
        item2 = self.items[random.randint(0, len(self.items) - 1)]
        crossed = copy.deepcopy(item1)
        index1 = random.randint(0, len(crossed) - 1)
        index2 = random.randint(index1 + 1, len(crossed))
        crossed[index1:index2] = item2[index1:index2]
        return crossed

    def mutate(self, item):
        for i in range(len(item)):
            if random.random() < self.mutation_rate:
                item[i] = self.gene()

    def sort(self):
        sorter = []
        for item in self.items:
            sorter.append((self.evaluate(item), item))
        sorter.sort(reverse=True)
        self.items = []
        for evaluated, item in sorter:
            self.items.append(item)

    def select(self):
        self.sort()
        self.items = self.items[0:int(len(self.items) * self.selection_rate)]

    def cycle(self):
        self.generation += 1
        self.select()
        for i in range(self.item_size - len(self.items)):
            item = self.cross()
            self.mutate(item)
            self.items.append(item)
        print(str(self.generation) + u'世代')
        self.sort()
        for item in self.items:
            print(item)
