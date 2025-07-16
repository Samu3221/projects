import pytesseract
import pyautogui
import re

def hit():
     pyautogui.sleep(2)
     image = pyautogui.screenshot(region=(226, 468, 170, 100 )) # takes a picture of the deal button
     text = pytesseract.image_to_string(image)
     real_text = re.search(r'\bHit\b', text)
     if real_text and 'Hit' in real_text.group():
         pyautogui.click(358, 505)
     else:
         print('no hit button found')
hit()