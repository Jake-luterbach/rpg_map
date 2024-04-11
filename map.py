from tabulate import tabulate

mapfile = 'map.text'

message={"quit": "thanks for playing this game" + "we hope you return someday"
         , "dust": "you better watch out" + 
          "because those outlaws and beasts will turn ya to dust if you aint careful.",
          "read": "seems like your map isn't working, maybe try again", 
          "write": "looks like your map is blank for some reason, maybe try again" }
wild_lands_map = [["Saloon", "Town_street", "Wildlands", "Heart_lands"],
["Town_street", "Wildlands","Campsite", "Heart_lands"],
["saloon", "townstreet", "campsite", "Wildlands"]]
           
def write():
  try:
    with open(mapfile, 'w') as file:
      file.write(tabulate(wild_lands_map,tablefmt = 'fancy_table'))
  except:
    print(f"{message['write']}")
  finally:
    print("don't lose this map, traveler")

def read():
  try:
    with open(mapfile, 'r') as file:
      print(file.read())

  except:
    print(f"{message['read']}")
  else:
    print(f"{message['dust']}")
  finally:
    print("good luck with your adventure")
