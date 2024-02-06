#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def select(command, workers):
    """""
    Функция для получения номера года
    """
    # Разбить команду на части для выделения номера года.
    parts = command.split(' ', maxsplit=1)
    # Проверить сведения работников из списка.
    count = 0

    for worker in workers:
        if today.year - worker.get('year', today.year) >= period:
            count += 1
    print(
        '{:>4}: {}'.format(count, worker.get('name', ''))
    )

    # Если счетчик равен 0, то работники не найдены.

    if count == 0:
                print("информация не найдена.")