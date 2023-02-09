#!/usr/bin/env python
# coding: utf-8

# # Assignment_02-02-2023

# ## 1. WHAT ARE THE CHARACTERISTICS OF TUPLES?IS TUPLES MUTABLE?
# 
# ### Ans:-
#            Tuples Characteristics described in given bleow:-
#            
#            1.Immutable : Tuples are immutable,which means the elements inside a tuples can not be altered
#                           once they assigned.
#            
#            2.Ordered   :  The elements in a tuple have a defined order and can be accessed through their index.
#            
#            3.Iterable  :  Tuples can be iteraed over,just like list.
#            
#            4.Parantheses: Tuples are defined using parantheses (),where as lists  are defined using squre bracket [].
#            
#            5.fixed Size : The size of tuple is fixed and cannot be changed dynamically like list.
#            
#            6.Supports indexing and Slicing: Tuples can be indexed and Sliced like list.
# 

# ## 2. What are the two tuples method in python? Give an example of each method. Give a                  reason why tuples have only two in-built methods as compared to list.
# 
# ### Ans:-
#               The two in-built methods for tuples in Python are:
#               
#               1.count() method: This method returns the number of times a specific element appears in a tuple.
#               
#               EXAMPLE:-
#                   sam= (1,2,3,[3,9,5],"Manas")
#                   sam.count(2)
#                   1
#               2.index() method: This method return the index of the first occurance of a specific element in the tuples.
#               
#               EXAMPLE:-
#                    sam1=(1,2,3,4,2,3,1,5,7,9)
#                    sam1.index(5)
#                    7
# 
#              Tuples are two in-built methods compared to lists because tuples are meant to be simple,efficient and 
#              light weight data structures for storing a fixed mumber of items.
#              The immutability of tuples make it less felxible compared to lists and the two methods are enough for 
#              most use cases.
#              

# ## 3. Which collection datatype in python do not allow duplicate item? Write a code using a set to remove duplicates from the given list.
# 
# ### Ans:-
#            The collection datatype in Python that does not allow duplicate items is "set".
#            

# In[1]:


## Write a code using a set to remove duplicates from the given list.
l=[1,1,1,2,1,3,1,4,2,1,2,2,2,3,2,4,3,1,3,2,3,3,3,4,4,1,4,2,4,3,4,4]
print(f"Original List :-{l}")
result=set(l)
print(f"List after removing dupicate elements:-{result}")


# ## 4. Expain the difference between the union() and update() methods for a set. Give an example of each method.
# 
# ### Ans.
#           The union() method is used to combine two sets into a single set. It returns a new set that contains all 
#           the elements from both sets, without any duplicates.
#           
#           The update() method, on the other hand, modifies an existing set by adding the elements from another set to it.
#           If the elements are already present in the set, the update method does not add duplicates.
#           
# 

# In[2]:


## Example of set.union()

set1= {1,2,3,4,5,"Manas",("sunandini")}
set2= {10,20,"sejal"}
set3= set1.union(set2)
print(set3)


# In[3]:


set3


# In[4]:


set1


# In[5]:


## Example of set,update()

set1.update(set2)
print(set1)


# In[6]:


set1


# ### 
#      The above example as you can see, the union() method return a new set [set3] that contains all the elements from both 
#      set1 and set2.
#                                        the update() method modifies set1 directly adding all the elements from set2 to it. 

# ## 5. what is a dictionary ? Give an example . Also state whether a dictionary is order or unordered.
# 
# ### Ans.
#           A dictionary is a data structure in Python that is used to store key-value pairs. The keys are unique and 
#           are used to access the corresponding values. In Python, dictionaries are declared using curly braces {}.
# 

# In[7]:


## One Example of a dictionary.

Monumnets = {'Delhi': 'LalQuila','Mumbai':'Gate way of India','Agra':'Taj Mahal','Jaipur':'Jal Mahal','bhopal':'upper lake'}
print(Monumnets)


# In[8]:


Monumnets.pop('bhopal')


# In[9]:


Monumnets


# #### 
#              Dictionaries in Python are unordered. This means that the elements in a dictionary do not have a defined order
#              and can be stored in any order. When you retrieve elements from a dictionary, they may not be in the same 
#              order as they were stored. However, the key-value association remains constant and you can use the keys 
#              to access the values.

# ## 6. Can we create a nested dictionary ? If so, Please give an example by creating simple one-level nested dictionary.
# 
# ### Ans.
#          Yes, you can create a nested dictionary in Python. A nested dictionary is a dictionary that contains 
#          another dictionary as its value. This allows you to create a hierarchical structure to organize your data.

# In[10]:


## an example of a simple one-level nested dictionary:
student= {'Manas':{'age': 41,'Course':'Data Science Master'}}
print (student)


# In[11]:


student['Manas']['age']


# In[12]:


student['Manas']['Course']


# ### 
#            To access the values in the inner dictionary, you can use the keys of the outer dictionary to 
#            access the inner dictionary, and then use the keys of the inner dictionary to access the values.

# ## 7. Using setdefault() method, create key named topics in the given dictionary and also add the value of the key as this list['Python','Mechine Learning','Deep Learning']
# 
# ### Ans.
#           The setdefault() method is used to add a new key to a dictionary with a default value if the 
#           key does not already exist in the dictionary.

# In[13]:


dict1={}
dict1.setdefault("language","Python")
dict1.setdefault("course","Machine Learning")
dict1.setdefault("Specialization","Deep Learning")
print(dict1)


# ## 8. What is the three view objects in dictionary ? Use three in-built methods in python to display . These three view objects for the given dictionary.
# 
# ### Ans.
#           In Python, dictionaries have three view objects: keys(), values(), and items().
# 
#          1.keys() returns a view object that displays a list of all the keys in the dictionary.
# 
#          2.values() returns a view object that displays a list of all the values in the dictionary.
# 
#          3.items() returns a view object that displays a list of all the key-value pairs in the dictionary as tuples.

# In[14]:


##  Example of view Object Dictionary

dict1={'Sport':'Cricket','Team':['India','Australia','England','South Africa','Sri Lanka','New Zeland']}
print(dict1)


# In[15]:


keys= dict1.keys()
print("Keys",keys)


# In[16]:


values = dict1.values()
print("Values",values)


# In[17]:


items = dict1.items()
print("Items",items)


# In[18]:


## Second Example of view Object Dictionary

persoan1={"name":"Manaspandey","age":"41","course":"Data Science Master"}
print(persoan1)


# In[19]:


keys= persoan1.keys()
print("Keys",keys)


# In[20]:


values = persoan1.values()
print("Values",values)


# In[21]:


items = persoan1.items()
print("Items",items)

