import pyttsx3
import wikipedia
import datetime
import speech_recognition as sr
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0])
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("i am Zira sir. How may i help you...")

def takeCommand():
    # it takes the input from the user through microphone and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        # print(e)
        print("please say that again")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp@gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shivamkanowziya111.sk@gmail.com', 'sk7011212998')
    server.sendmail('shivamkanowziya111.sk@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia:")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open hacker rank' in query:
            webbrowser.open("hackerrank.com")


        elif 'play music' in query:
            # using \\ to bypass the path or folder
            music_dir = "C:\\Users\\Shivam-Bam\\Music\\MiDrop"
            song = os.listdir(music_dir)
            print(song, end="\n")
            os.startfile(os.path.join(music_dir, song[3]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir, the time is {strTime}")

        elif 'email to shivam' in query:
            try:
                speak("what you want to send")
                content = takeCommand()
                to = "shivamkanowziya111.sk@gmail.com"
                sendEmail(to, content)
                speak("email has been sent successfully:")

            except Exception as e:
                print(e)
                speak("sorry we didn't able to send... unsuccessful")