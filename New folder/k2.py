# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:36:19 2020

@author: Keyvan
"""
import functools
class Calculator:
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y
    def mul(self, x, y):
        return x * y
    def div(self, x, y):
        return x / y
    
    def __enter__(self):
        print("salam")
        return self
    def __exit__(self, *args):
        print("bye")
        if args[0] is ZeroDivisionError:
            print("zero")
            return True

class Distance:
    def __init__(self, d):
        self.value = d
        
    def __add__(self, other):
        return Distance(self.value + other.value)
    
    def __sub__(self, other):
        return Distance(self.value - other.value)
    
    def __str__(self):
        return "Distance [" + str(self.value) + "]"
    
class MessageWriter:
    def __init__(self, filename):
        self.filename = filename
        
    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file
    
    def __exit__(self, *args):
        self.file.close()
    
class animal:
    def move(self):
        pass
    
class dog(animal):
    def move(self):
        print("walking")
        
class fish(animal):
    def move(self):
        print("swiming")

class Descriptor:
    def __init__(self):
        self.__fuel = 0
    
    def __get__(self, ins, owner):
        return self.__fuel
    def __set__(self, ins, va):
        if isinstance(va, int):
            self.__fuel = va
        else:
            raise TypeError

class Car:
    num_tyres = 4
    
    def __init__(self, name, color):
        self.name = name
        self.color = color

def logger(func):
    @functools.wraps(func)
    def inner(x, y):
        print("calling", func.__name__)
        val = func(x, y)
        print("called", func.__name__)
        return val
    return inner

def singleton(cls):
    print("salam")
    instance = None
    def get_instance():
        nonlocal instance
        print("ins", instance)
        if instance is None:
            instance = cls()
        return instance
    return get_instance

def genfunc(i):
    print("start")
    value = 0
    while value < i:
        print("first line of while")
        yield value
        print("first line after yield")
        value += 2
        print("last line of while")
    print("done")
    
class iteclass:
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        print("sa")
        if self.i < 4:
            r = self.i
            self.i += 1
            
        else: raise StopIteration
    
def coro(name):
    print("start")    
    while True:
        var = (yield)
        if var == name:
            print("Yes")
        elif var == "end":
            break
    print("out of while")
    vb = (yield)
    print("last var ", vb)
    
        

 


            



                