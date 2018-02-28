from flask import Flask
import json
import Edison

app = Flask(__name__)
edison = Edison.Edison()

# light sensor, sound sensor, vibration sensor

status = ""

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
    print("muy")

# while(True):
#     while(edison.getButtonStatus() == 1):
#         if (not edison.isParty()):
#             pass
#         else:
#             while(edison.isParty()):
#                 edison.displayAlarm()
#             edison.setBuzzerOff()
#             edison.clearScreen()
#
#     if (status == "light"):
#         while(edison.getButtonStatus() == 0):
#             if(not edison.isParty()):
#                 edison.displayLight()
#             else:
#                 while (edison.isParty()):
#                     edison.displayAlarm()
#                 edison.setBuzzerOff()
#         status = "sound"
#
#     elif (status == "sound"):
#         while(edison.getButtonStatus() == 0):
#             if (not edison.isParty()):
#                 edison.displaySound()
#             else:
#                 while (edison.isParty()):
#                     edison.displayAlarm()
#                 edison.setBuzzerOff()
#         status = "vibration"
#
#     elif (status == "vibration"):
#         while(edison.getButtonStatus() == 0):
#             if (not edison.isParty()):
#                 edison.displayVibration()
#             else:
#                 while (edison.isParty()):
#                     edison.displayAlarm()
#                 edison.setBuzzerOff()
#         status = "light"
#
#     else:
#         while(edison.getButtonStatus() == 0):
#             if (not edison.isParty()):
#                 pass
#             else:
#                 while (edison.isParty()):
#                     edison.displayAlarm()
#                 edison.setBuzzerOff()
#                 edison.clearScreen()
#         status = "light"

