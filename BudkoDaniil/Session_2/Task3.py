#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sequence = input().lower().split(',')
sorted_sequence = sorted(list(set(sequence)))
print(sorted_sequence)

