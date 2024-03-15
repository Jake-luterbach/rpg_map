wild_lands_map = {"Saloon": ["old saloon"],
"town_street": ["Street"],
"Campsite": ["campsite"],
"Wildlands": ["barren lands"],
"Heart_lands": ["Field"]}

Player={"xloc": 0, "yloc": 0}

map_rooms={"saloon":{"title": "A Saloon in Texas.",
                     "description": "A normal saloon for its time," 
                     + "three drunk men sit at the bar.",
                     "options": ["left", "up", "down", "right"]  
                    }
          }
Movement={"walk", "run", "horseback"}

def Mapping():
  global Player
  try:
    Playerloc=(wild_lands_map[Player["xlox"]["yloc"]])
    if 
  except:
      print("Error")
  