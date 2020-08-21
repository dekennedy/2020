#!/usr/bin/env python
# coding: utf-8

# In[31]:


PW= "jued"


lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

fourdigitcombo = [a+b+c+d for a in lowercase for b in lowercase for c in lowercase for d in lowercase]

#fourdigitcombo[:50] # Display first 50 ids

fourdigitcombo.index(PW)

#fourdigitcombo[:x]


# In[ ]:




