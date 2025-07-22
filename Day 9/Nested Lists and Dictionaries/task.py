capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary
# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

#print(travel_log["France"][2])

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

travel_log = {
    "France" : {
        "num_times_visitet": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visitet": 5,
        "cities_visited": ["Stuttgart", "Berlin"]
    }
}
print(travel_log["Germany"]["cities_visited"][0])