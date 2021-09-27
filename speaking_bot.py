import datetime
import os
import pyttsx3
import speech_recognition as sr
import webbrowser


p=int(datetime.datetime.today().hour)
print("THE CURRENT TIME IS ",p)
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voices",voices[1].id)
t="how can i help u"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    if p>=0 and p<12:
        speak("good morning sir, how  can i help u ")
    elif p>=12 and p<18:
        speak("good afternoon sir,how  can i help u  ")
    else:
        speak("good evening ,chusha hua anda")
        
def taking():
    s=sr.Recognizer()
    with sr.Microphone() as source:
        s.pause_threshold=1
        audio=s.listen(source,timeout=10)

    try:
        print("listening ....")
        print("Recognition ..")
        query = s.Recognize_google(audio)
        print(f"user said:{query}\n")
    except Exception as e:
        print("plss repeat sir ..")
        return 'none'
    return  query    
    


if _name_ == "_main_":
    wish()
    

    while True:

        query = taking().lower() 

       
        if "open youtube" in query:
            speak("searching for youtube")
            webbrowser.open("www.youtube.com")
        if "gooogle" in query:
            webbrowser.open("www.google.com")    
            



                  
    
         
   
   
    
    
    
   
   
        
        
        
    
    speak("i think this is the result which u searchng")
