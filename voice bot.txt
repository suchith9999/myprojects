import speech_recognition as sr
import pyttsx3 as pyttsx3
# import pyaudio
import pywhatkit
#pip install pywhatkit
import datetime 
#pip install wikipedia
import wikipedia
#pip install pyjokes
import pyjokes
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Alexa' in command:
                command = command.replace('Alexa', '')
                print(command)
    except:
        pass
    return  command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing  ' + song)
        pywhatkit.playonyt(song)     
    elif 'time' in  command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is  ' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, i am in a relationship with wifi')
    elif 'are you single' in command:
        talk('sorry, i am in a relationship with wifi')
    elif 'fuck you' in command:
        talk('sorry, i am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    take_command()
    run_alexa()
    
time.sleep(9)