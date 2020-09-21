import os
import random
import pyautogui
import time
import glob
from PIL import Image

def fish():
    ##Paramater Setting##
    TIME = "light"    #night/day
    CONFIDENCE=0.75
    CHECK_GAME_FILE=f"check_game.png"
    GAME_STAR_FILE=f"game_star.png"
    BUOY_W = 16
    BUOY_H = 24

    BUOY = {"night":[f"buoy/night_up.png", f"buoy/night_left.png"], 
            "day":[f"buoy/day_up.png", f"buoy/day_left.png"],
            "light":[f"buoy/light_up.png", f"buoy/light_left.png"]

            }
    BUOY_X = 1
    BUOY_Y = 1
    BUOY_FILE_CHECK = [f"buoy/1.png", f"buoy/2.png", f"buoy/3.png", f"buoy/4.png", f"buoy/5.png", f"buoy/6.png",f"buoy/7.png", f"buoy/8.png" , f"buoy/9.png", f"buoy/10.png"]

    # Flick the bar and judge whether the float can be detected normally.
    def first_step():
        #global BUOY_X, BUOY_Y
        pyautogui.mouseDown()   #Swing
        time.sleep(0.3+0.7*random.random())
        pyautogui.mouseUp()
        time.sleep(1.3)
        print("in 33")
        for i in BUOY_FILE_CHECK:
            a = pyautogui.locateOnScreen(i, confidence=CONFIDENCE) # Find buoy
            if (a != None):
                BUOY_X, BUOY_Y, temp1, temp2 = a
                print("found,%d,%d", BUOY_X, BUOY_Y)
                print(i)
                result = [i, BUOY_X, BUOY_Y]
                return result
        return "None"
        
    # Determine if a fish has been caught,the x1, y1 is the position of buoy.
    def second_step(x1, y1, BUOY_FILE):
        monitor_left=x1-5
        monitor_top=y1-5
        print("file",BUOY_FILE)
        for i in range(0,1000):
            pyautogui.screenshot(f'de/monitor_bobber_{i}.png', region=(monitor_left, monitor_top, BUOY_W+10, BUOY_H+10))
            target = pyautogui.locate(BUOY_FILE, f"de/monitor_bobber_{i}.png", confidence=0.6)
            if(target==None):
                return 1
        return 0

    # Fishing games.
    def third():
        pyautogui.click()
        time.sleep(0.2)
        for i in range(0,100):
            pyautogui.screenshot(f'de/monitor_game_{i}.png', region=(813, 540, 284, 32))
            target = pyautogui.locate(CHECK_GAME_FILE, f"de/monitor_game_{i}.png", confidence=0.95)
            if(target!=None):
                break
            if (i==99):
                return 0
			    
        for i in range(0,3000):
            pyautogui.screenshot(f'de/monitor_game_{i}.png', region=(813, 540, 284, 32))
            target = pyautogui.locate(GAME_STAR_FILE, f"de/monitor_game_{i}.png", confidence=0.6)
            if(target==None):
                pyautogui.mouseUp()
                return 1
            x2,y2,h,l = target
            if (x2<152):
                pyautogui.mouseDown()
            else:
                pyautogui.mouseUp()
        return 0 
    # Delete temp file
    def clean():
        monitor_images = glob.glob('de/monitor_*.png')
        for image in monitor_images:
            os.remove(image)
    
    while(True):
        clean()
        first_step_result = first_step()
        if (first_step_result != "None"):
            x1 = first_step_result[1]
            y1 = first_step_result[2]
            print(x1)
        else:
            print("No buoy found!")
            pyautogui.click()
            time.sleep(3) 
            continue
        if(second_step(x1, y1, first_step_result[0])):
            if (third()):
                print("it is ok")
            else:
                continue
            time.sleep(2)
        else:
            pyautogui.click()
            time.sleep(2)       


if __name__=="__main__":
    time.sleep(4)
    fish()

def small_game():
    CHECK_GAME_FILE=f"check_game.png"
    GAME_STAR_FILE=f"game_star.png"
    pyautogui.click()
    time.sleep(0.2)
    for i in range(0,200):
        pyautogui.screenshot(f'de/monitor_game_{i}.png', region=(813, 540, 284, 32))
        target = pyautogui.locate(CHECK_GAME_FILE, f"de/monitor_game_{i}.png", confidence=0.95)
        if(target!=None):
            break
        if (i==199):
            return 0
                        
    for i in range(0,3000):
        pyautogui.screenshot(f'de/monitor_game_{i}.png', region=(813, 540, 284, 32))
        target = pyautogui.locate(GAME_STAR_FILE, f"de/monitor_game_{i}.png", confidence=0.6)
        if(target==None):
            pyautogui.mouseUp()

            # Delete temp file
            monitor_images = glob.glob('de/monitor_*.png')
            for image in monitor_images:
                os.remove(image)

            return 1
        x2,y2,h,l = target
        if (x2<152):
            pyautogui.mouseDown()
        else:
            pyautogui.mouseUp()
    return 0 

