class Time:
    __slots__ = ['hours', 'minutes', 'seconds']

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

class Song:
    __slots__ = ['title', 'artist', 'duration']
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    __slots__ = ['title', 'artist', 'num_tracks', 'total_duration']
    def __init__(self, title, tracks=None):
        self.title = title
        self.tracks = []
        
        # Checks whether if tracks list is passed to this class, adds each one of them to the album track list
        if tracks is not None and len(tracks) > 0:
            for track in tracks:
                self.tracks.append(track)

        self.artists = set()

        # Updates artists name in a set list (all artist names will be unique meaning no duplicate names)
        if len(self.tracks) > 0:
            for track in self.tracks:
                self.artists.add(track.artist)
        
        self.num_tracks = len(tracks)
        
        # Update total duration
        total_duration_seconds = 0
        total_duration_mins = 0
        total_duration_hours = 0
        for track in self.tracks:
            total_duration_seconds += track.duration.seconds
            total_duration_mins += track.duration.minutes
            total_duration_hours += track.duration.hours

        self.total_duration(Time(total_duration_hours, total_duration_mins, total_duration_seconds))
        
def add_song(song, album):
    album.tracks.append(song)
    album.total_duration.hours += song.duration.hours
    album.total_duration.minutes += song.duration.minutes
    album.total_duration.seconds += song.duration.seconds

def print_album(album):
    print("Album Title:", album.title)
    print("Album Tracks:")
    for track in album.tracks:
        print(track.titl)
    print("Album Duration:", get_time(album.total_duration))

def get_time(time):
    return '{}:{:02}:{:02}'.format(time.hours, time.minutes, time.seconds)

def main():
    track_1 = Song('Californication', 'Red Hot Chili Peppers', Time(0, 2, 20))
    track_2 = Song('You Get What You Give', 'New Radicals', Time(0, 4, 35))
    track_3 = Song('Fortunate Son', 'Creedence Clearwater Revival', Time(0, 3, 10))

