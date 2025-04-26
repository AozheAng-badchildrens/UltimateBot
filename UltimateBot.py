from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
from dhooks import Webhook
import xlrd
import time
import random
import os
import pytesseract
import pyautogui as py
from datetime import datetime
from datetime import date
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from playsound import playsound

hook = Webhook("https://discord.com/api/webhooks/")
PATH = "C:\Program Files (x86)\chromedriver.exe"
keyboard = Controller()
file_location = "C:\Math\schedule.xlsx"
schedule = xlrd.open_workbook(file_location)
sheet = schedule.sheet_by_index(0)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Local\Programs\Tesseract-OCR\tesseract'
bit = 1
ytho = False
recordingended = False
timessent = 0

# Start Up
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
})
driver = webdriver.Chrome(PATH,options=chrome_options)

def isbetweentime(sh,sm,eh,em,curr_h,curr_m):
    if (sh == eh):
        if (curr_h == sh):
            if (sm <= curr_m <= em - 1):
                return True
        return False
    if (sh == curr_h):
        if (sm <= curr_m):
            return True
        return False
    elif (eh == curr_h):
        if (em - 3 >= curr_m):
            return True
        return False
    else:
        if (sh <= eh):
            if (sh < curr_h < eh):
                return True
            return False
        else:
            if (sh < curr_h <= 23):
                return True
            elif (0 <= curr_h < eh):
                return True
            return False
    return False

def Mockingbird():
    # Turn volume to 100%
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-10.0, None) #max
    hook = Webhook("https://discord.com/api/webhooks/")
    bug = "Error Occured at: " + str(findTime()[0]) + ' : ' + str(findTime()[1])
    hook.send(bug)
    # playsound('C:\Playlist\Mockingbird.mp3')

def openava():
    py.moveTo(29,1054)
    py.click()
    time.sleep(1)
    py.moveTo(1079,1050,duration=0.2)
    py.click(1079,1050)
    time.sleep(1)
    py.moveTo(996,960,duration=0.2)
    py.click(996,960)
    time.sleep(1)
    py.moveTo(1895,8,duration=0.2)
    py.click(1895,8)
    time.sleep(1)
    py.moveTo(207,1051,duration=0.2)
    py.click(207,1051)
    time.sleep(1)
    py.typewrite("google chrome")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    py.typewrite("web.ava.me")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(40)
    py.moveTo(993,677,duration=0.2)
    py.click()
    time.sleep(40)
    py.moveTo(1549,402,duration=0.2)
    py.click(1549,402)
    time.sleep(1.5)
    py.moveTo(608,666,duration=0.2)
    py.click(608,666)
    time.sleep(1.5)
    py.moveTo(834,390,duration=0.2)
    py.click(834,390)
    time.sleep(1.5)
    py.moveTo(1175,661,duration=0.2)
    py.click(1175,661)
    time.sleep(1.5)
    py.moveTo(1195,996,duration=0.2)
    py.click(1195,996)
    time.sleep(1.5)
    py.moveTo(1266,1049,duration=0.2)
    py.click(1266,1049)
    time.sleep(1.5)

def reconnect():
    py.moveTo(236,1048,duration=0.5)
    py.click(236,1048)
    time.sleep(2)
    py.typewrite("expressvpn")
    time.sleep(2)
    py.moveTo(644,650,duration=0.5)
    py.click(644,650)
    time.sleep(10)
    py.moveTo(1423,1054,duration=0.5)
    py.click(1423,1054)
    time.sleep(2)
    py.moveTo(236,1048,duration=0.5)
    py.click(236,1048)
    time.sleep(2)
    py.typewrite("expressvpn")
    time.sleep(2)
    py.moveTo(343,390,duration=0.5)
    py.click(343,390)
    time.sleep(15)
    py.moveTo(958,382,duration=0.5)
    py.click(958,382)
    time.sleep(15)
    py.moveTo(1267,1050,duration=0.2)
    py.dragTo(1120,1049,duration=0.4)
    time.sleep(1)

def press_and_release(key):
    keyboard.press(key)
    keyboard.release(key)

