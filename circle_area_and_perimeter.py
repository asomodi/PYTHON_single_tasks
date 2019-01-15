#!/usr/bin/env python
# coding: utf-8

# In[1]:


PI = 3.14

class Circle():
    def __init__(self,r):
        self.radius = r
    
    def area(self):
        return self.radius**2*PI
    
    def perimeter(self):
        return 2*self.radius*PI
    
NewCircle = Circle(5)

print(NewCircle.area())

print(NewCircle.perimeter())


# In[ ]:




