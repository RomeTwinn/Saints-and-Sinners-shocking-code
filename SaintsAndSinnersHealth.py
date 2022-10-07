import pyautogui
import time
import serial

serialport = serial.Serial('COM7', baudrate=9600)
barmargin = 56
health = 0
newhealth = 0
tol = 45
recheck = False
r = 232
g = 248
b = 27

while 1:
    # add a region instead of the whole screen
    img = pyautogui.screenshot()
    heart = pyautogui.locate("heart.png", img, confidence=0.92)
    balloon = pyautogui.locate("balloon.png", img, confidence=0.92)

    # print("Heart:", heart)
    # print("Balloon:", balloon)

    if heart is not None and balloon is not None:
        rightX = int(heart[0] + barmargin)
        leftX = int(balloon[0] - barmargin)
        centerY = int(((heart[1] + balloon[1]) / 2) + 21) #added 21 to center to the bar
        # (232, 248, 27)
        for x in range(rightX, leftX, 25):
            p = img.getpixel((x, centerY))
            # pyautogui.moveTo(x, centerY)
            if (r + tol) > p[0] > (r - tol) and (g + tol) > p[1] > (g - tol) and (b + tol) > p[2] > (b - tol):
                newhealth = x - rightX
            else:
                break
    if newhealth < health:
        print(" ")
        print("SHOCK")
        print(" ")
        serialport.write("s".encode('utf-8'))
    health = newhealth
    print("Health:", health)

    time.sleep(.7)
    # time.sleep(3)