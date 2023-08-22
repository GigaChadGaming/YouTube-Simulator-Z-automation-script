import pydirectinput
import time


# ask user for roblox app/screen resolution
def AskResolution():
    print("Please select your screen resolution")
    print("Type 1 for 1920x1080")
    print("Type 2 for 2560x1440")
    screenSize = input()
    return screenSize


resInput = int(AskResolution())
if resInput > 2:
    print("Sorry, that is not a valid option\n")
    resInput = int(AskResolution())

if resInput < 1:
    print("Sorry, that is not a valid option\n")
    resInput = int(AskResolution())

repeatCount = input("Please enter the amount of times you would like the script to repeat\n")
# #############################################################################################################
# 1920x1080

if resInput == 1:

    for x in repeatCount:
        time.sleep(2)

        pydirectinput.press('1')
        for i in range(30):
            pydirectinput.click()

        pydirectinput.keyDown('s')
        time.sleep(1)
        pydirectinput.keyUp('s')

        time.sleep(1)

        # sit in chair
        pydirectinput.moveTo(955, 513)
        pydirectinput.move(1, 1)
        pydirectinput.click()

        time.sleep(1)

        # open video editor
        pydirectinput.moveTo(791, 76)
        pydirectinput.move(1, 1)
        pydirectinput.click()
        pydirectinput.click()

        # edit
        pydirectinput.move(0, 250)
        for i in range(30):
            pydirectinput.keyDown('e')
            pydirectinput.keyUp('e')

        # export
        pydirectinput.moveTo(1346, 330)
        pydirectinput.move(1, 1)
        pydirectinput.click()
        pydirectinput.moveTo(1220, 644)
        pydirectinput.move(1, 1)
        pydirectinput.click()

        # click ok
        time.sleep(1)
        pydirectinput.moveTo(960, 627)
        pydirectinput.move(1, 1)
        pydirectinput.click()

        # exit edit window
        # pydirectinput.moveTo(2187, 278)
        # pydirectinput.move(1, 1)
        # pydirectinput.click()

        # open Photoshop
        pydirectinput.moveTo(486, 75)
        pydirectinput.move(1, 1)
        pydirectinput.click()
        pydirectinput.click()

        # make thumbnail
        pydirectinput.move(0, 450)
        for i in range(55):
            pydirectinput.keyDown('e')
            pydirectinput.keyUp('e')

        # save thumbnail
        pydirectinput.moveTo(1463, 712)
        pydirectinput.move(1, 1)
        pydirectinput.click()

        # open YouTube
        # pydirectinput.moveTo(218, 126)
        # pydirectinput.move(1, 1)
        # pydirectinput.click()
        # pydirectinput.click()

        # close pc
        pydirectinput.moveTo(900, 968)
        pydirectinput.move(1, 1)
        pydirectinput.click()

        # get out of chair
        pydirectinput.press('space')

        # go outside the house
        pydirectinput.keyDown('w')
        time.sleep(2)
        pydirectinput.keyUp('w')

# #############################################################################################################
# 2560x1440

if resInput == 2:
    time.sleep(2)
    for x in repeatCount:
        pydirectinput.press('1')
        for i in range(30):
            pydirectinput.click()

        pydirectinput.keyDown('s')
        time.sleep(1)
        pydirectinput.keyUp('s')

        time.sleep(1)

        # sit in chair
        pydirectinput.moveTo(1286, 695)
        pydirectinput.move(1, 1)
        pydirectinput.click()

        time.sleep(1)

        # open video editor
        pydirectinput.moveTo(1061, 128)
        pydirectinput.move(1, 1)
        pydirectinput.click()
        pydirectinput.click()

        # edit
        pydirectinput.move(0, 500)
        for i in range(30):
            pydirectinput.keyDown('e')
            pydirectinput.keyUp('e')

        # export
        pydirectinput.moveTo(1651, 425)
        pydirectinput.move(1, 1)
        pydirectinput.click()
        pydirectinput.moveTo(1684, 824)
        pydirectinput.move(1, 1)
        pydirectinput.click()

        # click ok
        time.sleep(1)
        pydirectinput.moveTo(1331, 840)
        pydirectinput.move(1, 1)
        pydirectinput.click()

        # exit edit window
        # pydirectinput.moveTo(2187, 278)
        # pydirectinput.move(1, 1)
        # pydirectinput.click()

        # open Photoshop
        pydirectinput.moveTo(624, 108)
        pydirectinput.move(1, 1)
        pydirectinput.click()
        pydirectinput.click()

        # make thumbnail
        pydirectinput.move(0, 450)
        for i in range(55):
            pydirectinput.keyDown('e')
            pydirectinput.keyUp('e')

        # save thumbnail
        pydirectinput.moveTo(1987, 986)
        pydirectinput.move(1, 1)
        pydirectinput.click()

        # open YouTube
        # pydirectinput.moveTo(218, 126)
        # pydirectinput.move(1, 1)
        # pydirectinput.click()
        # pydirectinput.click()

        # close pc
        pydirectinput.moveTo(1271, 1308)
        pydirectinput.move(1, 1)
        pydirectinput.click()

        # get out of chair
        pydirectinput.press('space')

        # go outside the house
        pydirectinput.keyDown('w')
        time.sleep(2)
        pydirectinput.keyUp('w')
