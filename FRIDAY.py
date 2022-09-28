import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import random
import webbrowser
import smtplib
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("i am FRIDAY, sir please tell me how may I help you")

def takeCommand():
    #Its takes microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("Say That again please...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('serderemail@gmail.com','senderemailpassword')
    server.sendmail('senderemail@gmail.com',to,content)
    server.close()
if __name__=="__main__":
    WishMe()
    while(True):
        query=takeCommand().lower()
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir="D:\\Song"
            songs=os.listdir(music_dir)
            i=random.randint(1,len(songs))
            os.startfile(os.path.join(music_dir,songs[i]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtime}")
        elif 'open vs code' in query:
            codepath="E:\\VS Code\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'email to subham' in query:
            try:
                speak('what should I say?')
                content=takeCommand()
                to="receiveremail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry Sir I am not able to send this email")
        elif 'quit' in query:
            exit()