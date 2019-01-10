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

def makeSpacecraftList(planets, voyage_list):
  spacecraft_list = []
  for planet in planets:
    for voyage in voyage_list:
      if planet in voyage:
        spacecraft_list.append((planet, voyage[0]))
        continue
  return spacecraft_list

spacecraft_list = makeSpacecraftList(planet_list, voyages)

mercury_voyages = []
venus_voyages = []
jupiter_voyages = []
saturn_voyages = []
earth_voyages = []
mars_voyages = []

for pair in spacecraft_list:
  if pair[0] == "Mercury":
    mercury_voyages.append(pair[1])
  elif pair[0] == "Venus":
    venus_voyages.append(pair[1])
  elif pair[0] == "Jupiter":
    jupiter_voyages.append(pair[1])
  elif pair[0] == "Saturn":
    saturn_voyages.append(pair[1])
  elif pair[0] == "Earth":
    earth_voyages.append(pair[1])
  elif pair[0] == "Mars":
    mars_voyages.append(pair[1])

def formatSpacecraftList(planet, voyage_list):
  sentence = ""
  sentence += planet
  sentence += ":"
  for spacecraft in voyage_list:
    sentence += spacecraft
    sentence += " "
  return sentence

print(formatSpacecraftList("Venus", venus_voyages))
print(formatSpacecraftList("Mars", mars_voyages))
print(formatSpacecraftList("Mercury", mercury_voyages))
print(formatSpacecraftList("Earth", earth_voyages))
print(formatSpacecraftList("Jupiter", venus_voyages))
print(formatSpacecraftList("Saturn", saturn_voyages))