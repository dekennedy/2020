#!/usr/bin/env python
# coding: utf-8

# In[17]:



PW= "DELL(r"


case = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'


fourdigitcombo = [a+b+c+d+e+f for a in case for b in case for c in case for d in case for e in case for f in case]

#fourdigitcombo[:50] # Display first 50 ids

x = fourdigitcombo.index(PW)

#fourdigitcombo[:x]

print(x)


# In[23]:


fourdigitcombo[x:x+1]


# In[ ]:




