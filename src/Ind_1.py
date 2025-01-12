#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

class FileNode:
    def __init__(self, path):
        self.path = path
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        for child in args:
            self.add_child(child)

    def __repr__(self):
        return f"<{self.path}>"


def build_file_tree(root_path, max_depth=20, current_level=1):
    """
    Построение дерева файловой системы до заданной глубины.
    """
    if current_level > max_depth:
        return None

    root_node = FileNode(root_path)
    try:
        for entry in os.scandir(root_path):
            try:
                if entry.is_dir():
                    child = build_file_tree(entry.path, max_depth, current_level + 1)
                    if child:
                        root_node.add_child(child)
                else:
                    root_node.add_child(FileNode(entry.path))
            except (FileNotFoundError, PermissionError):
                # Пропускаем недоступные или удаленные файлы/папки
                continue
    except (FileNotFoundError, PermissionError):
        # Пропускаем недоступные или удаленные директории
        pass
    return root_node


def find_large_file(node, min_size=1 * 1024**3, min_depth=5, current_level=1):
    """
    Рекурсивный поиск первого файла, удовлетворяющего условиям.
    """
    if current_level < min_depth:  # Пропускаем узлы до минимального уровня
        for child in node.children:
            if isinstance(child, FileNode):
                result = find_large_file(child, min_size, min_depth, current_level + 1)
                if result:
                    return result
        return None

    # Проверяем файлы на текущем уровне
    for child in node.children:
        if not isinstance(child, FileNode):  # Пропускаем недействительные узлы
            continue

        try:
            if os.path.isfile(child.path) and os.path.getsize(child.path) > min_size:
                return child.path
        except (OSError, PermissionError):
            continue

    # Рекурсивно проверяем дочерние узлы
    for child in node.children:
        if isinstance(child, FileNode):
            result = find_large_file(child, min_size, min_depth, current_level + 1)
            if result:
                return result

    return None


def main():
    # Укажите начальную директорию для поиска
    root_directory = "D:\Virtual Machines"  # Замените на нужный путь
    max_depth = 20  # Максимальная глубина обхода
    min_size = 1 * 1024**3  # Минимальный размер файла (1 ГБ)
    min_depth = 5  # Минимальная глубина поиска

    print("Строим дерево файлов...")
    file_tree = build_file_tree(root_directory, max_depth)

    if not file_tree:
        print("Не удалось построить дерево. Проверьте путь.")
        return

    print("Ищем файл...")
    large_file = find_large_file(file_tree, min_size, min_depth)

    if large_file:
        print(f"Найден файл: {large_file}")
    else:
        print("Файл размером более 1 ГБ на глубине не менее 5 уровней не найден.")

if __name__ == "__main__":
    main()
