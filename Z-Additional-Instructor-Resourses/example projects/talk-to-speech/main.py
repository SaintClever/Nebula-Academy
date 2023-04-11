import pyttsx3
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

engine.say("I will speak this text")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


text = str(input("Paste article\n"))
res = requests.get(text)
soup = BeautifulSoup(res.text, "html.parser")
articles = []

# need to find a way to stop it once it going without force quitting my terminal
for i in range(len(soup.select("p"))):
    article = soup.select("p")[i].getText().strip()
    articles.append(article)

text = " ".join(articles)
speak(text)