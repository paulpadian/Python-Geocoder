import geocoder

destinations = {"The Space Needle",
  "Crater Lake",
  "The Golden Gate Bridge",
  "Yosemite National Park",
  "Las Vegas, Nevada",
  "Grand Canyon National Park",
  "Aspen, Colorado",
  "Mount Rushmore",
  "Yellowstone National Park",
  "Sandpoint, Idaho",
  "Banff National Park",
  "Capilano Suspension Bridge"
}

for point in destinations:
  # Get the latitude and longitude from `geocoder`.
  g = geocoder.arcgis(point)

  # Print out `geopy`'s results.
  print(f'{point} coordinates are ({g.latlng})') 
