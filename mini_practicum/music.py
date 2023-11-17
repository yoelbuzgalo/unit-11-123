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

def get_time(time):
    return '{}:{:02}:{:02}'.format(time.hours, time.minutes, time.seconds)

def main():
    track_1 = Song('Californication', 'Red Hot Chili Peppers', Time(0, 2, 20))
    track_2 = Song('You Get What You Give', 'New Radicals', Time(0, 4, 35))
    track_3 = Song('Fortunate Son', 'Creedence Clearwater Revival', Time(0, 3, 10))
