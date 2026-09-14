"""Print the cursor position and pixel color after a five-second delay."""

import time

import pyautogui


def main():
    print("Move the cursor to the target pixel within five seconds.")
    time.sleep(5)
    position = pyautogui.position()
    print(f"Position: {position}")
    print(f"RGB: {pyautogui.pixel(position.x, position.y)}")


if __name__ == "__main__":
    main()
