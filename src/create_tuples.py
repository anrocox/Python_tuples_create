#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 3, 2014

@author: anroco

In python, how can you create a tuple?

En python, ¿como se puede crear una tupla?
'''

#create an empty tuple
tupla = ()
print (tupla)

#create a tuple with different data types
tupla = ('tuple', False, 2.2, 1)
print (tupla)

#create a tuple with numbers, notation without parenthesis
tupla = 3, 6, 2, 7, 1
print (tupla)

#create a tuple of one item, notation without parenthesis
tupla = 3,
print (tupla)

#create an empty tuple with tuple() function built-in python
tupla = tuple()
print (tupla)

#create a tuple from a iterable object
tupla = tuple([True, False])
print (tupla)
