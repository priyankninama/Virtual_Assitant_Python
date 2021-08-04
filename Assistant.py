import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evenning!")

    speak("I am your virtual assistant. How can I help You") 

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening.......")
         r.pause_threshold = 1
         audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
    
    except Exception as e:
        print(e)

        print("Couldn't understand say that again...")
        return "None"
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your_email-id', '')
    server.sendmail('Your_email-id', to, content)
    server.close()

if __name__ == "__main__":
    #speak("Hii I am Your Virtual Assistant")
    wishme()
    while True:
        Query = takecommand().lower()

        if 'wikipedia' in Query:
            speak('Searching Wekipedia..')
            Query = Query.replace("Wekipedia", "")
            results = wikipedia.summary(Query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            continue

        elif "tell me your name" in Query:
            speak("I am Jarvis. Your deskstop Assistant")
            continue

        elif 'open youtube' in Query:
            speak('openning youtube')
            webbrowser.open("youtube.com")
            continue

        elif 'open Google' in Query:
            speak('openning google')
            webbrowser.open("google.com")
            continue   

        elif 'open facebook' in Query:
            speak('openning facebook')
            webbrowser.open("facebook.com")
            continue
         
        elif 'play music' in Query:
            #webbrowser.open("gaana.com")
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            filename = random.choice(songs)
            music_path = os.path.join(music_dir, filename)
            print(songs)
            os.startfile(music_path)
            continue

        elif 'play movies' in Query:
            video_dir = 'F:\\'
            video = os.listdir(video_dir)
            filename = random.choice(video)
            video_path = os.path.join(video_dir, filename)
            print(filename)
            os.startfile(video_path)
            continue
    
        elif 'The time' in Query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(f"The time is {time}")
            continue

        elif "which day it is" in Query:
            day = datetime.datetime.today().weekday() + 1
            Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak("The day is " + day_of_the_week)
            continue

        elif "open Vs code" in Query:
            codepath = "C:\\Users\\Local\\ProgramsMicrosoft VS Code\\Code.exe"
            os.startfile(codepath)
            continue

        elif "send email" in Query:
            try:
                speak('What should I send')
                content = takecommand()
                to = "Your_Email-id"
                sendemail(to, content)
                speak("Email is sent")
            except Exception as e:
                print (e)
                speak("sorry for inconvenience cannot send email  ")
                
        elif "bye" in Query:
            speak("Bye. Happy to help you!")
            exit()