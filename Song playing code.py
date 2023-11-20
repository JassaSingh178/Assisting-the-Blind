import vlc

try:
    music_path = 'C:\\Users\\singh\\Music\\Blueeyes.mp3'  

    # Creating instance of VLC
    instance = vlc.Instance('--no-xlib')

    # Creating a new media player object
    player = instance.media_player_new()

    # Load the audio file into VLC
    media = instance.media_new(music_path)
    player.set_media(media)

    # Start playing the music
    player.play()

    # Wait for the playback to finish
    while True:
        state = player.get_state()
        if state == vlc.State.Ended:
            break

except Exception as e:
    print(f"Error occurred: {e}")
