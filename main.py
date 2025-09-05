import speech_recognition as sr 
import webbrowser
import pyttsx3 
import musiclibrary
import requests
from openai import OpenAI
import openai
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "6e1d463db95e450b9488c0746441c744"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcesses(command):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    

    try:
        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "you are a virtual assistant named jarvis skilled in general tasks like alexa and gooogle cloud"},
                {"role": "user", "content": command}
            ]
        )

        return completion.choices[0].message.content

    except openai.RateLimitError :
        print("⚠️ You exceeded your quota. Please check your OpenAI plan and billing.")

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open chatbot" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "play song" in c.lower():
        webbrowser.open("https://www.youtube.com/watch?v=enjkcCdAlXc&list=RDenjkcCdAlXc&start_radio=1")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] 
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/everything?q=apple&from=2025-09-03&to=2025-09-03&sortBy=popularity&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])
                print(article['title'])
    else:
        output = aiProcesses(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Neel...")
    while True:
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit= 2)
            word = r.recognize_google(audio)
            if(word.lower()== "hey neel"):
                speak("yes sir")
                with sr.Microphone() as source:
                    print("Neel Active...")
                    audio = r.listen(source,)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
        except Exception as e:
            print("Error...".format(e))
