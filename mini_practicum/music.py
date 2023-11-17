class Time:
    __slots__ = ['hours', 'minutes', 'seconds']

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

def get_time(time):
    return '{}:{:02}:{:02}'.format(time.hours, time.minutes, time.seconds)
