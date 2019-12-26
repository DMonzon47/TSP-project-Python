{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['Alabama', 'Montgomery', '32.361538', '-86.279118'], ['Alaska', 'Juneau', '58.301935', '-134.41974'], ['Arizona', 'Phoenix', '33.448457', '-112.073844'], ['Arkansas', 'Little Rock', '34.736009', '-92.331122'], ['California', 'Sacramento', '38.555605', '-121.468926'], ['Colorado', 'Denver', '39.7391667', '-104.984167'], ['Connecticut', 'Hartford', '41.767', '-72.677'], ['Delaware', 'Dover', '39.161921', '-75.526755'], ['Florida', 'Tallahassee', '30.4518', '-84.27277'], ['Georgia', 'Atlanta', '33.76', '-84.39'], ['Hawaii', 'Honolulu', '21.30895', '-157.826182'], ['Idaho', 'Boise', '43.613739', '-116.237651'], ['Illinois', 'Springfield', '39.78325', '-89.650373'], ['Indiana', 'Indianapolis', '39.790942', '-86.147685'], ['Iowa', 'Des Moines', '41.590939', '-93.620866'], ['Kansas', 'Topeka', '39.04', '-95.69'], ['Kentucky', 'Frankfort', '38.197274', '-84.86311'], ['Louisiana', 'Baton Rouge', '30.45809', '-91.140229'], ['Maine', 'Augusta', '44.323535', '-69.765261'], ['Maryland', 'Annapolis', '38.972945', '-76.501157'], ['Massachusetts', 'Boston', '42.2352', '-71.0275'], ['Michigan', 'Lansing', '42.7335', '-84.5467'], ['Minnesota', 'Saint Paul', '44.95', '-93.094'], ['Mississippi', 'Jackson', '32.32', '-90.207'], ['Missouri', 'Jefferson City', '38.572954', '-92.189283'], ['Montana', 'Helana', '46.595805', '-112.027031'], ['Nebraska', 'Lincoln', '40.809868', '-96.675345'], ['Nevada', 'Carson City', '39.160949', '-119.753877'], ['New Hampshire', 'Concord', '43.220093', '-71.549127'], ['New Jersey', 'Trenton', '40.221741', '-74.756138'], ['New Mexico', 'Santa Fe', '35.667231', '-105.964575'], ['New York', 'Albany', '42.659829', '-73.781339'], ['North Carolina', 'Raleigh', '35.771', '-78.638'], ['North Dakota', 'Bismarck', '48.813343', '-100.779004'], ['Ohio', 'Columbus', '39.962245', '-83.000647'], ['Oklahoma', 'Oklahoma City', '35.482309', '-97.534994'], ['Oregon', 'Salem', '44.931109', '-123.029159'], ['Pennsylvania', 'Harrisburg', '40.269789', '-76.875613'], ['Rhode Island', 'Providence', '41.82355', '-71.422132'], ['South Carolina', 'Columbia', '34', '-81.035'], ['South Dakota', 'Pierre', '44.367966', '-100.336378'], ['Tennessee', 'Nashville', '36.165', '-86.784'], ['Texas', 'Austin', '30.266667', '-97.75'], ['Utah', 'Salt Lake City', '40.7547', '-111.892622'], ['Vermont', 'Montpelier', '44.26639', '-72.57194'], ['Virginia', 'Richmond', '37.54', '-77.46'], ['Washington', 'Olympia', '47.042418', '-122.893077'], ['West Virginia', 'Charleston', '38.349497', '-81.633294'], ['Wisconsin', 'Madison', '43.074722', '-89.384444'], ['Wyoming', 'Cheyenne', '41.145548', '-104.802042']]\n"
     ]
    }
   ],
   "source": [
    "def read_cities(file_name):\n",
    "    \"\"\"\n",
    "    Read in the cities from the given `file_name`, and return \n",
    "    them as a list of four-tuples: \n",
    "\n",
    "      [(state, city, latitude, longitude), ...] \n",
    "\n",
    "    Use this as your initial `road_map`, that is, the cycle \n",
    "\n",
    "      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.\n",
    "    \"\"\"\n",
    "    road_map = []\n",
    "    infile = open(file_name,\"r\")\n",
    "    \n",
    "    inline = infile.readlines()\n",
    "    r_listt = [line.rstrip() for line in inline]\n",
    "    listt = [(line.split('\\t',4)) for line in r_listt]\n",
    "    #r_listt = [line.rstrip() for line in inline]\n",
    "    \n",
    "    infile.close()   \n",
    "    return listt\n",
    "\n",
    "    #read_cities('city-data.txt')\n",
    "\n",
    "    #for i in listt: \n",
    "\n",
    "#split split(/t) line where /t and create a 4 element tuple. Then add to roadmap.\n",
    "\n",
    "# divide each string into 4 strings at \"t\"\n",
    "# remove \"n\" ()\n",
    "# tranform into tuple \n",
    "# add to listt\n",
    "# return listt\n",
    "road_map = read_cities('city-data.txt')\n",
    "print(road_map)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Montgomery', 32.36, -86.28), ('Juneau', 58.3, -134.42), ('Phoenix', 33.45, -112.07), ('Little Rock', 34.74, -92.33), ('Sacramento', 38.56, -121.47), ('Denver', 39.74, -104.98), ('Hartford', 41.77, -72.68), ('Dover', 39.16, -75.53), ('Tallahassee', 30.45, -84.27), ('Atlanta', 33.76, -84.39), ('Honolulu', 21.31, -157.83), ('Boise', 43.61, -116.24), ('Springfield', 39.78, -89.65), ('Indianapolis', 39.79, -86.15), ('Des Moines', 41.59, -93.62), ('Topeka', 39.04, -95.69), ('Frankfort', 38.2, -84.86), ('Baton Rouge', 30.46, -91.14), ('Augusta', 44.32, -69.77), ('Annapolis', 38.97, -76.5), ('Boston', 42.24, -71.03), ('Lansing', 42.73, -84.55), ('Saint Paul', 44.95, -93.09), ('Jackson', 32.32, -90.21), ('Jefferson City', 38.57, -92.19), ('Helana', 46.6, -112.03), ('Lincoln', 40.81, -96.68), ('Carson City', 39.16, -119.75), ('Concord', 43.22, -71.55), ('Trenton', 40.22, -74.76), ('Santa Fe', 35.67, -105.96), ('Albany', 42.66, -73.78), ('Raleigh', 35.77, -78.64), ('Bismarck', 48.81, -100.78), ('Columbus', 39.96, -83.0), ('Oklahoma City', 35.48, -97.53), ('Salem', 44.93, -123.03), ('Harrisburg', 40.27, -76.88), ('Providence', 41.82, -71.42), ('Columbia', 34.0, -81.03), ('Pierre', 44.37, -100.34), ('Nashville', 36.16, -86.78), ('Austin', 30.27, -97.75), ('Salt Lake City', 40.75, -111.89), ('Montpelier', 44.27, -72.57), ('Richmond', 37.54, -77.46), ('Olympia', 47.04, -122.89), ('Charleston', 38.35, -81.63), ('Madison', 43.07, -89.38), ('Cheyenne', 41.15, -104.8)]\n"
     ]
    }
   ],
   "source": [
    "def print_cities(road_map):\n",
    "    \"\"\"\n",
    "    Prints a list of cities, along with their locations. \n",
    "    Print only one or two digits after the decimal point.\n",
    "    \"\"\"\n",
    "    \n",
    "    road_map2 = [(i[1],round(float(i[2]),2),round(float(i[3]),2)) for i in road_map]\n",
    "#round a float number not float a rounded string!!\n",
    "\n",
    "    return road_map2\n",
    "\n",
    "print_cities = print_cities(road_map)\n",
    "print(print_cities)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50\n"
     ]
    }
   ],
   "source": [
    "print(len(road_map))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "def compute_total_distance(road_map):\n",
    "    \"\"\"\n",
    "    Returns, as a floating point number, the sum of the distances of all \n",
    "    the connections in the `road_map`. Remember that it's a cycle, so that \n",
    "    (for example) in the initial `road_map`, Wyoming connects to Alabama...\n",
    "    \"\"\"\n",
    "    a = 0\n",
    "    c = 0\n",
    "    \n",
    "    #sqrt((x1-x2)^2 + (y1-y2)^2)\n",
    "    #circuit = lst[(i + 1) % len(lst)]\n",
    "    while a != len(road_map): \n",
    "        for i in road_map: \n",
    "            c+= math.sqrt((i[1] - (i+1[1])**2)+ (i[2] - (i+1)[2])**2)\n",
    "            a+=1\n",
    "    \n",
    "    \n",
    "    return float(c)\n",
    "print(compute_total_distance(print_cities))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "32.36 58.3\n",
      "90.66\n"
     ]
    }
   ],
   "source": [
    "a = print_cities[0][1]\n",
    "b = print_cities[1][1]\n",
    "print(a,b)\n",
    "print(a+b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def swap_cities(road_map, index1, index2):\n",
    "    \"\"\"\n",
    "    Take the city at location `index` in the `road_map`, and the \n",
    "    city at location `index2`, swap their positions in the `road_map`, \n",
    "    compute the new total distance, and return the tuple \n",
    "\n",
    "        (new_road_map, new_total_distance)\n",
    "\n",
    "    Allow for the possibility that `index1=index2`,\n",
    "    and handle this case correctly.\n",
    "    \"\"\"\n",
    "    new_roadmap = [0]\n",
    "    new_total_distance = 0.0\n",
    "    return (new_roadmap,new_total_distance)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
