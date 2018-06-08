home = [38.546500, -121.767264]
point = [38.560621, -121.744877]

import coordtool

home = coordtool.coordtool(home)
print(home.distance(point))
