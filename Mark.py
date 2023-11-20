import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio # to take audio input in python
import wikipedia
import webbrowser
import os
import time
import vlc


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def  speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Sir')
    elif hour>=12 and hour<18:
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')
    speak('I am Mark. Your personal assistant. Please tell me how may I help you')
 

def takecommand(): # It takes microphone input from the user and returns String output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.dynamic_energy_ratio = 1
        r.energy_threshold = 650
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query




if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com/")
        elif 'open code help' in query:
            webbrowser.open("https://www.thecodehelp.in/")
        elif 'open punjab university official site' in query:
            webbrowser.open("https://pu.ac.in/")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = 'C:\\Users\\singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'play one love' in query:
            try:
                music_path = 'C:\\Users\\singh\\Music\\onelove.mp3'  

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
        
        elif 'play blue eyes' in query:
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

        elif 'play brown rang' in query:
            try:
                music_path = 'C:\\Users\\singh\\Music\\Brownrang.mp3'
                
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

        elif 'play kalakar' in query:
            try:
                music_path = 'C:\\Users\\singh\\Music\\Kalakaar.mp3'
                
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

        