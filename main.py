
wild_lands_map:{[Saloon: "Saloon"],
                [town_street: "Street"],
                [Campsite: campsite],
                [Wildlands: barren lands],
                [Heart_lands: Field]}

try:
  Player={xloc = 0 , yloc = 0}
  map_rooms={"saloon":{"A Saloon in Texas":
                   "an saloon normal for its time, three drunk men sit at the bar"
                   "options":[left,up,down,right]}}
  Playerloc=(wild_lands_map[yloc][xloc])

except:
    print("Error")
  