import pyautogui
import pytesseract

def deal():
    pyautogui.sleep(2)
    image = pyautogui.screenshot(region=(823, 472, 187, 100 )) # takes a picture of the deal button
    image.save('dealbutton.png') #saves the deal button picture so it can be used by the next line
    location = list(pyautogui.locateOnScreen('dealbutton.png', confidence=0.4)) # makes a lits so i can draw the locations to click out
    pyautogui.click(location[0]/2.5, location[1]*30) #
    
deal()