def findTime():
    now = datetime.now().time()
    return (now.hour,now.minute)

def reply(word):
    py.moveTo(19,1051)
    py.click()
    time.sleep(0.7)
    py.moveTo(1259,1048)
    py.click()
    time.sleep(0.7)
    py.moveTo(1613,118)
    py.click()
    time.sleep(0.7)
    py.moveTo(1634,870)
    py.click()
    time.sleep(0.2)
    py.typewrite(word)
    press_and_release(Key.enter)

def copy():
    keyboard.press(Key.ctrl)
    keyboard.press("c")
    keyboard.release("c")
    keyboard.release(Key.ctrl)

def copyall():
    keyboard.press(Key.ctrl)
    keyboard.press("a")
    keyboard.release("a")
    keyboard.press("c")
    keyboard.release("c")
    keyboard.release(Key.ctrl)

def checkmic():
    py.moveTo(29,1054)
    py.click()
    time.sleep(1)
    py.moveTo(1072,1044)
    py.click()
    time.sleep(0.5)
    py.moveTo(915,920)
    py.click()
    time.sleep(0.4)
    py.moveTo(175,1048)
    py.click()
    time.sleep(0.4)
    py.typewrite("snip")
    time.sleep(0.4)
    press_and_release(Key.enter)
    time.sleep(0.4)
    py.moveTo(1374,448)
    py.click()
    time.sleep(0.5)
    py.moveTo(106,380)
    py.dragTo(176,408,duration=0.5)
    time.sleep(1)
    save()
    time.sleep(1)
    press_and_release(Key.enter)
    time.sleep(0.5)
    press_and_release(Key.left)
    time.sleep(0.5)
    press_and_release(Key.enter)
    time.sleep(1)
    py.moveTo(622,163)
    py.click()
    string = pytesseract.image_to_string("C:\Random Stuff\Capture.png")
    if ("Ava Mic" in string):
        return True
    return False

def paste():
    keyboard.press(Key.ctrl)
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release(Key.ctrl)

def save():
    keyboard.press(Key.ctrl)
    keyboard.press("s")
    keyboard.release("s")
    keyboard.release(Key.ctrl)

def getava():
    py.moveTo(1082,1049,duration=0.01)
    py.click(1082,1049)
    time.sleep(0.01)
    py.moveTo(1011,957,duration=0.01)
    py.click(1011,957)
    time.sleep(0.01)
    py.moveTo(1141,119,duration=0.01)
    py.click(1141,119)
    time.sleep(0.01)

def selectall():
    keyboard.press(Key.ctrl)
    keyboard.press("a")
    keyboard.release("a")
    keyboard.release(Key.ctrl)

def getArt():
    py.moveTo(1195,1053,duration=0.01)
    py.click(1195,1053)
    time.sleep(0.01)
    py.moveTo(119,366,duration=0.01)
    py.click(119,366)
    time.sleep(0.01)
    py.moveTo(965,283,duration=0.01)
    py.click(965,283)

def getELA():
    py.moveTo(1195,1053,duration=0.01)
    py.click(1195,1053)
    time.sleep(0.01)
    py.moveTo(171,401,duration=0.01)
    py.click()
    time.sleep(0.01)
    py.moveTo(965,283,duration=0.01)
    py.click(965,283)

def turnmicon():
    py.moveTo(1077,1045,duration=0.2)
    py.click(1077,1045)
    time.sleep(0.2)
    py.moveTo(962,953,duration=0.2)
    py.click(962,953)
    time.sleep(0.2)
    py.moveTo(1871,219,duration=0.2)
    py.click(1871,219)
    time.sleep(0.2)
    py.moveTo(609,664,duration=0.2)
    py.click(609,664)
    time.sleep(0.2)
    py.moveTo(843,385,duration=0.2)
    py.click(843,385)
    time.sleep(0.2)
    py.moveTo(1179,662,duration=0.2)
    py.click(1179,662)
    time.sleep(0.2)
    py.moveTo(1199,990,duration=0.2)
    py.click(1199,990)
    time.sleep(0.2)
    py.moveTo(1194,1053)
    py.click()

