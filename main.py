import os
import speech_recognition as sr 
import win32com.client as wc
import pyaudio

 
speaker =  wc.Dispatch("SAPI.Spvoice")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language="en-in")
            print(f"User said = {query}")        
            return query
        except Exception as e:
            return "Some error Occured. Sorry from Jarvis"
            

# text = "Hello, I am Jarvis A.I."
while True:
    print("listening")
    text = takecommand()
    speaker.Speak(text)
