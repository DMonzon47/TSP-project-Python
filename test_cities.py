import pytest
from cities import *

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
    
    road_map5 = [("Kentucky", "Frank","fort",5, 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint", "Paul", 44.95, -93.094)]
    
    road_map6 = [('Arizona', 'Phoenix', 33.45, -112.07),\
                ('Alaska', 'Juneau', 58.3, -134.42),\
                ('Alabama', 'Montgomery', 32.36, -86.28),\
                ('Arkansas', 'Little Rock', 34.74, -92.33),\
                ('California', 'Sacramento', 38.56, -121.47),\
                ('Colorado', 'Denver', 39.74, -104.98),\
                ('Connecticut', 'Hartford', 41.77, -72.68)]

    assert compute_total_distance(road_map1) == pytest.approx(38.53)
    assert compute_total_distance(road_map2) == "Incorrect type/format. 'road_map' index[2] and [3] must be of float() types." 
    assert compute_total_distance(road_map3) == "Empty 'road_map', please input correct format: [('state','city','latitude','longitude')]."
    assert compute_total_distance(road_map4) == "Incorrect type/format. 'road_map' index[2] and [3] must be of float() types."
    assert compute_total_distance(road_map5) == "List does not follow format [(state, city, latitude, longitude)]"
    assert compute_total_distance(road_map6) == pytest.approx(213.15)
    
def test_swap_cities():

    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    new_road_map1 = [("Delaware", "Dover", 39.161921, -75.526755),\
                    ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                    ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    
    road_map2 = [("Kentucky", "Frankfort", '38.197274', '-84.86311'),\
                ("Delaware", "Dover", '39.161921', '-75.526755'),\
                ("Minnesota", "Saint Paul", '44.95', '-93.094')]
        
    road_map3 = []
    
    road_map4 = [("Kentucky", "Frankfort", int(38.197274), int(-84.86311)),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    road_map5 = [(1, 2, 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    road_map6 = [('Alabama', 'Montgomery', 32.36, -86.28),\
                ('Alaska', 'Juneau', 58.3, -134.42),\
                ('Arizona', 'Phoenix', 33.45, -112.07),\
                ('Arkansas', 'Little Rock', 34.74, -92.33),\
                ('California', 'Sacramento', 38.56, -121.47),\
                ('Colorado', 'Denver', 39.74, -104.98),\
                ('Connecticut', 'Hartford', 41.77, -72.68)]

    new_road_map6 = [('Arizona', 'Phoenix', 33.45, -112.07),\
                ('Alaska', 'Juneau', 58.3, -134.42),\
                ('Alabama', 'Montgomery', 32.36, -86.28),\
                ('Arkansas', 'Little Rock', 34.74, -92.33),\
                ('California', 'Sacramento', 38.56, -121.47),\
                ('Colorado', 'Denver', 39.74, -104.98),\
                ('Connecticut', 'Hartford', 41.77, -72.68)]
    
    #new_total_distance = pytest.approx(38.53)

    assert swap_cities(road_map1,0,1) == (new_road_map1, pytest.approx(38.53))
                        #assert.raise(TypeError, swap_cities, True)
    assert swap_cities(road_map1,1.4,2.8) == "Input: index1 or index2 is of wrong type. Input must be an int."
    assert swap_cities(road_map2,1,2) == "Incorrect type. 'road_map' index[2] and [3] must be of float() types."
    assert swap_cities(road_map5,1,2) == "Incorrect type. 'road_map' index[0] and [1] must be of str() types."
    assert swap_cities(road_map3,1,2)== "Empty 'road_map', please input correct format: [('state','city','latitude','longitude')]."
    assert swap_cities(road_map4,1,2) == "Incorrect type. 'road_map' index[2] and [3] must be of float() types."
    assert swap_cities(road_map6,0,2) == (new_road_map6, pytest.approx(213.15))

    
    
def test_shift_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    new_road_map2 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                    ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                    ("Delaware", "Dover", 39.161921, -75.526755)]
    
    road_map2 = [("Kentucky", "Frankfort", '38.197274', '-84.86311'),\
                ("Delaware", "Dover", '39.161921', '-75.526755'),\
                ("Minnesota", "Saint Paul", '44.95', '-93.094')]
        
    road_map3 = []
    
    road_map4 = [("Kentucky", "Frankfort", int(38.197274), int(-84.86311)),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    road_map5 = [('Alabama', 'Montgomery', 32.36, -86.28),\
                ('Alaska', 'Juneau', 58.3, -134.42),\
                ('Arizona', 'Phoenix', 33.45, -112.07),\
                ('Arkansas', 'Little Rock', 34.74, -92.33),\
                ('California', 'Sacramento', 38.56, -121.47),\
                ('Colorado', 'Denver', 39.74, -104.98),\
                ('Connecticut', 'Hartford', 41.77, -72.68)]

    new_road_map5 = [('Connecticut', 'Hartford', 41.77, -72.68),\
                ('Alabama', 'Montgomery', 32.36, -86.28),\
                ('Alaska', 'Juneau', 58.3, -134.42),\
                ('Arizona', 'Phoenix', 33.45, -112.07),\
                ('Arkansas', 'Little Rock', 34.74, -92.33),\
                ('California', 'Sacramento', 38.56, -121.47),\
                ('Colorado', 'Denver', 39.74, -104.98)]

    assert shift_cities(road_map1) == new_road_map2
                #assert.raise(TypeError, shift_cities, 5)
    
    assert shift_cities(road_map2) == "Incorrect type. 'road_map' index[2] and [3] must be of float() types."
    assert shift_cities(road_map3)== "Empty 'road_map', please input correct format: [('state','city','latitude','longitude')]."
    assert shift_cities(road_map4) == "Incorrect type. 'road_map' index[2] and [3] must be of float() types."
    assert shift_cities(road_map5) == new_road_map5
        
    
