from pynput import mouse, keyboard
import time
from helper import Helper

def run():
  print('RUN')
  helper = Helper(keyboard.Controller(), keyboard.Key)
  helper.alt_tab_step(10)

for i in range(1,4):
  print(i)
  time.sleep(1)

print('GO')
while(True):
  time.sleep(10)
  run()