def connectowifi():
    py.moveTo(1610,1051)
    py.click()
    time.sleep(5)
    py.moveTo(1647,451)
    py.click()
    time.sleep(0.2)
    py.moveTo(1769,558)
    py.click()
    time.sleep(3)
    py.moveTo(1459,1052)
    py.click()
    time.sleep(0.2)

def snipVPN():
    py.moveTo(262,1055)
    py.click()
    time.sleep(0.7)
    py.typewrite("snip")
    keyboard.press(Key.enter)
    time.sleep(0.7)
    py.moveTo(1365,448)
    py.click()
    time.sleep(0.7)
    py.moveTo(717,125)
    py.dragTo(1208,896,duration=0.5)
    time.sleep(0.7)
    save()
    time.sleep(0.7)
    keyboard.press(Key.enter)
    time.sleep(0.7)
    py.moveTo(1009,526)
    py.click()
    time.sleep(0.7)
    py.moveTo(1325,12)
    py.click()
    time.sleep(0.7)

def checkVPN():
    global bit
    py.moveTo(1142,1053)
    py.click()
    time.sleep(0.2)
    snipVPN()
    time.sleep(1)
    s = pytesseract.image_to_string('C:\Random Stuff\Capture.png')
    if ("Connected" in s):
        return True
    else:
        if ("Connecting" in s or "Reconnecting" in s):
            if ("VPN will reconnect when available" in s or "Internet connection lost" in s):
                connectowifi()
            else:
                time.sleep(30)
        elif ("Not Connected" in s):
            py.moveTo(967,392)
            py.click()
            time.sleep(30)
        elif ("Unable" in s):
            Mockingbird()
        return False

def checkifdisconnected():
    global bit
    py.moveTo(646,1048)
    py.click()
    time.sleep(0.7)
    py.moveTo(514,929)
    py.click()
    time.sleep(0.5)
    py.moveTo(219,1056)
    py.click()
    py.typewrite("snip")
    keyboard.press(Key.enter)
    time.sleep(0.7)
    py.moveTo(1362,450)
    py.click()
    time.sleep(0.7)
    py.moveTo(468,92)
    time.sleep(0.7)
    py.dragTo(1342,535,duration=0.3)
    time.sleep(0.7)
    save()
    keyboard.press(Key.enter)
    time.sleep(0.7)
    py.moveTo(1009,530,duration=0.4)
    py.click()
    time.sleep(0.5)
    py.moveTo(1477,17)
    py.click()
    time.sleep(0.7)
    string = pytesseract.image_to_string('C:\Random Stuff\Capture.png')
    if ("Trying to connect" in string or "Reconnecting" in string or "Connection lost" in string):
        py.moveTo(1207,1054)
        py.click()
        time.sleep(0.1)
        return True
    py.moveTo(1207,1054)
    py.click()
    time.sleep(0.1)
    return False

def checkifjoined():
    py.moveTo(231,1058)
    py.click()
    time.sleep(0.5)
    py.typewrite("snip")
    time.sleep(0.2)
    press_and_release(Key.enter)
    time.sleep(1)
    py.moveTo(1373,450)
    py.click()
    time.sleep(1)
    py.moveTo(5,949)
    py.dragTo(110,996,duration=0.5)
    time.sleep(1)
    save()
    time.sleep(2)
    press_and_release(Key.enter)
    time.sleep(1)
    press_and_release(Key.left)
    time.sleep(1)
    press_and_release(Key.enter)
    time.sleep(1)
    py.moveTo(623,624)
    py.click()
    time.sleep(1)
    string = pytesseract.image_to_string("C:\Random Stuff\Capture.png")
    if (":" in string or "AM" in string or "PM" in string):
        return True
    return False

def doattendance(string):
    if ("attendance" in string or "Attendance" in string):
        index = string.find("ttendance")
        substr = string[index : ]
        if ("Jason" in substr or "Valerie" in substr or "Michael" in substr):
            time.sleep(2)
            return True
    return False

