#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add1():
    """"
    Функция для добавления информации о новых рейсах
    """
    # Запросить данные о работнике.
    name = input("Фамилия и инициалы? ")
    post = input("знак зодиака? ")
    year = int(input("Год рождения? "))
    # Создать словарь.
    worker = {'name': name, 'знак зодиака': post, 'year': year}

    return worker