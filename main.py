import map

wild_lands_map = [["Saloon", "Town_street", "Wildlands", "Heart_lands"],
["Town_street", "Wildlands","Campsite", "Heart_lands"],
["saloon", "townstreet", "campsite", "Wildlands"]]

Player={"xloc": 0, "yloc": 0}
map_tiles={"Saloon":{"title": "A Saloon in Texas.",
                     "description": "A normal saloon for its time," 
                     + "three drunk men sit at the bar.",
                     "options": ["left", "up", "down", "right"]},
          "Town_street":{"title": "a street in a town",
                         "description":"a town street in a old western town",
                       "options":["left","up", "down", "right"]}, 
           "Campsite":{"title": "a campsite outside of town",
                       "description":"a outlaws groups "+"campsite", 
                       "options":["left","up","down","right"]}, 
           "Wildlands":{"title": "a wild land with beasts",
                        "description": "a land filled "+"with wild things", 
                        "options":["left","up","down","right"]},
           "Heart_lands":{"title": "the heart of America",
                          "description": "filled with the most wild of " + "beasts",
                          "options":["left","up","down","right"]}
          }

           
Movement={"walk", "run", "horseback"}
while True:
  def Mapping():
    global Player
    try:
      map.write()
      move = input("what direction? ").capitalize()
      if move == "Right":
       Player["xloc"] += 1
      elif move == "Left":
       Player["xloc"] -= 1
      elif move == "Up":
        Player["yloc"] += 1
      elif move == "Down":
        Player["yloc"] -= 1
      elif move == "map":
        map.read()
      else:
        print("Error")
      Playerloc = (wild_lands_map[Player["xloc"]][Player["yloc"]]) 
      print(map_tiles[Playerloc]["description"])
    except Exception:
      print("Error")
  Mapping()
