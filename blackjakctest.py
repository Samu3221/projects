import pytesseract # gives the text on the screen
import pyautogui 
import time

# textx,texty = pyautogui.position() use in find position program
image = pyautogui.screenshot()
#use image directly to pytesseract
text = pytesseract.image_to_string(image)
#time.sleep(2)
#print(f'x is {textx}\ny is{texty}')
print(text)