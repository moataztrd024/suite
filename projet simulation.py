#!/usr/bin/env python
# coding: utf-8

# In[15]:


#EX 1
from math import*
while 1:
    n=int(input("donner le terme du suite:"))
    if n>=0 :break
def suite(n):
    if n==0:
        return 3
    return sqrt(3*suite(n-1)+4)
print(suite(n))
print ("la valeur approchés de racine de 13 est la suite de terme 1:",suite(1))


# In[4]:


#2eme methode 
u=3
n=int(input("donner le nbr de terme"))
import math
for i in range(0,n):
    u=math.sqrt((3*u)+4)
print('u',n,'=',u)   


# In[2]:


#EX 2
from math import*
from matplotlib.pyplot import *
def suite(n):
    if n==0:
        return 3
    return sqrt(3*suite(n-1)+4)# la fonction qui donne les termes du suite par la récursivité
x=[j for j in range(1,10,1) ]
y=[suite(i) for i in range(1,10,1)]
plot(x,y,'ro',label="y=f(x)",linestyle="-")# représentation de la fct suite
xlabel("x")
ylabel("y")
grid()
legend()
title("Trajectoire de la suite")
axhline(y=4,color='gray')
show()
print("la suite U(n) tend vers la droite y=4 dans +oo ")


# In[ ]:





# In[ ]:




