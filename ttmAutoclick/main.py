from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import threading
import time

# outterloop and innerloop for looping through TTM
outterlist = []
innerlist = []

init_delay = 5
process_delay = 5

start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')
button = Button.left

# recieve out loop coordinate X,Y pixels until receive e
pix = input()
while pix != "e":
    xy = [x.strip() for x in pix.split(',')]
    outterlist.append((xy[0], xy[1]))
    pix = input()

# recieve inner loop coordinate X,Y pixels until receive e
pix = input()
while pix != "e":
    xy = [x.strip() for x in pix.split(',')]
    innerlist.append((xy[0], xy[1]))
    pix = input()


class ClickMouse(threading.Thread):
    def __init__(self, outterloop, innerloop, init_delay, proc_delay, button):
        super(ClickMouse, self).__init__()
        self.mouse = Controller()
        self.outterloop = outterloop
        self.innerloop = innerloop
        self.init_delay = init_delay
        self.proc_delay = proc_delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        time.sleep(self.init_delay)
        l = len(self.outterloop)
        l2 = len(self.innerloop)

        while self.program_running:
            i = 0
            while self.running and (i < l):
                out_pos = self.outterloop[i]
                self.mouse.position(out_pos)
                time.sleep(.200)
                self.mouse.click(self.button)
                time.sleep(self.proc_delay)
                i = i + 1

                j = 0
                while self.running and (j < l2):
                    in_pos = self.innerloop[j]
                    self.mouse.position(in_pos)
                    time.sleep(.200)
                    self.mouse.click(self.button)
                    time.sleep(self.proc_delay)
                    j = j + 1
            time.sleep(0.1)


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

