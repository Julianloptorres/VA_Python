import pyttsx3;
import speech_recognition as sr;
import webbrowser;
import datetime;
import pywhatkit;
import os;
import yfinance as yf;
import pyjokes; 
import wikipedia;

#Listen to our voice and return audio as a text using google.

def transform():
    r = sr.Recognizer()
    with sr.Microphone() as mi_voz:
        r.pause_threshold = 0.8
        said = r.listen(mi_voz)
        try: 
            print('I am listening')
            q = r.recognize_google(said,language="en")
            return q
        except sr.UnknownValueError:
            print('Sorry I did not get it')
            return 'I am waiting'
        except sr.RequestError:
            print('Sorry the service is down')
            return 'I am waiting'
        except:
            return "I am waiting"

transform();

#speaks the message as an audio
def speaking(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

speaking('Hello ana. How are you doing?');

#install language from the computer
engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)


#use an specific "person" for reading
id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice',id)
engine.say("hello, ana. How are you?")
engine.runAndWait()

#return the weekday name
def query_day():
    day = datetime.date.today()
    print(day)
    weekday = day.weekday()
    print(weekday)
    mapping = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }
    try: 
        speaking(f' Today is {mapping[weekday]}')
    except:
        pass

    query_day()

    #returns the time
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speaking(f"{time[1]}o'clock and {time[2:4]} minutes")

query_time()

#greetings starting up
def whatsup():
    speaking('''Hi, my name is Ana: I am your personalassistant. What can I do for you?
    ''')

whatsup()

#The heart of the assistant. It takes queries and returns answers.
def querying():
    whatsup()
    start = True
    while(start):
        q = transform().lower()

        if 'start yourtube' in q:
            speaking('starting youtube. just a second')
            webbrowser.open('http://www.youtube.com')
            continue
        elif 'start web' in q:
            speaking('opening browser')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is it' in q:
            query_day()
            continue
        elif 'What time is it' in q:
            query_time()
            continue
        elif "stop" in q:
            speaking('I am shutting down')
            break
        elif "from wikipedia" in q:
            speaking('checking wikipedia')
            q = q.replace("widipedia","")
            result = wikipedia.summary(q, sentences=2)
            speaking('found on wikipedia')
            speaking(result)
            continue

        elif "your name" in q:
            speaking('I am Ana. Your VA')
            continue

        elif "search web" in q:
            pywhatkit.search(q)
            speaking('that is what I found')
            continue

        elif "play" in q:
            speaking(f'playing{q}')
            pywhatkit.playonyt(q)
            continue

        elif "joke" in q:
            speaking(pyjokes.get_joke())
            continue

        elif("stock price" in q):
            search = q.split("of")[-1].strip()
            lookup= {'apple': 'AAPL',
                    'amazon': 'AMZN',
                    'google': "GOOGL"}
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                currentprice = stock.info["regularMarketPrice"]
                speaking(f'found it, the price for {search} is {currentprice}')
                continue
            except:
                speaking(f'Sorry I have no data for {search}')
            continue
querying()