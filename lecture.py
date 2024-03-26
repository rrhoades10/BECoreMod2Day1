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


# dict.setdefault()
# return a value associated with a key in our dictionary

stock = {"apples": 30, "oranges": 20}
stock.setdefault("bananas", 15) #if it doesnt exist
print(stock)

print(stock.setdefault("apples", 2376234)) #


my_stuff = []

def add_shirt():
    while True:        
      thing = input("What shirt would you like to add to your stuff? ")
      if thing == "quit":          
          break
      my_stuff.append(thing)

def add_game():
    while True:
      game = input("What game would you like to add to your stuff?")
      
      if game == "quit":
          break
      my_stuff.append(game)

def add_food():
    while True:
      food = input("What food would you like to add to your stuff?")
      if food == "quit":
          break
      my_stuff.append(food)
def show_stuff():
    print("Heres all your stuff: ")
    for stuff in my_stuff:
        print(stuff)


my_stuff = {
#                 0        1          2
    "clothes": ["shirt", "pants", "socks"],
#                 0               1                2               3           4
    "games": ["Super Smash", "Half Life 2", "Baldurs Gate 3", "Valorant", "Call of Duty"],
#                  0                  1          2
    "food": ["Peanut Butter Cups", "Pizza", "Vegetables"]
}
shirt = my_stuff["clothes"][0]
print(shirt)

games = my_stuff["games"]
print(games)
cool_game = games[2]
print(cool_game)

my_stuff["food"].append("tacos")
print(my_stuff['food'])

# Convert the above code to keep track of your stuff in a dictionary
# your keys should be your categories (food, games, clothes, action figures, pokemon cards etc..)
# your values will be lists
# prompt the user to add items to each of their categories
# at the end print each category with the items inside each of those categories

my_stuff = {
    'clothes': ['shirt','pants','socks'],
    'games': ['Super Smash','Zelda','CoD','zombies'],
    'food': ['pizza','resses','veggies']
}
def add_clothes():
    user_input = input(f"What kind of clothes are you adding? : ")
    my_stuff['clothes'].append(user_input)
    print(my_stuff['clothes'])
def add_games():
    user_input = input(f"What kind of game are you adding? : ")
    my_stuff['games'].append(user_input)
    print(my_stuff['games'])
def add_food():
    user_input = input(f"What kind of food are you adding? : ")
    my_stuff['food'].append(user_input)
    print(my_stuff['food'])
# add_clothes()
# add_games()
# add_food()

def add_stuff():
    while True:
        key = input(f"What category should we add to? ")
        if key == "quit":
            break
        elif key in my_stuff:
            while True:
                stuff = input(f"What item would you like to add to your {key}? ")
                if stuff == "quit":
                    break
                my_stuff[key].append(stuff)
        else:
            print(f"{key} not found!")
        
def show_stuff():
    print("Heres all your stuff: ")
    for stuff in my_stuff:
        print(my_stuff[stuff])
# add_stuff()
# show_stuff()

def print_categories():
    print("Choose a category: ")
    for i in my_stuff:
        print(i)
        
def category_add():
    category = input("Choose a category by entering a number: ")
    item = input("Enter an item: ")
    my_stuff[category].append(item)
    print(my_stuff[category])
    
# while True:
#     print_categories()
#     category_add()
#     cont = input("Would you like to add more items? y/n: ")
#     if cont == "n":
#         break
# print("Your full list of stuff: ")
# for k, v in my_stuff.items():
#     print(f"Here is all your {k}")
#     for item in v:
#         print(item)



# Lists as values in dictionaries
library = {
#                   0                 1                           2                                       3
    "Fantasy": ["Harry Potter", "The Hobbit", "Lord of the Rings: The Two Towers", "Lord of the Rings: The Fellowship of the Ring"],
#                         0           1
    "Science Fiction": ["Dune", "Neuromancer"],
#                     0                      1
    "Mystery": ["Sherlock Holmes", "And Then There Were None"]
}
#  accessing our list
print(library['Fantasy'])
# indexing into a list that is a value in a dictionary
print(library["Fantasy"][1])
# looping through a list in a dictionary
for title in library["Fantasy"]:
    print(title)

