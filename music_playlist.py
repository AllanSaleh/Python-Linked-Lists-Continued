from linked_list import Node, LinkedList #Importing my LinkedList and Node class from linkedlist.py file

class Song:
  def __init__(self, title, artist, duration):
    self.title = title
    self.artist = artist
    self.duration = duration

class MusicPlaylist:
  def __init__(self, name):
    self.name = name
    self.songs = LinkedList()
    self.current_position = -1
  
  def add_song(self, title, artist, duration):
    song = Song(title, artist, duration)
    self.songs.append(song)
  
  def display(self):
    '''Show all the songs and artists in my playlist'''
    print("============= " + self.name + " =============")
    current = self.songs.head
    counter = 1
    while current:
      print(f"{counter}.) {current.data.title} - {current.data.artist}")
      current = current.next
      counter+=1
  
  def play_song_at_position(self,position):
    song = self.songs.get_at_position(position)
    self.current_position = position
    if song:
      print(f"Now playing: {song.title}")
  
  def next_song(self):
    next_position = self.current_position + 1
    next_song = self.songs.get_at_position(next_position)
    self.current_position = next_position
    print(f"Now Playing: {next_song.title}")
    return next_song
  
  def previous_song(self):
    previous_position = self.current_position - 1
    prev_song = self.songs.get_at_position(previous_position)
    self.current_position = previous_position
    print(f"Now Playing: {prev_song.title}")
    return prev_song
  
  def remove_current_song(self):
    removing = self.songs.delete_at_position(self.current_position)
    print(f"Removed Song {removing.data.title}")


playlist = MusicPlaylist("Bootcamp Bangerz")
playlist.add_song("Thriller", "Michael Jackson", 175)
playlist.add_song("Dreams ", "Fleetwood Mac", 500)
playlist.add_song("Soft Spine", "Spiritbox", 420)
playlist.add_song("Rick Astley", "Never Gonna Give You UP", 350)
playlist.add_song("Anomaly", "Aviana", 410)
playlist.add_song("Bright Eyes", "lover I dont have to love", 410)


playlist.display()

playlist.play_song_at_position(2)

playlist.next_song()
playlist.previous_song()
playlist.remove_current_song()

