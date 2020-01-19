import csv
from geopy.geocoders import Nominatim

with open("fourtyNiners.csv") as f:
    line = f.readline()
    players_uni_dict = {}
    while line:
        result = line.strip().split(",")
        players_uni_dict[result[0]] = result[1]
        line = f.readline()


def get_location(uni):
    a = "University of"
    b = "University"
    geolocator = Nominatim(user_agent="my_map")
    location = geolocator.geocode(uni)
    location2 = geolocator.geocode(a + uni)
    location3 = geolocator.geocode(uni + b)

    if location is not None:
        return location
    elif location2 is not None:
        return location2
    else:
        return location3


lat_long_dict = {}

# loop the dictionary
for player, university in players_uni_dict.items():
    try:
        location = get_location(university)
        lat_long = {}

        lat_long["latitude"] = location.latitude
        lat_long["longitude"] = location.longitude
        lat_long_dict[player] = lat_long
    except Exception as e:
        continue

print(lat_long_dict)

'''
with open('player_file.csv', 'a') as player_file:
    player_writer = csv.writer(player_file, delimiter=',')
    player_writer.writerow(['Player', "Latitude", "Longitude"])

    for player, latlong in lat_long_dict.items():
        player_writer.writerow(
            [player, latlong["latitude"], latlong["longitude"]])
'''