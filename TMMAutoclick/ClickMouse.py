import threading
import time
from pynput.mouse import Controller


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
                self.mouse.position = out_pos
                time.sleep(.200)
                self.mouse.click(self.button)
                time.sleep(self.proc_delay)
                i = i + 1

                j = 0
                while self.running and (j < l2):
                    in_pos = self.innerloop[j]
                    self.mouse.position = in_pos
                    time.sleep(.200)
                    self.mouse.click(self.button)
                    time.sleep(self.proc_delay)
                    j = j + 1
            time.sleep(0.1)

