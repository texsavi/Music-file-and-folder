import os, time, csv

with open("100MostStreamedSongs.csv") as file:
  data=csv.DictReader(file)
  for row in data:
    dir=os.listdir()
    artist=row["Artist(s)"].title()
    print(artist)
    song=row["Song"]
    print(song)
    if artist not in dir:
      os.mkdir(artist)
    path=os.path.join(f"{artist}",song)
    f=open(path,"w")
    f.close()
      

  

