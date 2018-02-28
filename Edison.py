import mraa
import pyupm_i2clcd
import pyupm_grove as grove
import pyupm_ldt0028 as ldt0028
import pyupm_mic as upmMicrophone
import time
from random import randint
from thread import *
import urllib

class Edison(object):

  
  def __init__(self):
    self.screen = pyupm_i2clcd.Jhd1313m1(6, 0x3E, 0x62)
    self.clearScreen()

    self.light = grove.GroveLight(2)

    self.mic = upmMicrophone.Microphone(1)
    self.threshContext = upmMicrophone.thresholdContext()
    self.threshContext.averageReading = 0
    self.threshContext.runningAverage = 0
    self.threshContext.averagedOver = 2

    self.piezo = ldt0028.LDT0028(0)

    self.button =  mraa.Gpio(3)
    self.button.dir(mraa.DIR_IN)

    self.buzzer = mraa.Gpio(6)
    self.buzzer.dir(mraa.DIR_OUT)
    self.buzzer.write(0)

  def clearScreen(self):
    self.screen.clear()
    self.screen.setColor(50, 50, 255)
    self.screen.setCursor(0, 0)
    self.screen.write("PartyDetector")
    self.screen.setCursor(1, 0)
    self.screen.write("is ready!")

  def getLoudness(self):
    buffer = upmMicrophone.uint16Array(128)
    len = self.mic.getSampledWindow(2, 128, buffer)
    thresh = 0
    if len:
      thresh = self.mic.findThreshold(self.threshContext, 30, buffer, len)
    return thresh

  def getBrightness(self):
    return self.light.value()

  def getVibration(self):
    return self.piezo.getSample()

  def getButtonStatus(self):
    return self.button.read()

  def setBuzzerOn(self):
    self.buzzer.write(1)

  def setBuzzerOff(self):
    self.buzzer.write(0)

  def displayLight(self):
    self.screen.clear()
    self.screen.setColor(75, 50, 50)
    self.screen.setCursor(0, 0)
    self.screen.write("Light Sensor")
    self.screen.setCursor(1, 0)
    self.screen.write(str(self.getBrightness()))
    time.sleep(0.5)

  def displaySound(self):
      ss = self.getLoudness()
      self.screen.clear()
      self.screen.setColor(50, 75, 50)
      self.screen.setCursor(0, 0)
      self.screen.write("Sound Sensor")
      self.screen.setCursor(1, 0)
      self.screen.write(str(ss))
      time.sleep(0.5)

  def displayVibration(self):
      ss = self.getVibration()
      self.screen.clear()
      self.screen.setColor(50, 50, 75)
      self.screen.setCursor(0, 0)
      self.screen.write("Vibration Sensor")
      self.screen.setCursor(1, 0)
      self.screen.write(str(ss))
      time.sleep(0.5)

  def displayAlarm(self):
      self.screen.clear()
      self.screen.setColor(randint(0, 255), randint(0, 255), randint(0, 255))
      # sound = self.getLoudness()
      # light = self.getBrightness()
      # vibration = self.getVibration()
      # self.screen.setCursor(0, 0)
      # self.screen.write(str(light))
      # self.screen.setCursor(0, 5)
      # self.screen.write(str(sound))
      # self.screen.setCursor(1, 3)
      # self.screen.write(str(vibration))
      self.screen.setCursor(0, 0)
      self.screen.write("PARTY")
      self.screen.setCursor(1, 0)
      self.screen.write("IS DETECTED!")
      self.setBuzzerOn()
      time.sleep(0.01)

  def isParty(self):
    sound = self.getLoudness()
    light = self.getBrightness()
    vibration = self.getVibration()
    sumStatus = 0
    if (sound > 130):
        sumStatus += 1
    if (light > 50):
        sumStatus += 1
    if (vibration > 18):
        sumStatus += 1
    party = False
    if (sumStatus >= 2):
        party = True
    return party

  def getSensorsValue(self):
    sound = self.getLoudness()
    light = self.getBrightness()
    vibration = self.getVibration()
    dictionary = ({})
    dictionary["Ligth Sensor"] = light
    dictionary["Sound Sensor"] = sound
    dictionary["Vibration Sensor"] = vibration
    if(self.isParty()):
        dictionary["Status"] = "PARTY IS DETECTED!"
    else:
        dictionary["Status"] = "Party is not detected!"
    return dictionary

  def sendMessage(self):
    url = "https://sms.ru/sms/send?api_id=BDEBF543-3DBB-273B-96C8-928C78CABFB5&to=79082356289&msg=PARTY+IS+DETECTED!!!+:)&json=0"
    urllib.urlopen(url)

