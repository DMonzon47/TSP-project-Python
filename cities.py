#!/usr/bin/env python
# coding: utf-8

# In[14]:


import random as rand
import math


# In[15]:


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    road_map = []
    infile = open(file_name,"r")
    
    inline = infile.readlines()
    r_listt = [line.rstrip() for line in inline]
    listt = [(line.split('\t',4)) for line in r_listt]
    #r_listt = [line.rstrip() for line in inline]
    
    infile.close()   
    return listt

    #read_cities('city-data.txt')

    #for i in listt: 

#split split(/t) line where /t and create a 4 element tuple. Then add to roadmap.

# divide each string into 4 strings at "t"
# remove "n" ()
# tranform into tuple 
# add to listt
# return listt
road_map = read_cities('city-data.txt')
#print(road_map)


# In[20]:


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    
    road_map2 = [(i[0],i[1],round(float(i[2]),2),round(float(i[3]),2)) for i in road_map]
    road_map = road_map2
#round a float number not float a rounded string!!

    return road_map

road_map = print_cities(road_map)
print(road_map)


# In[22]:


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    
    #to check for empty road_map
    if len(road_map) == 0: 
        return "Empty 'road_map', please input correct format: [('state','city','latitude','longitude')]."
    
    #to check if longitude and latitude is in float() type or if list is in correct format. 
    for i in road_map:
        if type(i[2]) == str or type(i[3]) == str:
            return "Incorrect type/format. 'road_map' index[2] and [3] must be of float() types."
        if type(i[2]) == int or type(i[3]) ==int:
            return "Incorrect type/format. 'road_map' index[2] and [3] must be of float() types."      
        if len(i)!= 4: 
            return "List does not follow format [(state, city, latitude, longitude)]" #may not be needed. 
        
    total_distance = 0
    x1 = road_map[0][2] #float or str?
    y1 = road_map[0][3]
    
    x2 = 0
    y2 = 0

    for i in range(len(road_map)): 
        x2 = road_map[(i + 1) % len(road_map)][2]
        y2 = road_map[(i + 1) % len(road_map)][3]
        total_distance += math.sqrt((x1-x2)**2 + (y1-y2)**2)    
        x1 = x2
        y1 = y2
            
    return round(float(total_distance),2)

#print(compute_total_distance(road_map))
#road_map11 = [("Kentucky", "Frank", 38.197274, -84.86311),\
#                ("Delaware", "Dover", 39.161921, -75.526755),\
#                ("Minnesota", "Saint Paul", 44.95, -93.094)]
#road_map2 = []
#print(compute_total_distance(road_map11))
#print(compute_total_distance(road_map2))
#print(compute_total_distance(road_map))


# In[19]:


def swap_cities(road_map, index1, index2):

    #to check for empty road_map
    if len(road_map) == 0: 
        return "Empty 'road_map', please input correct format: [('state','city','latitude','longitude')]."
    
    #to check if longitude and latitude is in float() type and if road_map follows correct format. 
    for i in road_map:
        if type(i[2]) != float or type(i[3]) != float:
            return "Incorrect type. 'road_map' index[2] and [3] must be of float() types."
        if type(i[0]) != str or type(i[1]) != str:
            return "Incorrect type. 'road_map' index[0] and [1] must be of str() types."
        if len(i)!= 4: 
            return "List does not follow format [(state, city, latitude, longitude)]"
        
        
    #checks if inputted index1 and index2 is of int type.     
    if type(index1)== float or type(index2) == float :
        return "Input: index1 or index2 is of wrong type. Input must be an int."
            
    if type(index1) == str or type(index2) == str: 
        return "Input: index1 or index2 is of wrong type. Input must be an int."
            
    #print(str(road_map)+'\n')
    road_map [index1],road_map [index2] = road_map [index2],road_map [index1]
    new_road_map = road_map
    new_total_distance = compute_total_distance(new_road_map)
            #count+=1
        
    #print(str(road_map)+'\n')
        
    return (new_road_map, new_total_distance)
print(swap_cities(road_map,0,1))
#print('\n')
#print(road_map)

#print(road_map2)
#swap_cities = (swap_cities(print_cities,1,1))
#print(swap_cities)


# In[6]:


rm = [1,2,3,4,5,6,7,8,9]

def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    
    #road_map = [road_map[-1]] + road_map[:-1]
    #print(road_map)
    
    #ROAD MAP DOES NOT CHANGE!!FIX THIS!
#     road_map2=[]
#     for i in road_map: 
#         road_map2.append(i)
    if len(road_map) == 0: 
        return "Empty 'road_map', please input correct format: [('state','city','latitude','longitude')]."
    
    for i in road_map:
        if type(i[2]) != float or type(i[3]) != float:
            return "Incorrect type. 'road_map' index[2] and [3] must be of float() types."
        if type(i[0]) != str or type(i[1]) != str:
            return "Incorrect type. 'road_map' index[0] and [1] must be of str() types."
        if len(i)!= 4: 
            return "List does not follow format [(state, city, latitude, longitude)]"
     #road_map = road_map2
    
    road_map.insert(0,road_map.pop())
    
    return  road_map
