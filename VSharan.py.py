import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with sr.Microphone() as origin:
            print('Listening...')
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            print('User said:', instruction)
    except sr.UnknownValueError:
        talk("Sorry, I couldn't understand what you said.")
        instruction = None
    except sr.RequestError:
        talk("Sorry, there was an issue with the speech recognition service.")
        instruction = None
    return instruction

def play_VSharan():
    instruction = input_instruction()
    if instruction:
        if "play" in instruction:
            song = instruction.replace('play', "")
            talk("Playing " + song)
            pywhatkit.playonyt(song)
        elif 'time' in instruction:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'date' in instruction:
            date = datetime.datetime.now().strftime('%d/%m/%Y')
            talk("Today's date is " + date)
        elif 'how are you' in instruction:
            talk('I am fine, how about you?')
        elif 'what is your name' in instruction:
            talk('I am VSharan, what can I do for you?')
        elif 'who is' in instruction:
            person = instruction.replace('who is', "")
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        else:
            talk('Please repeat')

play_VSharan()
