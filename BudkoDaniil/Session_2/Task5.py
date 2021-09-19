#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list_of_dicts = [{"V":"S001", "VX": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique_values = set()

for dict_ in list_of_dicts:
    for value in dict_.values():
        unique_values.add(value)

print(unique_values)

