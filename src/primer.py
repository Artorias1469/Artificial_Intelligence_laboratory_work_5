#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Практическая реализация поиска с итеративным углублением

import sys


def depth_limited_search(problem, limit):
    # Реализация функции depth_limited_search
    pass


cutoff = "cutoff"


def iterative_deepening_search(problem):
    "Выполняем поиск с ограничением глубины с возрастающими пределами глубины"
    for limit in range(1, sys.maxsize):
        result = depth_limited_search(problem, limit)
        if result != cutoff:
            return result
    return None  # Возвращаем None, если решение не найдено