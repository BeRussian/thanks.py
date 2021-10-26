import random

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
import schedule
import time
import webbrowser
import pyautogui as pg







def send_message(reciver, msg):

  pre = "+972"

  url = f"http://web.whatsapp.com/send?phone={pre}{reciver},&text=,{msg}"
  print(url)

  #open web brower
  webbrowser.get().open(url , 2)

  time.sleep(10)

  pg.moveTo(960, 540) 
  pg.click()
  pg.press('enter')
  print("ENTER PRESSED")
  time.sleep(1)
  pg.keyDown('Ctrl') # for windows Ctrl
  pg.press('w')
  pg.keyUp("Ctrl")
  time.sleep(0.5)
  pg.press('enter')



def emoji():
  emogies = ["\U0001F600" , "\U0001F601" , "\U0001F605" , "\U0001F642" , "\U0001F607"]
  rnd = random.randint(0,1)
  choose = -1
  if rnd == 1:
      choose = random.randint(0,len(emogies)-1)
      return emogies[choose]
  return "" 

def sentence():
  thanks = ["האוכל היה טעים מאוד" , "תודה רבה על האוכל" , "היה טעים","תודה על האוכל"]
  choose = random.randint(0,len(thanks)-1)
  return thanks[choose]


def timi():
  hour = random.randint(12,15) #(12:00 - 15:300)
  minute = random.randint(0,59)
  if minute<10:
      minute = str("0"+str(minute))
  time = f"{str(hour)}:{str(minute)}"
  return time



def main():
  reciver_number = "549244589" #format - "532464670" (without the zero at the start)

  timer = timi()
  final = sentence() + emoji()
  send_message(reciver_number, final)
  print(timer)
    
schedule.every().day.at(timi()).do(main)



while 1:
    schedule.run_pending()
    time.sleep(1)







