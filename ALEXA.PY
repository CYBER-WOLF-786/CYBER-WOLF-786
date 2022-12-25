import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            talk("yes what can i do for you")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
    except:
        pass
    return command 

def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M%p")
        talk("current time is " + time)
        print(time)
    elif "who make you" in command:
        talk("cyber wolf")
        print("CYBER WOLF")
    elif "what is your name" in command:
        talk("my name is alexa")

#idk

    elif "who the heck is" in command:
        person = command.replace("who the is", "")
        info = wikipedia.summary(person, 1)
        print (info)
        #funny question
    elif "single" in command :
        talk("i am in a relation with wifi")
    elif "are you" in command:
        talk ("i am fine, how are you")
    elif "date" in command:
        talk("sorry, I have a headache")
        
    
        #jokes
    elif "joke" in command :
        talk(pyjokes.get_jokes())

#wikipidea search

    elif "what" in command or "why" in command or "who" in command or "where" in command or "how" in command:
        what = command.replace("play", "")
        result = wikipedia.search(what)
        #talk("the", result)
        talk (result)
    
# cyber wolf youtube channel

    elif "which youtube channel is best for learning" in command:
        cyber_Wolf = command.replace("play", "")
        talk("playing" + cyber_Wolf)
        pywhatkit.playonyt("https://youtu.be/uHkhyH6VWGY")
    elif "print" in command:
        talk("printing"+command)
        print(command)
    
        

    else :
        talk("i cant answer it my tecnical team is working on it, we will set this mistakes after some updates thank you")


run_alexa()


 
