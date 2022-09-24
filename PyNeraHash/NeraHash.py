# -*- coding: UTF-8 -*-

import hashlib
import random
import requests
import time
from threading import Thread


class NeraHash:
    def __init__(self) -> None:
        '''Инициализация переменных'''
        # uint32_t максимум
        self.int_max = 2 ** 32 
        self.results = []


    def int_to_hash(self, integer: int) -> str:
        '''Перевод числа в sha256 хэш'''
        _int = str(integer)
        return hashlib.sha256(_int.encode()).hexdigest()


    def find_hash(self, hash: str) -> None:
        '''Поиск числа соответствующего sha256 хэшу'''
        for i in range(0, self.int_max):
            if self.int_to_hash(i) == hash:
                self.results.append(i)
                break


    def find_all(self, max, hash_list: list) -> list:
        '''Поиск чисел соответствующих каждому sha256 хэшу в списке'''
        # Создание списка потоков
        th_hash = []

        self.int_max = 2 ** max
        
        # Создание потоков
        for i in range(len(hash_list)):
            th_hash.append(
                Thread(
                    target=self.find_hash, 
                    args=(hash_list[i],)
                    )
                )
            th_hash[i].start()
        
        # Ожидание завершения потоков
        for i in range(len(th_hash)):
            th_hash[i].join()
        
        return self.results

