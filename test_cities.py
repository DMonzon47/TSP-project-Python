import pytest
from cities2 import *

def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    road_map2 = [("Kentucky", "Frankfort", '38.197274', '-84.86311'),\
                ("Delaware", "Dover", '39.161921', '-75.526755'),\
                ("Minnesota", "Saint Paul", '44.95', '-93.094')]
        
    road_map3 = []
    
    road_map4 = [("Kentucky", "Frankfort", int(38.197274), int(-84.86311)),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    road_map5 = [("Kentucky", "Frank","fort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint", "Paul", 44.95, -93.094)]

    assert cities.compute_total_distance(road_map1) == pytest.approx(38.53)
    
    assert cities.compute_total_distance(road_map2) == "Incorrect type/format. 'road_map' index[2] and [3] must be of float() types."
    
    assert cities.compute_total_distance(road_map3)== "Empty 'road_map', please input correct format: [('state','city','latitude','longitude')]."
    assert cities.compute_total_distance(road_map4) == "Incorrect type/format. 'road_map' index[2] and [3] must be of float() types."
    
    assert cities.compute_total_distance(road_map4) == "List does not follow format [(state, city, latitude, longitude)]"
    
    
def test_swap_cities():

    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    new_road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    
    road_map2 = [("Kentucky", "Frankfort", '38.197274', '-84.86311'),\
                ("Delaware", "Dover", '39.161921', '-75.526755'),\
                ("Minnesota", "Saint Paul", '44.95', '-93.094')]
        
    road_map3 = []
    
    road_map4 = [("Kentucky", "Frankfort", int(38.197274), int(-84.86311)),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    new_total_distance = pytest.approx(4.4)

    assert cities.swap_cities(road_map1,0,1) == (new_road_map1, new_total_distance)
                        #assert.raise(TypeError, swap_cities, True)
    assert cities.swap_cities(road_map1,1.4,2.8) == "Input: index1 or index2 is of wrong type. Input must be an int."
    
    assert cities.swap_cities(road_map2,1,2) == "Incorrect type. 'road_map' index[2] and [3] must be of float() types."
    
    assert cities.swap_cities(road_map3,1,2)== "Empty 'road_map', please input correct format: [('state','city','latitude','longitude')]."
    assert cities.swap_cities(road_map4,1,2) == "Incorrect type. 'road_map' index[2] and [3] must be of float() types."
    
    
    
def test_shift_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    new_road_map2 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    road_map2 = [("Kentucky", "Frankfort", '38.197274', '-84.86311'),\
                ("Delaware", "Dover", '39.161921', '-75.526755'),\
                ("Minnesota", "Saint Paul", '44.95', '-93.094')]
        
    road_map3 = []
    
    road_map4 = [("Kentucky", "Frankfort", int(38.197274), int(-84.86311)),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    new_total_distance = pytest.approx(4.4)

    assert cities.shift_cities(road_map1) == new_road_map2
                #assert.raise(TypeError, shift_cities, 5)
        
    assert cities.shift_cities(road_map1) == (new_road_map1, new_total_distance)
                        #assert.raise(TypeError, swap_cities, True)
    
    assert cities.shift_cities(road_map2) == "Incorrect type. 'road_map' index[2] and [3] must be of float() types."
    
    assert cities.shift_cities(road_map3)== "Empty 'road_map', please input correct format: [('state','city','latitude','longitude')]."
    assert cities.shift_cities(road_map4) == "Incorrect type. 'road_map' index[2] and [3] must be of float() types."

        
    
