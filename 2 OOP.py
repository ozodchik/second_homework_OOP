class Track:
  def __init__(self, name, duration):
    self.name = name 
    self.duration = duration
  def __str__(self):
    return f'трек: {self.name} - {self.duration} минут'
  def __repr__(self):
    return f'трек: {self.name} - {self.duration} минут'


class Album():
  def __init__(self, name, group):
    self.group = group  
    self.name = name
    self.tracks_list = []

  def add_track(self, track):
    return self.tracks_list.append(track)

  def __str__(self): 
    return (f'Альбом: {self.name} \n группа: {self.group}\n треки в альбоме: {self.tracks_list}')

  def get_tracks(self):
    return  self.tracks_list

  def album_info(self):
    return self.name


tracks = [ #это не имеет отношение к трекам в альбоме 
  #это для вывода треков в классе трек 
  Track("shape of you", 5),
  Track("believer", 7),
  Track("faded", 9),
  Track("i got love", 8),
  Track("birds", 4),
  Track("live like legends", 2)
]
for tracklist in tracks: #это для списка треков в классе трек      
  print(tracklist)

albums = [
  ("BEST", "Homework"),
  ("Favorites", "My best")
]

tracks = [ 
  ("shape of you", 5),
  ("believer", 7),
  ("faded", 9),
  ("i got love", 8),
  ("birds", 4),
  ("live like legends", 2)
]

ALBUMS = []

for name, group in albums:
  album = Album(name, group)
  for name, duration in tracks:
    track = Track(name, duration)
    album.add_track(track)
  ALBUMS.append(album)

for album in ALBUMS:
  print(album)

class Newtrack:
  def __init__(self, name, duration):
    self.name = name 
    self.duration = duration

track_1 = Newtrack("Boxing", 8)
track_2 = Newtrack("Flying", 6)

if track_1.duration > track_2.duration:
  print("track_1 > track_2")
  print(True)
else:
  print("track_1 > track_2")
  print(False)
