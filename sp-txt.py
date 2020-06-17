import pyautogui as auto
import speech_recognition as sr

while True:
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Speak Anything :")
      audio = r.listen(source)
      try:
         text = r.recognize_google(audio)
         #print("You said : {}".format(text))
         print(f"you said : {text} ")
         auto.typewrite(f'{text}\n')
         
      except:
         print("Sorry could not recognize what you said")