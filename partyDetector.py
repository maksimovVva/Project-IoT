import Edison

edison = Edison.Edison()

# light sensor, sound sensor, vibration sensor

status = ""

while(True):
    while(edison.getButtonStatus() == 1):
        if (not edison.isParty()):
            pass
        else:
            edison.sendMessage()
            while(edison.isParty()):
                edison.displayAlarm()
            edison.setBuzzerOff()
            edison.clearScreen()

    if (status == "light"):
        while(edison.getButtonStatus() == 0):
            if(not edison.isParty()):
                edison.displayLight()
            else:
                edison.sendMessage()
                while (edison.isParty()):
                    edison.displayAlarm()
                edison.setBuzzerOff()
        status = "sound"

    elif (status == "sound"):
        while(edison.getButtonStatus() == 0):
            if (not edison.isParty()):
                edison.displaySound()
            else:
                edison.sendMessage()
                while (edison.isParty()):
                    edison.displayAlarm()
                edison.setBuzzerOff()
        status = "vibration"

    elif (status == "vibration"):
        while(edison.getButtonStatus() == 0):
            if (not edison.isParty()):
                edison.displayVibration()
            else:
                edison.sendMessage()
                while (edison.isParty()):
                    edison.displayAlarm()
                edison.setBuzzerOff()
        status = "light"

    else:
        while(edison.getButtonStatus() == 0):
            if (not edison.isParty()):
                pass
            else:
                edison.sendMessage()
                while (edison.isParty()):
                    edison.displayAlarm()
                edison.setBuzzerOff()
                edison.clearScreen()
        status = "light"

