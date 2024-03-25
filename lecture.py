# Initializing Dictionaries
# Creating an empty dictionary

kitchen = {}
print(kitchen)

# Populate dictionary with key-value pairs
# dictionary in python is an ordered collection of key-value pairs
kitchen = {
    # key : value
    # keys must be unique
    "Spoon": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"    
}
print(kitchen)

# Accessing information in a dictionary
kitchen = {
    # key : value
    # keys must be unique
    "Spoon": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"    
}

# when accessing information from a dictionary
# we access the value through the key
# similar to how we can grab an element in a list by its position
# dict['key'] <- return the value associated with that key
spoon_location = kitchen["Spoon"]
print(spoon_location)
cup_location = kitchen['Cups']
print(cup_location)

#you can have integers as keys
# just be careful not to confuse the syntax with a list
mall = {
    "one": "General Store",
    "two": "Tm's",
    "three": "Stat Items",
    4: "Vending Machine"
} 
first_floor = mall["one"] # be careful to not confuse this with a list
print(first_floor)
fourth_floor = mall[4]
print(fourth_floor)
print(mall["three"])

# Trying to access a key in our dicionary that doesn't exist
kitchen = {
    # key : value
    # keys must be unique
    "Spoon": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"    
}
print(kitchen)
# toaster_location = kitchen['Toaster']

# This gives us a KeyError
# Traceback (most recent call last):
#   File "c:\Users\rrhoa\OneDrive\Documents\CodingTempleBECore\week_2\day_1\lecture.py", line 58, in <module>
#     toaster_location = kitchen['Toaster']
# KeyError: 'Toaster'

# Safer way to access information from a dictionary
# dict.get(key we're looking for, what to return if that key isnt found)
# .get() is "safer" because you cant confuse with indexing into list
# you can avoid errors messages and customize what is return if the key is not found


kitchen = {
    # key : value
    # keys must be unique
    "Spoon": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"    
}
# .get() with somethign that is in our dictionary
print(kitchen.get("Plates")) # -- "Middle Shelf"

#.get() with no existing key
print(kitchen.get('Toaster'))

# .get() with a customized return - what do we return if that key isn't found
print(kitchen.get('Spatula', "There is no spatula here! :("))

# Adding and Updating our Dictionary
community_center = {
    "Yoga": "8 AM",
    "Art": "10 AM"
}

print(community_center)
# adding to a dictionary
# dict['key to be added'] = 'value to be added at that key'
community_center["Smash Tournament"] = "7 PM"
print(community_center)

community_center['Valorant Comp'] = "ALL DAY GET HERE EARLY NERDS"
community_center['Pottery Class'] = "5 AM"
community_center['Dance Class'] = '5:30 PM'
community_center["Bingo"] = "9 AM"
community_center["Axe Throwing"] = "10 PM, specifically after drinks"
community_center["Coding Camp"] = "6 pm"
print(community_center)

# Updating a dictionary
# looks very similar to adding
#dict['key to be updated'] = 'new value'
# the key has to exist in order to update that specific key
# otherwise you just end up adding to the dictionary
community_center['Valorant Comp'] = "TBD"
print(community_center)

#using update()
# dict.update({"key to be added or updated": "value for that key"})
# adding to our dictionary with update()
community_center.update({"Pickleball": "12 PM"})
print(community_center)

# updating with update()
community_center.update({"Pottery Class": "6 AM"})
print(community_center)

# removing from a dicitonary in python
# dict.pop("key to be removed")
basket = {
    "Apples": 30,
    "Oranges": 20,
    "Bananas": 15
}

removed_item = basket.pop("Oranges")
print(removed_item)
print(basket)

# takes an optional second argrument that is returned if the key is not found
# if no second argument is provided and the key is not found, then you get a KeyError
removed_item2 = basket.pop("Strawberries", "Not Found")
print(removed_item)
print(basket)

# dict.popitem() no parameters, it pops the last item in your dictionary
user_data = {
    "name": "Ash Ketchum",
    "age": 10,
    "city": "Pallet Town"
}

popped_item = user_data.popitem()
print(popped_item)
print(user_data)

user_data["name"] = "Brock"
print(user_data)

