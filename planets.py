planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
# print(planet_list)
planet_list.extend(["Earth", "Venus"])
# print(planet_list)
planet_list.append("Pluto")
# print(planet_list)

rocky_planets = planet_list[0:2]
# print(rocky_planets)
rocky_planets.extend(planet_list[4:6])
# print(rocky_planets)
del(planet_list[6])
# print(planet_list)

voyages = [("spacecraft1", "Saturn", "Earth"), ("spacecraft2", "Venus", "Mars", "Mercury"), ("spacecraft3", "Venus", "Jupiter"), ("spacecraft4", "Jupiter")]

def makeSpacecraftDict(planets, voyage_list):
  """[Function to make key value pairs with the planet as the key and a list of satellites that visited the planet as the value]

  Arguments:
    planets {[list]} -- [list of planets]
    voyage_list {[list]} -- [list of tupples with the first value being the satelite and the rest of the values being the planets it visited]

  Returns:
    [dictionary] -- [planets and satellites visited key/value pairs]
  """

  spacecraft_dict = dict()
  for planet in planets:
    for voyage in voyage_list:
      if planet in voyage:
        try:
          spacecraft_dict[planet].append(voyage[0])
        except KeyError:
          spacecraft_dict[planet] = list()
          spacecraft_dict[planet].append(voyage[0])

  return spacecraft_dict

spacecraft_dict = makeSpacecraftDict(planet_list, voyages)
print(spacecraft_dict)