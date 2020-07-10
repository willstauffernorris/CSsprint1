import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  # def __str__(self):
  #   return self.name + str(self.lat) + str(self.lon)


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#

# Store the instances in the "cities" list, below.

# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.


def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list

  with open('cities.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      name = row[0]
      lat = float(row[3])
      lon = float(row[4])
      city = City(name, lat, lon)
      cities.append(city)
  return cities

cities = []
cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
  #print(c)
  print((c.name, c.lat, c.lon))




# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.



# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

userinput1 = input("Enter lat1,lon1: 45,-100 or press ENTER") or (45,-100)
print(f"You entered {userinput1}")

userinput2 = input("Enter lat2,lon2: 32,-120 or press ENTER") or (32,-120)
print(f"You entered {userinput2}")


  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

def cityreader_stretch(lat1=userinput1[0], lon1=userinput1[1], lat2=userinput2[0], lon2=userinput2[1], cities=[]):
  lat1 = float(lat1)
  lon1 = float(lon1)
  lat2 = float(lat2)
  lat2 = float(lat2)


## I need to make the normalizer to have this work, but I'm not there yet.
  if lat1 < lat2:
    highest_lat = lat2
    lowest_lat = lat1
  else:
    highest_lat = lat1
    lowest_lat = lat2

  if lon1 < lon2:
    highest_lon = lon2
    lowest_lon = lon1
  else:
    highest_lon = lon1
    lowest_lon = lon2
  
  print(highest_lon)
  print(highest_lat)
  print(lowest_lon)
  print(lowest_lat)

  # within will hold the cities that fall within the specified region
  within = []

  for city in cities:
    if (city.lat < highest_lat) and (city.lat > lowest_lat) and (city.lon < highest_lon) and (city.lon > lowest_lon):
      within.append(city)
      print(city.name, city.lat, city.lon)
  return within


# call my function
print("These cities are within your coordinates:")
#cityreader_stretch(cities=cities)

cityreader_stretch(userinput1[0], userinput1[1], userinput2[0], userinput2[1], cities=cities)