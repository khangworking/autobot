import time

class Helper:
  def __init__(self, controller, key):
    self.controller = controller
    self.key = key

  def get_controller(self):
    return self.controller

  def get_key(self):
    return self.key

  def keep_alt_tab(self):
    self.controller.press(self.key.alt_l)
    self.controller.press(self.key.tab)

  def release_alt_tab(self):
    self.controller.release(self.key.alt_l)
    self.controller.release(self.key.tab)

  def alt_tab_step(self, step):
    self.keep_alt_tab()
    for i in range(step):
      self.controller.release(self.key.tab)
      time.sleep(0.5)
      self.controller.press(self.key.tab)
    self.release_alt_tab()

  def keep_ctrl_with(self, key):
    self.controller.press(self.key.ctrl_l)
    self.controller.press(key)

  def release_ctrl_with(self, key):
    self.controller.release(self.key.ctrl_l)
    self.controller.release(key)

  def ctrl_pgDw_step(self, step):
    self.keep_ctrl_with(self.key.page_down)
    for i in range(step):
      self.controller.release(self.key.page_down)
      time.sleep(0.12)
      self.controller.press(self.key.page_down)
    self.release_ctrl_with(self.key.page_down)
