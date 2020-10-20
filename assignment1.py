import pyautogui

def clicker():
    im = pyautogui.screenshot()
    CurrPixel = im.getpixel((670,630))

    pyautogui.moveTo(140, 450)
    target = pyautogui.position()
    
    while target==(140,450):
        target = pyautogui.position()
        pyautogui.doubleClick()
        if pyautogui.pixelMatchesColor(670, 630, (255, 255, 255)):
            pyautogui.click(670, 630)
        elif pyautogui.pixelMatchesColor(700, 680, (175, 176, 170)):
            pyautogui.click(700,680)
        elif pyautogui.pixelMatchesColor(700, 750, (178, 178, 166)):
            pyautogui.click(700, 750)
        if pyautogui.pixelMatchesColor(700, 820, (174, 172, 159)):
            pyautogui.click(700, 820)
        pyautogui.click(140, 450)
        
clicker()

