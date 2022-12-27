from cow import Cow

#class Dragon extends class Cow
class Dragon(Cow):
  #method canBreatheFire() return True/False
  def canBreatheFire(self):
    return True

  #constructor
  def __init__(self,name, image):
    super().__init__(name) #calling parent's constructor
    self.image = image
