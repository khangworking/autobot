from pynput import mouse, keyboard
import time
from helper import Helper
from random import randint

def run():
  time.sleep(randint(5, 10))
  helper = Helper(keyboard.Controller(), keyboard.Key)
  helper.alt_tab_step(10)

for i in range(1, 4):
  print(i)
  time.sleep(1)

print('GO')
while(True):
  run()
