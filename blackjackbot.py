#this program only works on a 1440x900 screen in and if you line the website up right


import pyautogui
import re
import pytesseract

def main():
    play()
    for i in range(3):
        blackjack(i)
    finished()
    print('Thank you for playing')
    
def play():
    print('Begining poker, you have 3 seconds to go to the screen')
    pyautogui.sleep(3)
    pyautogui.click(920, 502)
    pyautogui.sleep(7)
    pyautogui.click(619, 763)
    pyautogui.sleep(3)
    pyautogui.click(750, 602)
    pyautogui.sleep(3)
    pyautogui.click()
    
def blackjack(n):
    while n + 1 != 4:
        deal()
        hitorstand()
        while n < 4:
            wait() # while the deal text not on screen do not go further
    
def deal():
    pyautogui.sleep(2)
    image = pyautogui.screenshot(region=(823, 472, 187, 100 )) # takes a picture of the deal button
    image.save('dealbutton.png') #saves the deal button picture so it can be used by the next line
    location = list(pyautogui.locateOnScreen('dealbutton.png', confidence=0.4)) # makes a lits so i can draw the locations to click out
    pyautogui.click(location[0]/2.5, location[1]*30) # magic numbers need to be removed they are used cause the scale of the screenshot is not the scale of the pixels on the screen

#the pyautogui refuses to click the hit button because it thinks the stand button is that button i dont know how to increase the accuarcy
#i should have made a function for hitting or make it make more sense instead of the random magic numbers but this works sorta 
def hit():
     pyautogui.sleep(2)
     image = pyautogui.screenshot(region=(226, 468, 170, 100 )) 
     text = pytesseract.image_to_string(image)
     real_text = re.search(r'\bHit\b', text)
     if real_text and 'Hit' in real_text.group():
         pyautogui.click(358, 505)
     else:
         print('no hit button found')
     
    
def stand():
     pyautogui.sleep(2)
     image = pyautogui.screenshot(region=(226, 468, 170, 100 )) # takes a picture of the deal button
     image.save('hitbutton.png') #saves the deal button picture so it can be used by the next line
     image.show()
     location = list(pyautogui.locateOnScreen('hitbutton.png', confidence=0.4)) # makes a lits so i can draw the locations to click out
     pyautogui.click(location[0]/2.5, location[1]*30)

def wait():
    while True:
        image = pyautogui.screenshot(region=(823, 472, 187, 100 ))
        image.save('dealbutton.png')
        text = pytesseract.image_to_string(image)
        real_text = re.search(r'\bDEAL\b', text)
        if real_text and 'DEAl' in real_text.group():
             location = list(pyautogui.locateOnScreen('dealbutton.png', confidence=0.4)) 
             pyautogui.click(location[0]/2.5, location[1]*30) #magic numbers
             break
        else:
            pyautogui.sleep(3)
            continue
    

    
def finished():
    pyautogui.sleep(6)
    pyautogui.click(256, 166)
    pyautogui.sleep(2)
    pyautogui.click(466, 578)
    pyautogui.sleep(2)
    pyautogui.click(659, 741)

def hitorstand():
    pyautogui.sleep(2)
    image = pyautogui.screenshot(region=(798, 647, 200, 100))
    text = pytesseract.image_to_string(image)
    num, player = text.split(' ')
    number = makeint(num)
    while number < 17:
        if number < 17:
            hit()
        elif number >= 17 and number < 21:
            stand()
        else:
            wait()
            
    
def makeint(n):
    return int(n)


if __name__ == '__main__':
    main()