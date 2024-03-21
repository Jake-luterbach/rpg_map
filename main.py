wild_lands_map = ["Saloon", ["old saloon"],
"Town_street", ["Street"],
"Campsite", ["campsite"],
"Wildlands", ["barren lands"],
"Heart_lands", ["Field"]]

Player={"xloc": 0, "yloc": 0}
map_tiles={"saloon":{"title": "A Saloon in Texas.",
                     "description": "A normal saloon for its time," 
                     + "three drunk men sit at the bar.",
                     "options": ["left", "up", "down", "right"]},
          "Town_street":{"title": "a town street in a old western town",
                       "options":["left","up", "down", "right"]}, 
           "Campsite":{"title": "a outlaws groups "+"campsite", 
                       "options":["left","up","down","right"]}, 
           "Wildlands":{"title": "a land filled "+"with wild things", 
                        "options":["left","up","down","right"]},
           "Heart_lands":{"title": "the heart of America"+
                          "filled with the most wild of" + "beasts",
                          "options":["left","up","down","right"]}
          }

           
Movement={"walk", "run", "horseback"}

def Mapping():
  global Player
  try:
    Playerloc = (wild_lands_map[Player["xloc"]][Player["yloc"]]) 
    move=input("what direction? ").capitalize()
    if move == "Right":
     Playerloc[Player["xloc"]] += 1
    if move == "Left":
     Playerloc[Player["xloc"]] -= 1
    if move == "Up":
      Playerloc[Player["yloc"]] += 1
    if move == "down":
      Playerloc[Player["yloc"]] -= 1
    print(Playerloc + map_tiles["title"])
    
  else:
      print("something")
  except Exception:
      print("Error")
Mapping()