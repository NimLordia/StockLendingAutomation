import pyautogui, time

time.sleep(5)  # Gives 5 seconds to place mouse at desired pixel
print(pyautogui.position())
print(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y))
