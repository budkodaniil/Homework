#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import ceil

number = int(input())
max_divisor = ceil(number / 2)

for divisor in range(1, max_divisor + 1):
    if number % divisor == 0:
        print(divisor)
print(number)

