# challenge

class Car:
  def __init__(self, model_name, mileage, manufacture):
    self.model_name = model_name
    self.mileage = mileage
    self.manufacture = manufacture
  
  def gas(self):
    print(f"{self.model_name}, {self.mileage}, {self.manufacture}")

  def breaks(self):
    print(f"break: {self.model_name}, {self.mileage}, {self.manufacture}")

if __name__ == '__main__':
  track = Car("suzuki", 16, "ABC")
  volxs = Car("Ameri", 110, "Barkey")

  track.gas()
  track.breaks()

  volxs.gas()
  volxs.breaks()