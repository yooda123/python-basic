from car import Car

class Track(Car):
  def __init__(self, model_name, mileage, manufacture, max_capacity):
      super().__init__(model_name, mileage, manufacture)
      self._max_capacity = max_capacity
      self._capacity = 0

  def gas(self):
    if self._capacity > self._max_capacity:
      print("重量オーバーなので走れません")
      print(f"最低でも{self._capacity - self._max_capacity}tの荷物を降ろしてください")
    else:
      super().gas()

  def load(self, weight):
    if weight > 0:
      # 荷物積む
      self._capacity += weight
      print(f"{self._capacity}tの荷物を積みました")
    else:
      # 荷物降ろす
      if self._capacity <= -weight:
        print(f"{self._capacity}t全ての荷物を降ろしました")
        self._capacity = 0
      else:
        print(f"{self._capacity}tの荷物を降ろしました")
        self._capacity += weight
      
    if self._capacity > self._max_capacity:
      print("最大積載量をオーバーしました")

    print(f"現在の積載量は{self._capacity}tです")
    


if __name__ == '__main__':
  track = Track("suzuki", 16, "ABC", 100)
  track.gas()
  track.breaks()
  track.load(101)
  track.gas()
  track.load(-1000)
  track.gas()