# adding to a list inside of a dictionary
library["Mystery"].append("Syndrome e")

print(library["Mystery"])

scifi = library["Science Fiction"]
print(scifi)
scifi.append("Stargate SG1")
print(scifi)

# looping through lists in dictionaries
# start by looping through the dictionary items
# keys(), values(), items()
for genre, titles in library.items():
    # grabs each unique key in our dictionary
    print(f"These are the books in your {genre} collection: ")
    # second for loop to iterate through the titles, which are our lists (values)
    for title in titles:
        # prints each item in our list
        print(title)
print(library.items())

# book = "Fantasy"
# genre, title = book
# print(genre)
# print(title)

for genre in library:
    print(f"These are all the books in your {genre} collection: ")
    for title in library[genre]:
        print(title)


# list of dictionaries
art_gallery = [
    {"Title": "Starry Night", "Artist": "Van Gogh", "Year": 1889},
    {"Title": "The Scream", "Artist": "Munch", "Year": 1893},
    {"Title": "Guernica", "Artist": "Picasso", "Year": 1937}
]

for art in art_gallery:
    print(art["Title"], art["Artist"], art["Year"])

# art_gallery.append("Hello there")
# print(art_gallery)
art_gallery.append({"Title": "The Persistence of Memory", "Artist":'Dali', "Year": 1931})
print(art_gallery)


# more lists in dictionaries
valorant_agents = {
    "good agents": ["Todd", "Jeff"],
    "bad agents": ["Everyone Else", "specifically whoever Haya plays"]
}

for quality, agents in valorant_agents.items():
    print(f"Here are the {quality} agents")
    for agent in agents:
        print(agent)

for quality, agents in valorant_agents.items():
    print(quality, agents)

for key in valorant_agents.keys():
    print(key)

for value in valorant_agents.values():
    print(value)
    for agent in value:
        print(agent)

print(valorant_agents.items())

kitchen = {
    "Top Drawer": "Spoons",
    "Bottom Drawer": "Knives",
    "Cabinet": "lovely assortment of coffee mugs"
}

print(kitchen.items())
print(kitchen.keys())
print(kitchen.values())

print(kitchen.keys(), kitchen.values())

for key, value in kitchen.items():
    print(key,value)

print("Top Drawer", kitchen["Top Drawer"])

artist_singles = {
    "Jimmy Eat World": "Firefight",
    "The Beatles": "Strawberry Fields",
    "Sufjan Stevens": "Chicago",
    "Billie": "What was I made for" ,
    "Stevie Wonder": "Isnt She Lovely",
    "SZA": "Snooze",
    "Black Sabbath": "War Pigs",
    "All American Rejects": "Gives You Hell",
    "Logic": "5 am"
}

print(artist_singles.values()) # list of all the values
print(artist_singles['Billie'])
print(artist_singles['SZA'])
print(artist_singles["Logic"])
print(artist_singles.get("The Beatles"))
# grabbing a key that doesnt exist
# print(artist_singles['Wilco'])
# .get() does not give you an error
#  will return None, if the key you're looking for doesnt exist
print(artist_singles.get("Wilco"))
# using .get() with a second arugment
print(artist_singles.get("Wilco", "Artist Not Found"))
if artist_singles.get("Wilco", False) == False:
    print("Artist not found. ")
else:
    print(artist_singles["Wilco"])

numbers = [12, 56, 17, 1, 23, 109]
print(numbers[2]) #<--- grabing a list element by index
print(artist_singles["Jimmy Eat World"]) # <-- accessing a values by key in a dictionary
# the data structure determine if we are "indexing" or not
# you can index into a list but not into a dictionary
weird_dictionary = {
    0: "weird value 0",
    1: "weird value 1",
    2: "weird value 2"
}
print(weird_dictionary[1]) #< what even is this


artist_singles = {
    "Jimmy Eat World": ["Firefight", "The Middle", "Invented"],
    "The Beatles": ["Strawberry Fields", "In My Life", "Hey Bulldog"],
    "Sufjan Stevens": "Chicago",
    "Billie": "What was I made for" ,
    "Stevie Wonder": ["Isnt She Lovely", "Higher Ground"],
    "SZA": "Snooze",
    "Black Sabbath": ["War Pigs", "Iron Man", "Paranoid"],
    "All American Rejects": ["Gives You Hell", "Dirty Little Secret", "Move Along"],
    "Logic": "5 am"
}

