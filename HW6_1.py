import time
from turtle import color


class TrafficLight:
    color = ["крассный", "желтый", "зелёный"]

    def running(self):
        while True:
            print(f"Включается {color[1]} 7 ")
            time.sleep(7)
            print(f"Включается {color[2]}")
            time.sleep(2)
            print(f"Включаем {color[3]}")
            time.sleep(5)


a = TrafficLight()
a.running()