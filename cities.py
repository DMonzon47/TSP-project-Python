#!/usr/bin/env python
# coding: utf-8

# In[23]:


"""
The following need to be imported inorder to use the visualisation functions:
import matplotlib 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import random as rand
import math
"""


# In[24]:


import random as rand
import math


# In[25]:


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 
      [(state, city, latitude, longitude), ...] 
    Use this as your initial `road_map`, that is, the cycle 
      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    infile = open(file_name,"r")
    inline = infile.readlines()
    r_listt = [line.rstrip() for line in inline]
    listt = [(line.split('\t',4)) for line in r_listt]
    infile.close() 
    
    #converts listt into road_map with types for each element as: str,str,float,float.
    road_map = [(i[0],i[1], float(i[2]),float(i[3])) for i in listt]   
    return road_map


# In[26]:


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    
    #rounds coordinates to 2 decimal places. 
    road_map2 = [(i[0],i[1],round(i[2],2),round(i[3],2)) for i in road_map]
    road_map = road_map2
    
    return (road_map)

#print_cities(road_map)


# In[27]:


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


# In[28]:


def swap_cities(road_map, index1, index2):
    
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


# In[29]:


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
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


# In[30]:


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


# In[31]:


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
        print('Distance between '+ str(road_map[i][1]) + ' -> ' + str(road_map[(i + 1) % len(road_map)][1])+               ' is '+ str(distance))
        
    total_distance = compute_total_distance(road_map)    
    print ('Total distance: ' + str(total_distance))


# In[38]:


#longitude = x, latitude = y
def visualise(road_map):

    import matplotlib 
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import figure
    
    longitude_x = [(i[3]) for i in road_map]
    latitude_y = [(i[2]) for i in road_map]
    annotates1 = [(i[1]) for i in road_map]
    
    #adds coordinates for index[0] at end of list to plot onto scatter: allows line to loop back to start.
    longitude_x.append(road_map[0][3])
    latitude_y.append(road_map[0][2])
    
    
    #adjust lat and long to min and max of road_map with +- 5 allowance.
    y_min = min(latitude_y) -5
    y_max = max(latitude_y) + 5
    x_min = min(longitude_x) - 5
    x_max = max(longitude_x) + 5
    
    a = compute_total_distance(road_map)
    
    plt.figure(figsize = (16,12))
    plt.scatter(longitude_x, latitude_y)
        
    #uses label/key to display total_distance of road_map
    plt.plot(longitude_x, latitude_y, color = 'green', lw = 0.5, label = 'Total distance: ' + str(a))
    
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(loc="upper right", prop = {'size':14})
    
    #plt.ylim(-90, 90)
    #plt.xlim(-180,180)
    
    #adjust lat and long scale to min and max of road_map with +- 5 allowance for better visualisation.
    plt.ylim(y_min, y_max)
    plt.xlim(x_min,x_max)
    
    #add grid lines to plot
    plt.rc('grid', linestyle="dashed", color='grey')
    plt.grid(True)
    
        
    #annotates each plot with city and order plotted. Starting from 0.
    for i,txt in enumerate(annotates1): 
        plt.annotate((i,annotates1[i]),(longitude_x[i],latitude_y[i]))

    plt.title("TSP: best cycle road map visualiser.")

    plt.show()


# In[39]:


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    file = input("Please input your file name, or type 'None' to exit: \n")
    
    if file == 'None':
        return  "Goodbye!"
    
    #prevents function from crashing if file is not found. Prompts user to input file name again. 
    try:
        f = open(file, "r")
    except:
        print("There is no file named " + "'" + file + "'.")
        file = input("Please input your file name: \n")
        if file == 'None':
            return ("Goodbye!")
        
    road_map = read_cities(file)
    
    #assigned original road_map
    road_map2 = print_cities(road_map)
    print('Original road_map: \n'+str(road_map2) +  '\n')
    
    best_cycle = find_best_cycle(road_map2)
    
    print("Best cycle: \n" + str(best_cycle))
    #print_map(best_cycle[1])
    
    visualise(best_cycle[1])
    
    if __name__ == "__main__": #keep this in
        main()
        return "main name"


# In[40]:


#main()


# def main():
#     """
#     Reads in, and prints out, the city data, then creates the "best"
#     cycle and prints it out.
#     """
#     file = input("Please input your file name, or type 'None' to exit: \n")
#     
#     
#     if file == 'None':
#         return  "Goodbye!"
#     
#     
#     while file != 'None':
#     #prevents function from crashing if file is not found. Prompts user to input file name again. 
#         try:
#             f = open(file, "r")
#         except:
#             print("There is no file named " + "'" + file + "'.")
#             file = input("Please input your file name: \n")
#             if file == 'None':
#                 return "Goodbye!"
#     
#     road_map = read_cities(file)
#     
#     #assigned original road_map
#     road_map2 = print_cities(road_map)
#     print('Original road_map: \n'+str(road_map2) +  '\n')
#     
#     best_cycle = find_best_cycle(road_map2)
#     
#     #print_map(best_cycle)
#     
#     print("Best cycle: \n" + str(best_cycle))
#     
#     if __name__ == "__main__": #keep this in
#         main()
#         return "main name"