def listen_to_name(endh,endm,ID):
    global bit
    if (ID == "d563p7ixjx"):
        File = "ELA.txt"
    elif (ID == "fpnutfqhjk"):
        File = "Art.txt"
    else:
        File = "ELA.txt"
    nn = 0
    respondarr = ["hi","hello","I'm here",'Hi',"Hello","present","Michael is here","here"]
    n = 0
    cc = 0
    previouscount = [0]
    string = ""
    replied = False
    hook = Webhook("https://discord.com/api/webhooks/")
    isinbreakout = False
    timesjoined = 0
    while True:
        getava()
        copyall()
        time.sleep(0.01)
        if (File == "Art.txt"):
            getArt()
        else:
            getELA()
        time.sleep(0.01)
        selectall()
        time.sleep(0.01)
        paste()
        save()
        time.sleep(0.02)
        if (n % 100 == 0 and n > 1):
            checkifdisconnected()
        if (n % 23 == 0):
            if (checkmic() == False):
                openava()
        with open(File,"r") as f:
            time.sleep(0.02)
            string = f.read()
            num = string.count("Michael")
            if ("Joining conversation..." in string and timesjoined <= 2):
                timesjoined+=1
                py.moveTo(1081,1046)
                py.click()
                keyboard.press(Key.ctrl)
                keyboard.press("r")
                keyboard.release(Key.ctrl)
                keyboard.release("r")
                time.sleep(60)
                py.moveTo(942,677)
                py.click()
                time.sleep(0.5)
                py.moveTo(610,667)
                py.click()
                time.sleep(0.5)
                py.moveTo(819,406)
                py.click()
                time.sleep(0.5)
                py.moveTo(951,450)
                py.click()
                time.sleep(0.5)
                py.moveTo(1201,662)
                py.click()
                time.sleep(0.5)
                py.moveTo(1199,990)
                py.click()
            if ("No Internet connection. Reconnecting..." in string):
                cc += 1
                if (cc > 4):
                    if (checkifdisconnected() == True):
                        connectovpn()
                        return
            else:
                cc = 0
            if (doattendance(string) and replied == False):
                replied = True
                try:
                    reply(random.choice(respondarr))
                    string = "Successfully Replied here at " + str(findTime()[0]) + ' : ' + str(findTime()[1])
                    hook.send(string)
                except:
                    hook.send("Failed to Reply!")
            f.close()   
        n+=1
        time.sleep(1)
        if (num not in previouscount and nn < 1):
            nn += 1
            previouscount.append(num)
            reply(respondarr[random.randrange(0,2)])
            pol = "Replied at " + str(findTime()[0]) + ' : ' + str(findTime()[1])
            hook.send(pol)
        if ("OFF" in (string[len(string) - 10 : ])):
            turnmicon()
        if ("Search Ava Room" in string):
            py.moveTo(21,1051)
            py.click()
            time.sleep(0.5)
            py.moveTo(1085,1056)
            py.click()
            time.sleep(0.5)
            py.moveTo(947,937)
            py.click()
            time.sleep(0.5)
            py.moveTo(1055,676)
            py.click()
            time.sleep(15)
            py.moveTo(615,664)
            py.click()
            time.sleep(1)
            py.moveTo(865,413)
            py.click()
            time.sleep(1)
            py.moveTo(1184,669)
            py.click()
            time.sleep(1)
            py.moveTo(1192,991)
            py.click()
            time.sleep(1)
        if (n % 4 == 0 and n > 1):
            if (isclassover() == True):
                string = "Left Class Successfully at " + str(findTime()[0]) + ' : ' + str(findTime()[1])
                hook.send(string)
                driver.get('https://meet.google.com/landing?hs=193&pli=1&authuser=1')
                if (bit == 1):
                    bit -= 1
                return
        if (isinbreakout == False):
            if (n % 30 == 0 and n > 1):
                try:
                    breako = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div[2]/span/span')
                    breako.click()
                    isinbreakout = True
                    try:
                        hook = Webhook("https://discord.com/api/webhooks/")
                    except:
                        pass
                    try:
                        chatt = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[3]/span/button')
                        chatt.click()
                        time.sleep(2)
                    except:
                        hook = Webhook("https://discord.com/api/webhooks/")
                        hook.send("Failed to open chat!")
                except:
                    isinbreakout = False
        else:
            try:
                leavebreakout = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
                leavebreakout.click()
                isinbreakout = False
                hook = Webhook("https://discord.com/api/webhooks/")
                hook.send("Left breakout!")
            except:
                isinbreakout = True
        if (int(findTime()[0]) >= endh and int(findTime()[1]) >= endm):
            hook = Webhook("https://discord.com/api/webhooks/")
            driver.get("https://meet.google.com/landing?hs=193&pli=1&authuser=1")
            time.sleep(10)
            string = "Left Class Successfully at " + str(findTime()[0]) + ' : ' + str(findTime()[1])
            hook.send(string)
            py.moveTo(1266,1049,duration=0.2)
            py.click(1266,1049)
            time.sleep(1.5)
            if (bit == 0):
                bit += 1
            return

def isclassover():
    global ytho
    py.moveTo(21,1052)
    py.click()
    time.sleep(0.7)
    py.moveTo(1266,1056)
    py.click()
    time.sleep(0.7)
    py.moveTo(300,1054)
    py.click()
    time.sleep(0.7)
    py.typewrite("snip")
    keyboard.press(Key.enter)
    time.sleep(0.7)
    py.moveTo(1376,452)
    py.click()
    time.sleep(0.7)
    py.moveTo(1453,174)
    py.click()
    time.sleep(0.7)
    py.dragTo(1863,837,duration=0.3)
    time.sleep(0.7)
    save()
    time.sleep(0.7)
    press_and_release(Key.enter)
    time.sleep(0.7)
    press_and_release(Key.left)
    time.sleep(0.7)
    press_and_release(Key.enter)
    time.sleep(0.7)
    py.moveTo(1882,17)
    py.click()
    time.sleep(0.7)
    string = pytesseract.image_to_string('C:\Random Stuff\Capture.png').lower()
    if (string.count("here") >= 3 and ytho == False):
        ytho = True
        try:
            reply("here")
            hook = Webhook("https://discord.com/api/webhooks/")
            pol = "Replied here at " + str(findTime()[0]) + ' : ' + str(findTime()[1])
            hook.send(pol)
        except:
            pass
    if ((string.count("bye") + string.count("Bye") + string.count("see you")) >= 2 or (string.count("au revoir") + string.count("Au revoir") + string.count("a la prochaine") + string.count("A la prochaine")) >= 2):
        return True
    return False

def startrecording():
    py.moveTo(25,1050)
    py.click()
    time.sleep(0.5)
    py.moveTo(647,1045)
    py.click()
    time.sleep(1)
    py.moveTo(1643,56)
    py.click()
    time.sleep(5)
    py.moveTo(1725,522)
    py.click()
    time.sleep(2)
    py.moveTo(897,536)
    py.click()
    time.sleep(1)
    py.moveTo(1184,757)
    py.click()
    time.sleep(1)
    py.moveTo(1184,805)
    py.click()
    time.sleep(1)
    py.moveTo(1241,951)
    py.click()

def endrecording():
    py.moveTo(25,1050)
    py.click()
    time.sleep(0.5)
    py.moveTo(647,1045)
    py.click()
    time.sleep(1)
    py.moveTo(514,929)
    py.click()
    time.sleep(0.5)
    py.moveTo(1640,58)
    py.click()

def blockcam():
    py.moveTo(1760,62,duration=0.2)
    py.click()
    time.sleep(0.1)
    py.moveTo(1452,237,duration=0.2)
    py.click()
    time.sleep(0.1)
    py.moveTo(1755,439,duration=0.2)
    py.click()
    time.sleep(2)

def connectovpn():
    global bit
    reconnect()
    if (bit == 0):
        bit += 1
    yeeted = 0
    while (checkVPN() == False):
        time.sleep(10)
        yeeted += 1
        if (yeeted >= 4):
            Mockingbird()

def joinmeeting(ID,endh,endm,starth,startm):
    global bit
    hook = Webhook("https://discord.com/api/webhooks/")
    if (checkifdisconnected() == True):
        connectovpn()
        return
    time.sleep(1)
    py.moveTo(1266,1051,duration=0.1)
    py.click()
    time.sleep(0.1)
    a = ID
    b = endh
    c = endm
    driver.get('https://meet.google.com/landing?hs=193&pli=1&authuser=1')
    # Turn Volume to 0%
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-60.9, None) #min
    try:
        # Enter Meeting Code
        meet = driver.find_element_by_xpath('//*[@id="i3"]')
        meet.send_keys(ID)
        meet.send_keys(Keys.RETURN)
        time.sleep(5)
        times = 1
        while (driver.title == "Google Meet" and times <= 6):
            times += 1
            driver.refresh()
            time.sleep(15)
            try:
                meet = driver.find_element_by_xpath('//*[@id="i3"]')
                meet.send_keys(ID)
                meet.send_keys(Keys.RETURN)
            except:
                pass
            time.sleep(30)
        if (times > 7):
            hook.send("No Class Today or wrong ID!")
            if (bit == 1):
                bit -= 1
            return
        time.sleep(40)
        driver.implicitly_wait(15)
        # Block camera and mic
        try:
            LMFAO = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
            LMFAO.click()
        except:
            blockcam()
            time.sleep(3)
        # Join Meeting
        try:
            join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
            join.click()
        except:
            try:
                join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
                join.click()
            except:
                try:
                    join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span')
                    join.click()
                except:
                    py.moveTo(1342,635)
                    py.click()
        hook = Webhook("https://discord.com/api/webhooks/")
        driver.implicitly_wait(40)
        time.sleep(20)
        if (checkifjoined() == True):
            string = "Class Successfully joined at " + str(findTime()[0]) + ' : ' + str(findTime()[1])
            hook.send(string)
        else:
            string = "Failed to Join Class at " + str(findTime()[0]) + ' : ' + str(findTime()[1])
            hook.send(string)
            if (bit == 0):
                bit += 1
            return
        # Open Chat
        try:
            chatt = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[3]/span/button')
            chatt.click()
            time.sleep(2)
        except:
            hook.send("Failed To Open Chat!")
        if (ID == "d563p7ixjx" or ID == "fpnutfqhjk"):
            if (ID == "d563p7ixjx"):
                startrecording()
            try:
                openava()
                time.sleep(2)
                listen_to_name(endh,endm,ID)
            except:
                pass
        if (driver.title == "Google Meet"):
            if (bit == 1):
                bit -= 1
            return 
        isinbreakout = False
        po = 0
        while (isbetweentime(starth,startm,endh,endm,int(findTime()[0]),int(findTime()[1])) == True):
            po+=1
            if (po % 6 == 0 and po > 1):
                if (checkifdisconnected() == True):
                    connectovpn()
                    return
            try:
                textarea = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[4]/div[1]/div[1]/div[2]/textarea')
                textarea.click()
                time.sleep(2)
            except:
                try:
                    chat = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[3]/span/button')
                    chat.click()
                except:
                    pass
            if (po % 5 == 0 and po > 1):
                if (isinbreakout == False):
                    try:
                        breako = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div[2]/span/span')
                        breako.click()
                        isinbreakout = True
                        hook.send("In breakout!")
                    except:
                        isinbreakout = False
                else:
                    try:
                        leavebreakout = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
                        leavebreakout.click()
                        hook.send("Left breakout!")
                    except:
                        pass
            if (isclassover() == True):
                string = "Left Class Successfully at " + str(findTime()[0]) + ' : ' + str(findTime()[1])
                hook.send(string)
                driver.get('https://meet.google.com/landing?hs=193&pli=1&authuser=1')
                if (bit == 1):
                    bit -= 1
                return
            time.sleep(2)
        while True:
            if (int(findTime()[0]) >= endh and int(findTime()[1]) >= endm):
                if (ID == 'fpnutfqhjk'):
                    os.system('shutdown -s -t 30')
                try:
                    string = "Left Class Successfully at " + str(findTime()[0]) + ' : ' + str(findTime()[1])
                    hook.send(string)
                    driver.get('https://meet.google.com/landing?hs=193&pli=1&authuser=1')
                    if (bit == 0):
                        bit += 1
                except:
                    hook.send("Failed to leave class!")
                break
        py.moveTo(1267,1050,duration=0.2)
        py.click(1267,1050)
        time.sleep(1)
    except:
        Mockingbird()
        if (checkifdisconnected() == True):
            connectovpn()
        return

def backwordsearch(s):
    for i in range(len(s)-1,-1,-1):
        if (s[i] == '/'):
            return i

def getlink():
    py.moveTo(922,341)
    py.dragTo(496,346,duration=0.5)
    copy()
    time.sleep(0.7)
    time.sleep(0.2)
    getArt()
    time.sleep(0.1)
    selectall()
    time.sleep(0.1)
    paste()
    time.sleep(0.1)
    save()
    time.sleep(0.2)
    with open("Art.txt",'r') as f:
        string = f.read()
        ind = backwordsearch(string) + 1
        string = string[ind : ]
        f.close()
    return string

def openexcel():
    py.moveTo(773,1051)
    py.click()
    time.sleep(0.5)
    py.moveTo(573,223)
    py.click()
    time.sleep(0.5)
    py.typewrite("C:\Math\schedule.xlsx")
    press_and_release(Key.enter)

def getschedule():
    py.moveTo(1079,1055)
    py.click()
    time.sleep(2)
    py.moveTo(1898,8)
    py.click()
    time.sleep(0.5)
    py.moveTo(1079,1055)
    py.click()
    time.sleep(2)
    py.moveTo(877,61)
    py.click()
    py.typewrite("https://classroom.google.com/u/2/h")
    press_and_release(Key.enter)
    time.sleep(10)
    py.moveTo(158,316)
    py.click()
    time.sleep(5)
    string = getlink()
    time.sleep(0.2)
    openexcel()
    time.sleep(2)
    py.moveTo(178,469)
    py.click()
    time.sleep(0.2)
    press_and_release(Key.backspace)
    time.sleep(0.2)
    py.typewrite(string)
    time.sleep(0.5)
    save()
    time.sleep(0.5)
    py.moveTo(1080,1050)
    py.click()
    time.sleep(0.7)
    py.moveTo(1690,522)
    py.click()
    time.sleep(0.2)
    py.moveTo(38,129)
    py.click()
    time.sleep(0.5)
    py.moveTo(116,575)
    py.click()
    time.sleep(4)
    string = getlink()
    openexcel()
    time.sleep(2)
    py.moveTo(190,493)
    py.click()
    time.sleep(0.5)
    press_and_release(Key.backspace)
    time.sleep(0.5)
    py.typewrite(string)
    save()
    time.sleep(1)
    py.moveTo(1080,1050)
    py.click()
    time.sleep(0.7)
    py.moveTo(1690,522)
    py.click()
    time.sleep(0.2)
    py.moveTo(38,129) 
    py.click()
    time.sleep(1)
    py.moveTo(175,654)
    py.click()
    time.sleep(3)
    string = getlink()
    openexcel()
    time.sleep(2)
    py.moveTo(186,513)
    py.click()
    time.sleep(0.5)
    press_and_release(Key.backspace)
    time.sleep(0.5)
    py.typewrite(string)
    time.sleep(1)
    save()
    time.sleep(1)
    py.moveTo(1080,1050)
    py.click()
    time.sleep(0.7)
    py.moveTo(1690,522)
    py.click()
    time.sleep(0.2)
    py.moveTo(38,129)
    py.click()
    time.sleep(1)
    py.moveTo(119,502)
    py.click()
    time.sleep(3)
    string = getlink()
    openexcel()
    time.sleep(1)
    py.moveTo(200,541)
    py.click()
    time.sleep(0.5)
    press_and_release(Key.backspace)
    time.sleep(0.7)
    py.typewrite(string)
    time.sleep(1)
    save()
    time.sleep(1)
    py.moveTo(1523,177)
    py.click()
    time.sleep(0.5)
    py.moveTo(1373,32)
    py.click()
    time.sleep(0.5)

def readschedule():
    global bit
    global ytho
    schedule = xlrd.open_workbook(file_location)
    sheet = schedule.sheet_by_index(0)
    current_time = findTime()
    for i in range(1,5):
        starthour = int(sheet.cell_value(i,3)[1:len(sheet.cell_value(i,3))-1])
        startmin = int(sheet.cell_value(i,6)[1:len(sheet.cell_value(i,6))-1])
        endhour = int(sheet.cell_value(i,9)[1:len(sheet.cell_value(i,9))-1])
        endmin = int(int(sheet.cell_value(i,12)[1:len(sheet.cell_value(i,12))-1]))
        if (int(current_time[0]) == endhour and (int(current_time[1]) == endmin or int(current_time[1]) == endmin + 1 or int(current_time[1]) == endmin + 2)):
            if (bit == 0):
                bit += 1 
        if (int(current_time[0]) == starthour and ((int(current_time[1]) == startmin) or int(current_time[1]) == startmin + 1 or int(current_time[1]) == startmin + 2)):
            if (bit == 0):
                bit += 1
        if (isbetweentime(starthour,startmin,endhour,endmin,int(current_time[0]),int(current_time[1]))):
            if (bit == 1):
                # getschedule()
                # time.sleep(2)
                schedule = xlrd.open_workbook(file_location)
                sheet = schedule.sheet_by_index(0)
                time.sleep(1)
                ytho = False
                joinmeeting(sheet.cell_value(i,0),endhour,endmin,starthour,startmin)

def background_process():
    global recordingended
    global timessent
    if (int(findTime()[0]) == 1 and int(findTime()[1]) == 38):
        if (recordingended == False):
            endrecording()
            recordingended = True
    if (int(findTime()[0]) == 2 and int(findTime()[1]) >= 41):
        if (timessent < 2):
            py.moveTo(25,1050)
            py.click()
            time.sleep(0.5)
            py.moveTo(647,1045)
            py.click()
            time.sleep(1)
            py.moveTo(514,929)
            py.click()
            time.sleep(1)
            py.moveTo(1173,799)
            py.click()
            time.sleep(1)
            py.moveTo(947,1049)
            py.click()
            time.sleep(1)
            py.moveTo(839,774)
            py.click()
            time.sleep(0.3)
            paste()
            time.sleep(0.3)
            press_and_release(Key.enter)
            timessent += 1
    if (int(findTime()[0]) == 2 and int(findTime()[1]) >= 43):
        os.system("shutdown -s -t 20")
    readschedule()
    time.sleep(10)

# Main Program
try:
    # Login
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+
    'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+
    '&flowName=GlifWebSignIn&flowEntry = ServiceLogin') 
    driver.implicitly_wait(20) 
    loginbox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
    loginbox.send_keys("3534841@gapps.yrdsb.ca")
    loginbox.send_keys(Keys.RETURN)
    time.sleep(20)
    while (driver.title != 'YRDSB Google Apps Single Sign On'):
        time.sleep(1)
    login = driver.find_element_by_xpath('//*[@id="UserName"]')
    login.send_keys("3534941")
    lul = driver.find_element_by_xpath('//*[@id="Password"]')
    lul.send_keys("7qjev3")
    lul.send_keys(Keys.RETURN)
    time.sleep(10)
    driver.implicitly_wait(15)
    py.moveTo(1804,100,duration=0.5)
    py.click(1804,100)
    time.sleep(4)
    while (driver.title != 'Gmail'):
        time.sleep(1)
    py.moveTo(1125,577)
    py.click()
    time.sleep(15)
    while (driver.title[14 : ] != '303941@gapps.yrdsb.ca - York Region District School Board Mail'):
        time.sleep(1)

    # Google Meet
    driver.get("https://meet.google.com/landing?hs=193&pli=1&authuser=1")
    driver.implicitly_wait(5)

    while True:
        background_process()

except:
    Mockingbird()
    hook = Webhook("https://discord.com/api/webhooks/")
    if (checkifdisconnected() == True):
        connectovpn()
    hook.send('Connection Error!')
    while True:
        background_process()