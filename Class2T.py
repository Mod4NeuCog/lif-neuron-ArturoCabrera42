# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:28:40 2022

@author: acabr
"""

letters = ['a', 'b', 'c'] #This is a comment
integers = [1,2,3]

def combine(a,b):
    c = []
    for i in range(3):
        c.append(a[i])
        c.append(b[i])
    return c

print(combine(letters, integers))