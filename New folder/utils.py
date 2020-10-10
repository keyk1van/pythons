#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""utils module"""
print("it is utils")


# In[2]:


def printer(x):
    print("printer")
    print(x)
    print("end")


# In[3]:


class Shape:
    def __init__(self, idd):
        self._idd = idd
    def __str__(self):
        return "Shape- " + self.idd
    
    @property
    def idd(self):
        print("idd method")
        return self._idd
    
    @idd.setter
    def idd(self, value):
        print("iddSet method")
        self._idd = value
    


# In[4]:


default_shape = Shape("square")

