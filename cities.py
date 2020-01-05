#!/usr/bin/env python
# coding: utf-8

# In[32]:


import random as rand
import math


# In[2]:


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 
      [(state, city, latitude, longitude), ...] 
    Use this as your initial `road_map`, that is, the cycle 
      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    
    #road_map = []
    infile = open(file_name,"r")
    inline = infile.readlines()
    r_listt = [line.rstrip() for line in inline]
    road_map = [(line.split('\t',4)) for line in r_listt]
    
    
    infile.close()   
    return road_map

road_map = read_cities('city-data.txt')
print(road_map)


# In[24]:


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    
    #creates a list (road_map2) where each index has a list of: str,str,float,float.
    road_map2 = [(i[0],i[1],round(float(i[2]),2),round(float(i[3]),2)) for i in road_map]
    road_map = road_map2


    return (road_map)

print_cities(road_map)


# In[25]:


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    
    #to check for empty road_map
    if len(road_map) == 0: 
        return "Empty 'road_map', please input correct format: [('state','city','latitude','longitude')]."
    
    #to check if longitude and latitude is in float() type and if road_map follows correct format. 
    for i in road_map:
        if len(i)!= 4: 
            return "List does not follow format [(state, city, latitude, longitude)]"
        if type(i[2]) != float or type(i[3]) != float:
            return "Incorrect type/format. 'road_map' index[2] and [3] must be of float() types." 
        if type(i[0]) != str or type(i[1]) != str:
            return "Incorrect type/format. 'road_map' index[2] and [3] must be of str() types." 
        
    total_distance = 0
    #coordinates index from road_map. (floats, longitude and latitude)
    x1 = road_map[0][2] 
    y1 = road_map[0][3]
    
    x2 = 0
    y2 = 0

    for i in range(len(road_map)): 
        x2 = road_map[(i + 1) % len(road_map)][2]
        y2 = road_map[(i + 1) % len(road_map)][3]
        #compute distance between two cities and then add to 'total_distance', returns a float to 2 decimal places. 
        total_distance += math.sqrt((x1-x2)**2 + (y1-y2)**2)    
        x1 = x2
        y1 = y2
            
    return round(float(total_distance),2)

#print(compute_total_distance(road_map))


# In[47]:


def swap_cities(road_map, index1, index2):

    #if indices are same, return road_map. 
    if index1==index2:
        return road_map
    
    #checks if inputted index1 and index2 is of int type.     
    if type(index1)!= int or type(index2) != int:
        return "Input: index1 or index2 is of wrong type. Input must be an int."
    
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
            
    #create new_road_map from original road_map so that original is unaltered.
    new_road_map = [(i) for i in road_map]
    new_road_map [index1],new_road_map [index2] = new_road_map [index2],new_road_map [index1]
    
    new_total_distance = compute_total_distance(new_road_map)

    return (new_road_map, new_total_distance)
#print(swap_cities(road_map,0,1))


# In[27]:


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    
    #road_map = [road_map[-1]] + road_map[:-1]
    #print(road_map)
    
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
     
    #create new_road_map to leave original unaltered.
    new_road_map = [(i) for i in road_map]
    
    #shifts all elements in list to index+1. Last element becomes index[0] (start of list).
    new_road_map.insert(0,new_road_map.pop())
    
    return  new_road_map
#print(shift_cities(road_map))


# In[28]:


def find_best_cycle(road_map):
    """ 
    Using a combination of swap_cities and shift_cities, try 10000 swaps/shifts, 
    and each time keep the best cycle found so far. After 10000 swaps/shifts, return the best cycle found so far. 
    Use randomly generated indices for swapping. 
    """
    
    n = 10000
    count = 0
    new_cycle = 0
    best_cycle = 1060.14
    best_cycle_road_map = road_map 
    
    while count!= n:
        #generate random int to choose element from road_map. int range from 0 to len(road_map).
        n1 = int((len(road_map)) * rand.random())
        n2 = int((len(road_map)) * rand.random())

        a = swap_cities(best_cycle_road_map, n1, n2)

        #a[1] is total_distance computed for road_map. 
        if a[1] < best_cycle: 
            best_cycle = a[1]
            best_cycle_road_map = a[0] #a[0] is road_map generated for the cycle. 

        b = shift_cities(best_cycle_road_map)
        
        new_cycle = compute_total_distance(b)
        
        if new_cycle < best_cycle:
            best_cycle = new_cycle
            
            best_cycle_road_map = b

        count+=1

    return ('Total distance: ' + str(best_cycle)), best_cycle_road_map
#store best cycle and best shift/swap, compares and replaces. 


# In[29]:


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    
    ***need to fix this for new functions!!!!***
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
    print ('Total distance: ' + str(total_distance))
        
#print_map(road_map)


# In[45]:


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """

    file = input("Please input your file name: \n")
    
    #prevents function from crashing if file is not found. Prompts user to input file name again. 
    try:
        f = open(file, "r")
    except:
        print("There is no file named " + "'" + file + "'.")
        file = input("Please input your file name: \n")
    
    road_map = read_cities(file)
    
    #print_roadmap = print_cities(road_map)
    
    #assigned original road_map
    road_map2 = print_cities(road_map)
    print('\n'+str(road_map2) +  '\n')
    
    best_cycle = find_best_cycle(road_map2)
    
    print(best_cycle)

    if __name__ == "__main__": #keep this in
        main()
        return "main name"


# In[46]:

#main()


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





# In[ ]:




