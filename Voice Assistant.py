import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Bolna shuru kro...")
    audio=r.listen(source)
try:
    command=r.recognize_google(audio)
    command=command.lower()
    print("Aapne bola:",command)
    if "hello" in command:
        speak("Hello,main aapka voice assistant hu")

    elif "time" in command:
        time=datetime.datetime.now().strftime("%H:%M")
        speak("Abhi time hai " + time)

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Youtube open kr rha hu")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Google open kr raha hu") 

    elif "wikipedia" in command:
        speak("Wikipedia par search kr raha hu")
        result=wikipedia.summary(command,sentences=2)
        print(result)
        speak(result)

    elif "notepad" in command:
        os.system("notepad")
        speak("Notepad open kar raha hu")
    else:
        speak("Sorry mujhe samaj nhi aaya")  
except:
    print("Error aa gaya")            
    


