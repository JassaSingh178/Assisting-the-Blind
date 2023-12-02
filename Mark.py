import pyttsx3  # Importing the pyttsx3 module for text-to-speech conversion
import datetime  # Importing the datetime module for handling date and time
import speech_recognition as sr  # Importing the speech_recognition module for recognizing speech
import pyaudio  # Importing the pyaudio module for audio input
import wikipedia  # Importing the wikipedia module for accessing Wikipedia content
import webbrowser  # Importing the webbrowser module for opening web pages
import os  # Importing the os module for interacting with the operating system
import time  # Importing the time module for time-related functions
import vlc  # Importing the vlc module for audio and video playback

engine = pyttsx3.init('sapi5')  # Initializing the pyttsx3 engine for speech synthesis
voices = engine.getProperty('voices')  # Retrieving the available voices
# engine.setProperty('voice', voices[0].id)  # Setting the voice property (commented out)

# Function to speak out the provided 'audio' string
def speak(audio):
    engine.say(audio)  # Convert text to speech
    engine.runAndWait()  # Execute speech synthesis

# Function to greet the user based on the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)  # Getting the current hour of the day
    # Greeting the user based on the time of the day
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')
    speak('I am Mark. Your personal assistant. Please tell me how may I help you')  # Providing assistant introduction

def takecommand():  # Function to take microphone input from the user and return recognized speech as text
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Accessing the microphone as the audio source
        print("Listening...")  # Indicating that the system is listening
        r.pause_threshold = 0.5  # Setting pause duration for speech recognition
        r.dynamic_energy_ratio = 1  # Adjusting dynamic energy ratio for speech recognition
        r.energy_threshold = 650  # Setting the energy threshold for speech recognition
        audio = r.listen(source)  # Capturing audio input from the microphone
    try:
        print("Recognizing...")  # Indicating speech recognition processing
        query = r.recognize_google(audio, language='en-in')  # Recognizing speech using Google Speech Recognition
        print(f"User said: {query}\n")  # Displaying the recognized speech
    except Exception as e:
        print("Say that again please...")  # Prompting the user to repeat if speech recognition fails
        return "None"
    return query  # Returning the recognized speech as text

# Main execution starts here
if __name__ == '__main__':
    wishMe()  # Greeting the user
    while True:  # Creating an infinite loop for continuous interaction
        query = takecommand().lower()  # Taking user input and converting it to lowercase for easy comparison
        # Logic for executing tasks based on the recognized query
        # Various conditions check for specific user commands and perform corresponding actions
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        # The following elif conditions handle different user commands for opening various websites
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
        elif 'open vs code' in query:
            codePath = 'C:\\Users\\singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        # The following elif condition plays specific music files
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

        
