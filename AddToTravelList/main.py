import json

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name, times_visit, city_names):
    travel_log.append([{'country': country_name, 'visits':times_visit, 'cities':city_names}])


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Louisiana", 25, ["Kaplan", "New Roads", "Ville Platte"])

print(json.dumps(travel_log, indent=2))



