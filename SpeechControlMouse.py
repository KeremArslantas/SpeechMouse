import speech_recognition as sr
import pyautogui

# İşlevler
def up():
    pyautogui.move(0, -50)

def down():
    pyautogui.move(0, 50)

def left():
    pyautogui.move(-50, 0)

def right():
    pyautogui.move(50, 0)

def click():
    pyautogui.click()

def scrool_up():
    pyautogui.scroll(15)

def scrool_down():
    pyautogui.scroll(-15)

# Ses tanıma
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Komut bekleniyor...")
        audio = r.listen(source)

    try:
        komut = r.recognize_google(audio, language="en-US").lower()
        print(f"Anlasilan komut: {komut}")

        if "up" in komut:
            up()
        elif "down" in komut:
            down()
        elif "left" in komut:
            left()
        elif "right" in komut:
            right()
        elif "click" in komut:
            click()
        elif "exit" in komut:
            break
    except sr.UnknownValueError:
        print("Ses algilanamadi.")
    except sr.RequestError as e:
        print(f"Hata: {str(e)}")
