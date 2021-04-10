import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui 
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha 
import time


engine = pyttsx3.init()
wolframalpha_app_id = 'PJ72TW-6V75PAJKKK'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(month)
    speak(date)
    speak(year)


def wishme():
    speak("Welcome back Shivam")
    time_()
    date_()


    #greetings

    hour=datetime.datetime.now().hour

    if  hour >= 6 and hour <= 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir!")

    speak("Your Assistant is as your service. Please tell me How can I help you today?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio,language='en-US')
        print(query)
        

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    
    #for this function, we must enable low security in gmail which we are going to use as a sender

    server.login('shivam1999dubey@gmail.com','password')
    server.sendmail('username@gmail.com', to,content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/Mr. Gates/Desktop/screenshot.png')


def cpu():
    usage= str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())


if __name__ == '__main__':
    wishme()

    while True:
        query = TakeCommand().lower()

        #all the commands will be stored in a lower case in query for easy recognition

        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak('Searching...')
            query=query.replace('wikipedia','')
            result= wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result) 

        elif 'send email' in query:
            try:
                speak("What do you want to send  in email?")
                content=TakeCommand()
                #provide reciever email address
                
                speak('Who is the reciever?')
                reciever=input("Enter reciever's Email ID:")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')

            except Exception as e:
                print(e)
                speak('Unable to send an Email.')

        elif 'search in chrome' in query:
            speak('What to search, Shivam?')
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            #chromepath is the location of chrome installation directory
            search=TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')   #only open website with an extension of .com at the end

        elif 'search in youtube' in query:
            speak('What to search, Shivam?')
            search_Term= TakeCommand().lower()
            speak("Here we go to Youtube!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search google' in query:
            speak('What to google, Shivam?')
            search_Term=TakeCommand().lower()
            speak('Searching...')
            wb.open('https://www.google.com/search?q='+search_Term)


        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak('Going offline Sir!')
            quit()

        elif 'word' in query:
            speak('Opening MS Word Sir...')
            ms_word = r'C:/Program Files (x86)/Microsoft Office/Office16/WINWORD.EXE'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak('What to write, Sir?')
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak("Sir, Shoud i include date and time?")
            ans = TakeCommand()
            if 'yes' in ans or 'Sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done taking notes Sir!')
            else:
                file.write(notes)

        elif 'show notes' in query:
            speak('Showing notes...')
            file= open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()

        elif 'play music' in query:
            songs_dir = 'D:/SONGS'
            music = os.listdir(songs_dir)
            speak('What do you want to listen, Sir?')
            speak('Select a number...')
            ans = TakeCommand().lower()
            while('number' not in ans and ans != 'random' and ans != 'you choose'):
                speak('I could not understand you. Please try again.')
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number',''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(1,100)

            os.startfile(os.path.join(songs_dir,music[no]))

        elif 'remember that' in query:
            speak("What should I remember?")
            memory = TakeCommand()
            speak("You asked to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak('You asked me to remember that'+remember.read())

        elif  'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/everything?q=apple&from=2021-04-08&to=2021-04-08&sortBy=popularity&apiKey=d77eb06f0da84eae8b5d9641705b39ea")
                data = json.load(jsonObj)
                i = 1
                speak('Here are some top headlines from the business sector')
                print('======TOP HEADLINES======'+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description'+'\n'])
                    speak(item['title'])
                    i += 1
            except Exception as e:
                print(str(e))

        
        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https:/www.google.com/maps/place/"+location)


        elif 'calculate' in query:
            client= wolframalpha.Client('PJ72TW-6V75PAJKKK')
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The answer is : '+answer)
            speak('The answer is '+answer)

        elif 'what is' in query or 'who is' in query:
            #uses the same upi wolframalpha
            client = wolframalpha.Client('PJ72TW-6V75PAJKKK')
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text) 
            except StopIteration:
                print("No results found")


        elif 'stop listening' in query:
            speak('For how many seconds you want me to stop listening, Sir?')
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

            


