
# coding: utf-8

# In[1]:


def generate_sentences(list_s, list_v, list_o):
    for s in list_s:
        for v in list_v:
            for o in list_o:
                print(s + " " + v + " " + o)

subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

generate_sentences(subjects, verbs, objects)

