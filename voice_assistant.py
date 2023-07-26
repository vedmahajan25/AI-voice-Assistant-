import speech_recognition as sr 
import webbrowser
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id) 

r = sr.Recognizer()

def listen_to_audio():
    with sr.Microphone() as source:
        print("listening......")
        audio = r.listen(source)
    return audio

def process_audio(audio):
    try:
        text = r.recognize_google(audio,language="hi-IN")
        print("you said:",text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I can't understand what you said")
    except sr.RequestError as e:
        print("Could not request results from speech recognition service;{0}".format(e))
    return None

def  respond_to_text(text):
    if "यूट्यूब" in text:
        webbrowser.open("https://www.youtube.com/")
        engine.say("Opening Youtube")
        engine.runAndWait()
    elif "गूगल" in text:
        webbrowser.open("https://www.google.com/")
        engine.say("Opening Google")
        engine.runAndWait()
    elif "फेसबुक" in text:
        webbrowser.open("https://www.facebook.com/")
        engine.say("Opening Facebook")
        engine.runAndWait()
    else :
        print("Sorry, I can't understand your command")
        engine.say("Sorry, I can't understand your command")
        engine.runAndWait()

def  main():
    audio=listen_to_audio()
    text = process_audio(audio)
    if text:
        respond_to_text(text)

if __name__ == "__main__":
    main()