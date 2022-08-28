import numpy as np
import pyautogui
import time

print(pyautogui.size())

screenshot = pyautogui.screenshot()
screenshot = np.array(screenshot)

L, H = pyautogui.size()[0], pyautogui.size()[1]

pixelTargetList = [[255, 160, 4], [178, 178, 185], [182, 19, 19], [252, 33, 25], [252, 30, 26], [68, 66, 54],
                   [214, 202, 1]]

Turn = 0
Start = True

time.sleep(1)

while True:

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot).tolist()

    # Nature
    if screenshot[990][1350] == [163, 205, 50]:
        # Fin combat
        if Turn > 0:
            print("Fin combat")
            pyautogui.press("esc")

        Turn = 0
        Start = True

        for i in range(H):
            flag = False
            for j in range(L):
                if screenshot[i][j] in pixelTargetList:
                    pyautogui.moveTo(j, i, 0.5)
                    pyautogui.leftClick()

                    screenshot = pyautogui.screenshot()
                    screenshot = np.array(screenshot).tolist()

                    if screenshot[1000][1353] == [66, 213, 215]:
                        flag = True
                    break
            if flag == True:
                break

    # Combat
    else:

        screenshotFight = pyautogui.screenshot()
        screenshotFight = np.array(screenshotFight).tolist()

        if (Start):
            pyautogui.moveTo(1450, 1000, 0.5)
            pyautogui.leftClick()
            Start = False
            pyautogui.moveTo(10, 10, 0.5)

        if Turn == 0:

            if screenshotFight[1000][1353] == [66, 213, 215]:

                # Altéré N°1
                if screenshotFight[1020][981] == [109, 91, 118]:
                    time.sleep(0.5)
                    pyautogui.hotkey("ctrl", "'")

                    screenshotFight = pyautogui.screenshot()
                    screenshotFight = np.array(screenshotFight).tolist()

                    for i in range(H):
                        flag1 = False
                        for j in range(L):
                            if screenshotFight[i][j] == [34, 51, 153]:
                                pyautogui.moveTo(j, i, 0.5)
                                time.sleep(0.5)
                                pyautogui.leftClick()

                                flag1 = True
                                break
                        if flag1 == True:
                            break

                # Altéré N°2
                if screenshotFight[1020][1072] == [109, 91, 118]:
                    time.sleep(0.5)
                    pyautogui.hotkey("ctrl", "-")

                    screenshotFight = pyautogui.screenshot()
                    screenshotFight = np.array(screenshotFight).tolist()

                    for i in range(H):
                        flag2 = False
                        for j in range(L):
                            if screenshotFight[i][j] == [34, 51, 153]:
                                pyautogui.moveTo(j, i, 0.5)
                                time.sleep(0.5)
                                pyautogui.leftClick()

                                flag2 = True
                                break
                        if flag2 == True:
                            break

                # Liberté des altérés
                if screenshotFight[1000][1000] == [162, 134, 82]:
                    time.sleep(0.5)
                    pyautogui.press("'")

                    screenshotFight = pyautogui.screenshot()
                    screenshotFight = np.array(screenshotFight).tolist()

                    for i in range(H):
                        flag3 = False
                        for j in range(L):
                            if screenshotFight[i][j] == [34, 51, 153]:
                                pyautogui.moveTo(j, i, 0.5)
                                time.sleep(0.5)
                                pyautogui.leftClick()

                                flag3 = True
                                pyautogui.moveTo(10, 10, 0.5)
                                break
                        if flag3 == True:
                            break
                    Turn += 1
        else:
            time.sleep(0.5)
            pyautogui.press("f1")
