from pynput.mouse import Button
from pynput.keyboard import Listener, KeyCode
from TMMAutoclick.ClickMouse import ClickMouse

# outter loop and inner loop for looping through TTM
outterlist = []
innerlist = []

init_delay = eval(input("Pre-process delay(Secs): "))
process_delay = eval(input("Processing delay(Secs): "))

start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')
button = Button.left

# receive out loop coordinate X,Y pixels until receive e
print("Insert coordinates for Outter loop in format X,Y separating each with new line\n"
      " and insert an e in the last line to stop inserting")
pix = input()
while pix != "e":
    xy = [eval(x.strip()) for x in pix.split(',')]
    outterlist.append((xy[0], xy[1]))
    pix = input()

# receive inner loop coordinate X,Y pixels until receive e
print("Insert coordinates for Inner loop in format X,Y separating each with new line\n"
      " and insert an e in the last line to stop inserting")
pix = input()
while pix != "e":
    xy = [eval(x.strip()) for x in pix.split(',')]
    innerlist.append((xy[0], xy[1]))
    pix = input()


click_thread = ClickMouse(outterlist, innerlist,init_delay, process_delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()

