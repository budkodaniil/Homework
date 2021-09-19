#!/usr/bin/env python
# coding: utf-8

# In[4]:


n=int(input('Please enter a positive integer between 1 and n : '))
for row in range(1, n + 1):
    print(*(f"{row*col:3}" for col in range(1, n + 1)))


# In[ ]:





# In[ ]:




