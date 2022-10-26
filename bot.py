# import pyautogui as p
# import time

# WIN = p.click('win.png')
# time.sleep(1)

# SEARCH = p.write('paint')
# time.sleep(1)

# x, y = p.locateCenterOnScreen('paint.png')
# p.moveTo(x, y)
# p.click()

import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')