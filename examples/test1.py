# -*- coding: UTF-8 -*-
import time
import random
from PyNeraHash.NeraHash import *


if __name__ == '__main__':
    '''Тестирование работы'''
    test_nh = NeraHash()
    hash_list = []
    # 16 бит на число 
    size = 16

    # Создаем список хэшей
    for i in range(64):
        hash_list.append(test_nh.int_to_hash(random.randint(0, 2 ** size)))
    
    # Вычисляем время за которое будет выполнен поиск
    start = time.time()
    print(test_nh.find_all(size, hash_list))
    print(time.time() - start)