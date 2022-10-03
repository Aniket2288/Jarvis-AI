from dataclasses import replace
import imp
import smtplib
from tkinter import E
import webbrowser
import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import os
import datetime
import smtplib
import webbrowser

# print(voices[1].id)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning")
    elif hour>= 12 and hour < 18:
        speak(" good Afternoon")
    else:
        speak("good evening")
    
    speak("This is Jarvis Sir!  How may I  assist you?")

def takecommand():
    # it is use to get voice from microphone and send to the string or pc 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")

    except Exception as e:
        print(e)
        print("say that again...")
        return "None"
    return query    
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo
    server.starttls
    server.login('32aniketis@gmail.com', 'password')
    


if __name__ == "__main__":
    # speak("hello dear Aniket how are you?")
    wishMe()
    # while True:
    if 1:
        query = takecommand().lower()
        # Logic for executing task base on query
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query , sentences= 2 )
            speak("Acoording to Wikipedia..")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")  

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  
         
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir time is {strtime}")
            
        elif 'play music' in query:
            music_dir = 'D:\\Silence'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'open code' in query:
            path = "C:\\Users\\32ani\\OneDrive\\Desktop\\Visual Studio Code.lnk"    
            os.startfile(path)

        elif 'send email to aniket' in query:
            try:   
                speak('what should I say')
                content = takecommand()
                to = '32aniketis@gmail.com'
                sendEmail(to , content)

            except Exception as e:
                print(e)
                speak('I wont able to send this cause of your Nuiesance Problem')