print(artist_singles["Jimmy Eat World"][1])
cool_song = artist_singles["The Beatles"]
print(cool_song)
print(cool_song[2])
print(artist_singles["All American Rejects"][2])


# Dicionaries in Dictionaries
museum_exhibits = {
    "Ancient Egypt": {
        "Artifacts": ["Sphinx", "Pyramid"],
        "Famous Pharaohs": ["King Tutunkhamun", "Cleopatra"]
    },
    "Renaissance Art": {
        "Notable Artists": ["Leonardo", "Michelangelo", "Raphael", "Donatello"],
        "Key Works": ["Mona Lisa", "The Last Supper", "Defeating Shredder"]
    }
}
# grabbing regular ole keys from our dictionary to get to the nested dictionaries
print(museum_exhibits["Ancient Egypt"])
print(museum_exhibits["Renaissance Art"])
# going farther into the nested dicitonaries
#     dictionary        key              a key in the dictionary that is a value of the previous key
print(museum_exhibits["Ancient Egypt"]["Artifacts"][1])
# setting variable break points
exhibit1 = museum_exhibits['Ancient Egypt']
print(exhibit1['Artifacts'][1])

# access defeating shredder
print(museum_exhibits['Renaissance Art']['Key Works'][2])

# adding to a nested dictionary
museum_exhibits['Ancient Egypt']["Recent Discovery"] = ["New Tomb", "The scary slab from courage the cowardly dog"]
print(museum_exhibits)

# looping through our nested dictionaries

# museum_exhibits.items()
museum_exhibits = {
    # exhibit
    "Ancient Egypt": { #details
        #section         information
        "Artifacts": ["Sphinx", "Pyramid"],
        #section                    information
        "Famous Pharaohs": ["King Tutunkhamun", "Cleopatra"]
    },
    # exhibit
    "Renaissance Art": { #details
        #section                     information
        "Notable Artists": ["Leonardo", "Michelangelo", "Raphael", "Donatello"],
        #section                   information
        "Key Works": ["Mona Lisa", "The Last Supper", "Defeating Shredder"]
    }
}
for exhibit, details in museum_exhibits.items():
   
    for section, information in details.items():
        print(f" {section}:  {information}")


print(museum_exhibits.items())
print(museum_exhibits['Ancient Egypt'].items())


pokemon = {
    "abilities": 
        {
            "ability": {
                "name": "swarm",
                "description": "Power Up Bug Type Moves"

            },
            "ability2": {
                "name": "guts",
                "description": "Power Up Bug Type Moves"

            }
        }  
    

}
print(pokemon["abilities"]["ability"]["name"])
print(pokemon["abilities"]["ability2"]["name"])

# copying a dictionary
# Shallow Copy / Deep Copy
original_artists = {"Picasso": 1881, "Van Gogh": 1853, "Monet": 1840}
# dict.copy()
copied_artists = original_artists.copy()

print(original_artists)
print(copied_artists)
copied_artists["Van Gogh"] = 1900
print("Original", original_artists)
print("Copied", copied_artists)

# DEEP COPY
import copy
# copy.deepcopy()
original_paintings = {"The Starry Night": "Van Gogh", "The Scream": "Munch" }
reproduced_paintings = copy.deepcopy(original_paintings)

# Change a value in the deep copy
original_paintings["The Starry Night"] = "Da Vinci"
print("Original: ", original_paintings)
print("Reproduced ", reproduced_paintings )

# deepcopy()
test = {
    "name": "Snoopy",
    "occupation": "Charlie Brown's Dog"
}
new_test = copy.deepcopy(test)
print(new_test)

test2 = {
    "name": "Snoopy",
    "occupation": "Charlie Brown's Dog"
}


# copied_paintings = original_paintings
# copied_paintings['The Scream'] = "Donatello"
# print("Original", original_paintings)
# print("Copied", copied_paintings)





test = {

}

test.update({"test":"hello"})

print(test)












     

















