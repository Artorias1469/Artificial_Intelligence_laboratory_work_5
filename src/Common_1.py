#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add_children(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, target_id, limit):
    """Ищет узел с заданным идентификатором target_id на ограниченной глубине limit."""
    if node is None:
        return False
    if node.value == target_id:
        return True
    if limit <= 0:
        return False

    # Рекурсивно ищем в дочерних узлах, уменьшая лимит глубины на 1
    return depth_limited_search(
        node.left, target_id, limit - 1
    ) or depth_limited_search(node.right, target_id, limit - 1)


def iterative_deepening_search(root, target_id, max_depth):
    """Основной метод для поиска узла с идентификатором target_id с итеративным углублением."""
    depth = 0
    while True:
        # Запускаем поиск с ограничением глубины depth
        found = depth_limited_search(root, target_id, depth)
        if found:
            return True
        depth += 1  # Увеличиваем глубину для следующей итерации
        if depth == max_depth:
            return False
        # При желании можно установить максимальный лимит для depth, чтобы избежать бесконечного цикла


def main():
    root = BinaryTreeNode(1)
    root.add_children(BinaryTreeNode(2), BinaryTreeNode(3))
    root.left.add_children(BinaryTreeNode(4), BinaryTreeNode(5))
    root.right.add_children(BinaryTreeNode(6), BinaryTreeNode(7))

    # Проверяем существование узлов с идентификаторами 5 и 10
    print(
        iterative_deepening_search(root, 5, 5)
    )  # Ожидаемый результат: True (узел существует)
    print(
        iterative_deepening_search(root, 10, 5)
    )  # Ожидаемый результат: False (узел не существует)


if __name__ == "__main__":
    main()