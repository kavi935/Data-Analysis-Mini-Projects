# SpeechRecognition: This helps your program understand and convert spoken words into text.
#PyAudio: This lets your program record and play sounds.
#setuptools: This helps you package your python project and share your Python programs with others.
#webbrowser: This can open websites in your web browser from your Python program.
#pyttsx3:helps to convert text to sound.
#requests: to requset to get your api keys for conecting two software applications
#gtts:just like pyttsx3, it helps to store mp3 file seperately and more efficient and natural voice processing library.
#pygame:This is a library for writing video games but it also has functionalities to play sound files.

import speech_recognition as sr
import webbrowser
import pyttsx3                     #gtts and ttsmaker are more various text to speech,tts maker is for unlimited usage with free api key acces.
import musiclibrary
import requests
from gtts import gTTS 
import pygame

recognizer = sr.Recognizer()
engine = pyttsx3.init()             
voices = engine.getProperty('voices')
newsapi = "58498680e33546ea86567de917843593"

def speak(text):
    engine.setProperty('voice', voices[1].id)     #to change voice in pyttsx3
    engine.say(text)
    engine.runAndWait()

def speak_new(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='en')                #gtts:Generate a speech audio file from text, You can use gTTS.
    tts.save(filename)

     # Initializing  Pygame mixer
    pygame.mixer.init()                    #pygame:Play the generated speech audio file, You can use pygame to load and play the MP3 file created by gTTS.

    # Load the MP3 file
    pygame.mixer.music.load('output.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
     
    print(f"Audio saved as {filename}")



def processcomand(c):
  if "open google" in c.lower():
        webbrowser.open("https://google.com")
  elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
  elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
  elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
  elif "open instagram" in c.lower():
       webbrowser.open("https://www.instagram.com")
  elif "play" in c.lower():
        song = c.lower().split(" ")[1]    #split helps to convert in list[play,waves] then 1 choose waves in list.
        link = musiclibrary.music[song]
        webbrowser.open(link) 
  elif "tell me the news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey=58498680e33546ea86567de917843593")
        if r.status_code == 200:         #When you see r.status_code == 200, it means the request was successful, and the server has returned the requested data.
            # Parse the JSON response
            data = r.json()               #java script object notation:It's commonly used for transmitting data in web applications, including news APIs.
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title']) 
  else:
      speak_new(c)
                   

# also usage of open ai can be done but its is paid,otherwise we can communicate with jarvis like google,alexa...and ask anything.                     

speak("Initializing Jarvis....")
while True:                                         #it helps to run code infinite untill conditions met
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=7)         #timeout means time takeen to process listening.
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Master")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source,timeout=6, phrase_time_limit=10)     #time phrase time taken by user for speak or pause normal to avoid error
                    command = r.recognize_google(audio)

                    processcomand(command)


        except Exception as e:
            print("Error; {0}".format(e))     #The string "Error; {0}" contains a placeholder {0}.
                                               #The format(e) method replaces the {0} placeholder with the value of e.




