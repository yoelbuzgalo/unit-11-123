import music

def test_song():
    # Setup
    expected_title = 'Fireworks'
    expected_artist = 'Katy Perry'
    expected_min = 2
    expected_seconds = 20

    # Invoke
    result = music.Song(expected_title, expected_artist, music.Time(0, 2, 20))

    # Analysis
    assert result.title == expected_title
    assert result.artist == expected_artist
    assert result.duration.minutes == expected_min
    assert result.duration.seconds == expected_seconds
