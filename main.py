import pyautogui
import time

pyautogui.alert("A automação vai ser iniciada, não aperte nada.")
pyautogui.PAUSE = 0.5

# abrir o google drive no seu computador
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/my-drive")
pyautogui.press('enter')

# entrar na minha área de trabalho
pyautogui.hotkey('winleft', 'd')

print(pyautogui.position())

# clicar e arrastar o arquivo para o google drive
pyautogui.moveTo(1858, 34)
pyautogui.mouseDown()
pyautogui.moveTo(936, 628)

# # enquanto arrasta, mudar para o chrome
pyautogui.hotkey('alt', 'tab')

# # largar o arquivo
pyautogui.mouseUp()

time.sleep(5)
pyautogui.alert("A automação foi finalizada")



#pyautogui.KEYBOARD_KEYS
#pyautogui.position()

