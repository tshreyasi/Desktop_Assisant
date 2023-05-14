import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os 
import pyautogui
import pyjokes
from googletrans import Translator


from wikipedia.wikipedia import search

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour >=4 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("good evening")
    speak("I am Siri, your AI assistant. Please tell me how may I help you")

def takeCommand():
    #take microphn as input and returns the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..... Go ahead")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio , Language = 'en-in')
        print("User said: ", query)
    
    except Exception as e:
        print("I am not sure I understand")
        speak("I  am not sure I understand")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("abcd1234@gmail.com","123test")
    server.sendmail("abcd1234@gmail.com",to , content)
    server.close

def screenshot():
    img=pyautogui.screenshot()
    img.save("Desktop\ss.png")


def jokes():
    speak(pyjokes.get_joke())


def translation(info , des):
    translator= Translator()
    trans_sen= translator.translate(info , dest = des)
    try:
        print(trans_sen.pronunciation)
        speak(trans_sen.pronunciation)
        print(trans_sen.text)
    except Exception as e:
        print(e)


if __name__== "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        print(query)
        if 'wikipedia' in query:
            speak("Searching...")
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accoring to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'play music' in query:
            music_dir =''

        elif 'time' in query:
            strTime = datetime.datetime.now().strTime("%H:%M:%S")
            speak("the current time is ",strTime)
        
        elif 'send email' in query:
            try:
                speak("what should i write")
                content = takeCommand()
                to = "abc@gmail.com"
                sendEmail(to , content)
                speak("email has been sent!")
            except Exception as e:
                print("Failed to sent")
                speak("failed to sent")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'logout' in query:
            os.system("shutdown - l")
        
        elif 'remember that' in query:
            speak("what should i remember?")
            data= takeCommand()
            speak("you said me to remember " + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif 'do you know' in query:
            remember= open("data.txt", "r")
            speak("you said me to remember " + remember.read())
        
        elif 'screenshot' in query():
            screenshot()
            speak("done!")
        
        elif 'tell jokes' in query:
            jokes()

        elif 'bye' or 'shut up' or 'go to hell' or 'go offline' in query:
            quit()
        
        elif 'what is your name' or 'who are you' in query:
            print("I am Siri! Your AI assistant. Give the commands.")
            speak("I am Siri! Your AI assistant. Give the commands.")
        
        
            
        else:
            chromepath ="C://Users//HP//AppData//Local//Google//Chrome//Application//chrome.exe %s"
            search= takeCommand().lower()
            webbrowser.get(chromepath).open_new_tab(search)
