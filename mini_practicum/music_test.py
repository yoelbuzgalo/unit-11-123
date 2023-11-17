import music

def test_song():
    # Setup
    expected_title = 'Fireworks'
    expected_artist = 'Katy Perry'
    expected_duration = 10

    # Invoke
    result = music.Song(expected_title, expected_artist, expected_duration)

    # Analysis
    assert result.title == expected_title
    assert result.artist == expected_artist
    assert result.duration == expected_duration
