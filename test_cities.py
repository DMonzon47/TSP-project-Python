import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

    assert (compute_total_distance(2) == 4.1)
    #assert.raises(TypeError, compute_total_distance, "4.1")

def test_swap_cities():
    '''add your tests'''
    assert (swap_cities(1,4) == ("test1", "new_total_distance"))
    #assert.raise(TypeError, swap_cities, True)

def test_shift_cities():
    '''add your tests'''
    assert shift_cities("road_map") == ("road_map")
    #assert.raise(TypeError, shift_cities, 5)

"""
if test___name__ == "__main__": #keep this in
    main()
    assert __name__("__main__") == "__main__"
    #assert.raise(TypeError, __name__, 5)
"""