# del
# del removes variables from memory
name = "Dark Magician"
print(name)
del name # this comepletely removes the name variable from memory
# print(name) <-- NameError

book_shelf = {
    "Fiction": 10,
    "Non-Fiction": 7,
    "Mystery": 5,
    "Manga": 15
}

del book_shelf['Mystery']
print(book_shelf)

# dict.clear()
# deletes everything in the dictionary
session_data = {"user_id":12435, "status": "active", "username": "Yermomlol"}
session_data.clear()
print(session_data)


# Accessing information in our dictionary by loops
# .keys(), .values(), .items()
community_center = {
    "Yoga": "8 AM",
    "Art": "10 AM",
    "Smash Tournament": "7 PM",
    "Valorant Comp": "All Day, get here early nerds",
    "Pottery Class": "5 AM",
    "Dance Class": "5:30 PM",
    "Bingo": "9 AM",
    "Axe Throwing": "10 PM, specifically after drinks",
    "Coding Camp": "6 PM"
}
# looping through keys
#looping through the dictionary with no extra methods
for key in community_center:
    print(key)
#dict.keys()
print(community_center.keys())
com_keys = community_center.keys()
print(com_keys)
for key in community_center.keys():
    print(key) 
print() #prints a new line
# looping with keys to access values in dictionary
print("Here are the times of all of our events: ")
for activity in community_center.keys():
    print(f"{activity} starts at {community_center[activity]}") #activity as a key, is going to give me the time of each activity 

community_center["Art"]
community_center["Yoga"]
community_center["Smash Tournament"]
# similar to this BUT NOT THE SAME BECAUSE DICTIONARIES AND LISTS ARE DIFFERENT
# names = ["bob", "jim", "gertrude"]
# for i in range(len(names)):
#     print(names[i])

# looping through a dictionary's values
# dict.values()
community_center = {
    "Yoga": "8 AM",
    "Art": "10 AM",
    "Smash Tournament": "7 PM",
    "Valorant Comp": "All Day, get here early nerds",
    "Pottery Class": "5 AM",
    "Dance Class": "5:30 PM",
    "Bingo": "9 AM",
    "Axe Throwing": "10 PM, specifically after drinks",
    "Coding Camp": "6 PM"
}  
print(community_center.values())
for value in community_center.values():
    print(value)

# sorting my dicionary's keys
# sorted() <-- creates a copy of the list and sorts it
for activity in sorted(community_center.keys()):
    print(f"{activity} starts at {community_center[activity]}")


sorted_dict_keys = sorted(community_center)
print(sorted_dict_keys)

sorted_dict_values = sorted(community_center.values())
print(sorted_dict_values)


# dict.items() --> list a of tuples. where the key is the first position and the value is the second position
community_center = {
    "Yoga": "8 AM",
    "Art": "10 AM",
    "Smash Tournament": "7 PM",
    "Valorant Comp": "All Day, get here early nerds",
    "Pottery Class": "5 AM",
    "Dance Class": "5:30 PM",
    "Bingo": "9 AM",
    "Axe Throwing": "10 PM, specifically after drinks",
    "Coding Camp": "6 PM"
} 
print(community_center.items())
for key, value in community_center.items():
    print(f"{key} starts at {value}")

for activity, time in community_center.items():
    if time == "6 PM":
        print(f"Oh cool! I can participate in {activity}")
    else:
        print("I cant do that!")

kitchen = {
    # key : value
    # keys must be unique
    "Spoon": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"    
}
for utensil, location in kitchen.items():
    if location == "Top Drawer":
        print(f"Yay I found the {utensil}")

for item in kitchen.items():
    print(item)

utensil, location = ('Spoon', 'Top Drawer')
print(utensil)
print(location)

# counter dictionary
names = ["Ryan", "Mary", "Haya", "Raymond","Haya","Haya","Haya","Haya", "Jesica","Jesica","Jesica","Jesica","Jesica","Jesica", "Ryan","Ryan","Ryan","Mary","Mary","Mary","Mary","Mary","Raymond","Raymond","Raymond",]

name_count = {}
for name in names:
    if name not in name_count:
        #name_count.update({name:1})
        name_count[name] = 1
    else:
        # name_count.update({name:name_count[name]+1})
        name_count[name] += 1
print(name_count)


    












     

















