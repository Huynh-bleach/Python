
import speech_recognition
from gtts import gTTS
import os
import datetime

import playsound
from datetime import date
#from datetime import date, datetime
import wikipedia
import webbrowser as wb
import dieukienamluong
robot_ear = speech_recognition.Recognizer()
def speak(text):
       tts = gTTS(text=text, lang='vi')
       filename = "voice.mp3"
       tts.save(filename)
       playsound.playsound(filename)
       os.remove(filename)








def introduction():
    speak("Bạn có thể cho tôi biết tên của bạn là gì không để tôi có thể dễ xưng hô")
    global name
    name = namefull().lower()
def welcome():
    
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <11:
        speak(f"Chào buổi sáng {vocative} {name} ")
    elif hour >= 11 and hour<13:
        speak(f"Chào buổi trưa {vocative} {name}")
    elif hour >= 13 and hour<18:
        speak(f"Chào buổi chiều {vocative} {name}")
    else:
        speak(f"Chào buổi tối {vocative} {name}")
    speak(f"Tôi có thể giúp gì cho {vocative} {name} đây")
def command():
    with speech_recognition.Microphone() as sourse:

        print("Rotbot: Tôi đang nghe nè")
        audio_data = robot_ear.record(sourse, duration=5)
    print("Robot: . . .")
    try:
        text = robot_ear.recognize_google(audio_data, language="vi")
    except:
        print("Tôi không hiểu bạn đang nói gì hay bạn hãy nhập thứ bạn tìm đi")
        speak("Tôi không hiểu bạn đang nói gì hay bạn hãy nhập thứ bạn tìm đi")
        text = str(input("lệnh của bạn là:"))
    print("you:" + text)
    return text
def namefull():
    with speech_recognition.Microphone() as sourse:

        print("Rotbot: Tôi đang nghe tên của bạn đây")
        audio_data = robot_ear.record(sourse, duration=3)
    print("Robot: . . .")
    try:
        text = robot_ear.recognize_google(audio_data, language="vi")
    except:
        print("Bạn không cho tôi biết tên bạn là gì phải không vậy thì tôi gọi bạn là kẻ nguy hiểm nhe")
        speak("Bạn không cho tôi biết tên bạn là gì phải không vậy thì tôi gọi bạn là kẻ nguy hiểm nhe")
        text = "Kẻ nguy hiểm"
    return text
    
robot_brain = ""
global vocative
vocative = "ông trùm"
introduction()
welcome()

while True:
    with speech_recognition.Microphone() as sourse:

        print(f"Rotbot: {vocative} {name} hãy nói đi tôi đang nghe đây")
        audio_data = robot_ear.record(sourse, duration=5)
    print("Robot: . . .")
    try:
        you = robot_ear.recognize_google(audio_data, language="vi")
    except:
        you = ""
    print("you:" + you)
    

    if you =="":
        robot_brain = f"Tôi không thể nghe thấy {vocative} {name} đang nói gì, hãy thử lại"
        speak(robot_brain)
    elif "Xin chào" in you:
        robot_brain = f"hello {vocative} {name}"
        speak(robot_brain)
    elif "hôm nay" in you:
        today = date.today()
        robot_brain = today.strftime("Hôm nay là ngày %d tháng %m năm %Y")
        speak(robot_brain)  
    elif "mấy giờ" in you:  
        robot_brain = datetime.datetime.now().strftime("%H Giờ %M Phút %S giây")
        speak(robot_brain)
    elif "Goodbye" in you or "kết thúc" in you:
        robot_brain = f"Bye {vocative} {name}, hẹn gặp lại {vocative} {name} lần sau "
        speak(robot_brain)
        break
    elif "Google" in you:
        speak(f"{vocative} {name} muốn tìm cái gì")
        search = command().lower()
        url= f"https://www.google.com.vn/search?q={search}"
        wb.get().open(url)
        speak(f"tôi đã tìm thấy {search} trên google")
    elif "YouTube" in you:
        speak(f"{vocative} {name} muốn tìm cái gì")
        search = command().lower()
        url= f"https://www.youtube.com/search?q={search}"
        wb.get().open(url)
        speak(f"tôi đã tìm thấy {search} trên Youtube")
    elif "Facebook" in you:
        speak(f"{vocative} {name} muốn tìm cái gì")
        search = command().lower()
        url= f"https://www.facebook.com/search?q={search}"
        wb.get().open(url)
        speak(f"tôi đã tìm thấy {search} trên Youtube")
    elif "điều chỉnh âm lượng" in you:
         dieukienamluong.volumcontrol()
    elif you:
        wikipedia.set_lang("vi")
        robot_brain = wikipedia.summary(you, sentences=1)
        speak(robot_brain)   
    else:
        robot_brain = " tôi khỏe cảm ơn còn bạn"
        speak(robot_brain)
    print("Robot:" + robot_brain)




   
    