#print(shift_cities(road_map))
#rm_map = shift_cities(rm)
#print(shift_cities(rm_map))
#print(shift_cities(rm_map))
#print(shift_cities(rm_map))


# def find_best_cycle(road_map):
#     """
#     Using a combination of `swap_cities` and `shift_cities`, 
#     try `10000` swaps/shifts, and each time keep the best cycle found so far. 
#     After `10000` swaps/shifts, return the best cycle found so far.
#     Use randomly generated indices for swapping.
#     """
# 
#     n = 10000
#     count = 0
#     new_cycle = 0
#     best_cycle = 1060.14
#     best_cycle_road_map = road_map
#     
#     while count!= n:
#         n1 = int((len(road_map)) * rand.random())
#         n2 = int((len(road_map)) * rand.random())
#         #print('start cycle: ' + str(best_cycle))
#         #print(str(best_cycle_road_map)+'\n')
#         a = swap_cities(best_cycle_road_map, n1, n2)
#         #print('swapped total: ' + str(a[1]))
#         #print(n1,n2)
#         #print (a[1])
#         #print(type(a[1]))
#         #print(type(a[0]))
#         
#         if a[1] < best_cycle: 
#             best_cycle = a[1]
#             best_cycle_road_map = a[0]
#             #print('\n'+'second cycle: ' + str(best_cycle))
#             #print('second cycle: ' + str(best_cycle_road_map)+ '\n')
#         #maybe check total distance again here above?: 
#         
#         b = shift_cities(best_cycle_road_map)
#         
#         #is this doing it properly and storing the right road_map?
#         #print('\n Shift_cycle: ' + str(b))
#         new_cycle = compute_total_distance(b)
#         print('shifted_new cycle: ' + str(new_cycle))
#         if new_cycle < best_cycle:
#             best_cycle = new_cycle
#             
#             best_cycle_road_map = b
#             #print(n1,n2,b, new_cycle)
#         count+=1
#         #print('count: ' + str(count))
#         #print(best_cycle_road_map)
#     return ('Total distance: ' + str(best_cycle)), best_cycle_road_map
# """store best cycle and best shift/swap, compare and replace. """
# t1 = find_best_cycle(road_map)
# print(t1)
# 
# """when swap cities is called, use the best cycle map!, not road_map!,  best cycle roapmap = roadmap!"""
# 
# """Works when swap cities allows index1==index2
#     is this also calculating [49] -> [0]???
#     FIX THIS - shift_cities not working properly in this function"""

# In[7]:


def find_best_cycle(road_map):

    n = 10000
    count = 0
    new_cycle = 0
    best_cycle = 1060.14
    best_cycle_road_map = road_map
    
    while count!= n:
        n1 = int((len(road_map)) * rand.random())
        n2 = int((len(road_map)) * rand.random())

        a = swap_cities(best_cycle_road_map, n1, n2)

        
        if a[1] < best_cycle: 
            best_cycle = a[1]
            best_cycle_road_map = a[0]

        
        b = shift_cities(best_cycle_road_map)
        

        new_cycle = compute_total_distance(b)
        
        if new_cycle < best_cycle:
            best_cycle = new_cycle
            
            best_cycle_road_map = b

        count+=1

    return ('Total distance: ' + str(best_cycle)), best_cycle_road_map
"""store best cycle and best shift/swap, compare and replace. """
#t1 = find_best_cycle(road_map)
#print(t1)


# In[13]:


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """

    for i in range(len(road_map)): 
        x1 = road_map[i][2]
        y1 = road_map[i][3]
        x2 = 0
        y2 = 0
        
        #print(x1, x2, y1,y2)
        x2 = road_map[(i + 1) % len(road_map)][2]
        y2 = road_map[(i + 1) % len(road_map)][3]
        #print(x2,y2)
        distance = round((math.sqrt((x1-x2)**2 + (y1-y2)**2)),2) 
        print('Distance between '+ str(road_map[i][1]) + ' -> ' + str(road_map[(i + 1) % len(road_map)][1]) +' is '+ str(distance))

    

    total_distance = compute_total_distance(road_map)    
    return ('Total distance: ' + str(total_distance))
        

print_map(road_map)


# In[48]:


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """

    file = input("Please input your file name: \n")
    
    road_map = read_cities(file)
    
    #print_roadmap = print_cities(road_map)
    
    road_map2 = print_cities(road_map)
    print('\n'+str(road_map2) +  '\n')
    
    best_cycle = find_best_cycle(road_map2)
    
    return (best_cycle)


#if _name_ == "_main_": #keep this in
#        main()
#        return "main name



# In[ ]:


print(main())


# In[23]:


def visualise(road_map):
    import tkinter as tk
    import matplotlib 
    import matplotlib.pyplot as plt
    from matplotlib.path import Path
    import matplotlib.patches as patches
    from matplotlib.pyplot import figure


# print(visualise(best_cycle_road_map))


# In[ ]:




