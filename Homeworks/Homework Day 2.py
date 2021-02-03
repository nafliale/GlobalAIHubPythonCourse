#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1

mylist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print (mylist)


# In[2]:


(mylist[5:], mylist[:5]) = (mylist[:5], mylist[5:])

print (mylist)


# In[4]:


#2

n=int(input("Enter a number: "))
num = 0

while num <=n:
  print(num)
  num +=2


# In[ ]:




