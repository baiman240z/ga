# -*- coding: utf-8 -*-
import random
import copy
import math


class Point:
    def __init__(self):
        self.x = random.random()
        self.y = random.random()


class Tsp:
    def __init__(self, gene_size, item_size, selection_rate, mutation_rate):
        self.generation = 0
        self.gene_size = gene_size
        self.item_size = item_size
        self.selection_rate = selection_rate
        self.mutation_rate = mutation_rate
        self.points = []
        for i in range(gene_size):
            self.points.append(Point())
        origin = list(range(gene_size))

        self.items = []
        for i in range(item_size):
            item = copy.deepcopy(origin)
            random.shuffle(item)
            self.items.append(item)

    def distance(self, point_no1, point_no2):
        p1 = self.points[point_no1]
        p2 = self.points[point_no2]
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def evaluate(self, item):
        distance = 0
        size = len(item)
        for start in range(size):
            end = start + 1
            if end == size:
                end = 0
            distance += self.distance(
                item[start],
                item[end]
            )
        return distance

    def cross(self):
        current_item_size = len(self.items)
        item1 = self.items[random.randint(0, current_item_size - 1)]
        item2 = self.items[random.randint(0, current_item_size - 1)]
        size = len(item1)
        crossed = [-1] * size
        index1 = random.randint(0, size - 1)
        index2 = random.randint(index1 + 1, size)
        crossed[index1:index2] = item2[index1:index2]
        for i in range(0, size):
            if crossed[i] == -1:
                for point_no in item1:
                    if point_no not in crossed:
                        crossed[i] = point_no
                        break
        return crossed

    def mutate(self, item):
        if random.random() < self.mutation_rate:
            size = len(item)
            index1 = random.randint(0, size - 1)
            index2 = random.randint(0, size - 1)
            if index1 > index2:
                index1, index2 = index2, index1
            index2 += 1
            item[index1:index2] = reversed(item[index1:index2])

    def sort(self):
        sorter = []
        for item in self.items:
            sorter.append((self.evaluate(item), item))
        sorter.sort()
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

    def top(self):
        self.sort()
        return self.items[0]
