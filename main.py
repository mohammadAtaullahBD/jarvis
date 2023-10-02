import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime

chatStr = ""




def chat(voiceQuery):
    global chatStr
    # print(chatStr)
    openai.api_key = apikey
    chatStr += f"User: {voiceQuery}\n Jarvis: "
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as error:
        say(f"Sorry, some error occurred from api and the error is {error}")


def ai(prompt):
    openai.api_key = apikey
    text = f""

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.py", "w") as f:
        f.write(text)


def say(text):
    os.system(f'say "{text}"')


def takeCommand():
    r = sr.Recognizer()
    print('start listening')
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        audio = r.listen(source)
        print("Recognizing...")
        voiceQuery = r.recognize_google(audio)
        print(f"User said: {voiceQuery}")
        return voiceQuery


if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")

    while True:
        print("Listening...")
        try:
            query = takeCommand()
        except Exception as e:
            say(f"Sorry from Jarvis, some error occurred while taking command")
            continue

        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hour {minute} minutes")

        # todo: Add a feature to play a specific song
        # elif "open music" in query:
        #     musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
        #     os.system(f"open {musicPath}")

        # elif "open facetime".lower() in query.lower():
        #     os.system(f"open /System/Applications/FaceTime.app")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Take my command".lower() in query.lower():
            command = input('Enter you command')
            ai(prompt=command)

        elif "exit jarvis".lower() in query.lower():
            say('Jarvis exiting, Have a good day!')
            exit()

        elif "reset the chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)

        # say(query)

